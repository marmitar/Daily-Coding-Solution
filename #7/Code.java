public class Code {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Message needed");
            return;
        }

        String msg = args[0];
        System.out.println("Message: " + msg);

        msg = Encoder.encode(msg);
        System.out.println("Encoded: " + msg);

        long start = System.currentTimeMillis();
        long ans = Encoder.possibilities(msg, "slow");
        long end = System.currentTimeMillis();
        System.out.println("Decoding (slow): " + ans + " in " + (end - start) + "ms");

        start = System.currentTimeMillis();
        ans = Encoder.possibilities(msg, "fast");
        end = System.currentTimeMillis();
        System.out.println("Decoding (fast): " + ans + " in " + (end - start) + "ms");
    }
}