import java.util.HashMap;
import java.util.Hashtable;

public class Encoder {
    public static String toValidMessage(String message) {
        return message.toLowerCase().replaceAll("[^a-z]+", "");
    }

    public static String toValidEncoded(String encoded) {
        return encoded.replaceAll("[^0-9]+", "");
    }

    private static String map(char c) {
        return Integer.toString(c - 'a' + 1);
    }

    private static char unmap(String s) {
        int val = Integer.parseInt(s) + 'a' - 1;
        if (val < 'a' || val > 'z') {
            return (char) -1;
        }

        return (char) val;
    }

    public static String encode(String message) {
        String ans = "";
        for (int i = 0; i < message.length(); i++) {
            ans += map(message.charAt(i));
        }

        return ans;
    }

    private static long possibilities_trivial(String substr) {
        if (substr.length() == 0) {
            return 1;
        }

        long ways = 0;
        if (unmap(substr.substring(0, 1)) != (char) -1) {
            ways += possibilities_trivial(substr.substring(1));

            if (substr.length() > 1 && unmap(substr.substring(0, 2)) != (char) -1) {
                ways += possibilities_trivial(substr.substring(2));
            }
        }

        return ways;
    }

    private static final HashMap <String, Long> mapped = new HashMap <String, Long> ();

    private static long possibilities_dp(String substr) {
        if (substr.length() == 0) {
            return 1;
        }

        int first = substr.charAt(0) - '0';
        if (first == 0) {
            return 0;
        }

        String remainder = substr.substring(1);

        Long ways1 = mapped.get(remainder);
        if (ways1 == null) {
            ways1 = possibilities_dp(remainder);
            mapped.put(remainder, ways1);
        }

        if (remainder.length() == 0) {
            return ways1;
        }

        int second = remainder.charAt(0) - '0' + 10 * first;
        if (second > 26) {
            return ways1;
        }

        remainder = remainder.substring(1);
        Long ways2 = mapped.get(remainder);
        if (ways2 == null) {
            ways2 = possibilities_dp(remainder);
            mapped.put(remainder, ways2);
        }

        return ways1 + ways2;
    }

    public static long possibilities(String encoded, String mode) {
        switch (mode) {
            case "trivial":
            case "slow":
                return possibilities_trivial(encoded);

            case "dynamic":
            case "dp":
            case "fast":
            default:
                return possibilities_dp(encoded);
        }
    }

    public static long possibilities(String encoded) {
        return possibilities(encoded, "fast");
    }
}