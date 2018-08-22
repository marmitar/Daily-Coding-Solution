public class Code {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Code OPERATION MESSAGE");
            return;
        }

        String msg;

        switch (args[0].toLowerCase()) {
            case "encode":
                msg = Encoder.toValidMessage(args[1]);
                System.out.println("Message: " + msg);

                msg = Encoder.encode(msg);
            break;
            case "decode":
                msg = Encoder.toValidEncoded(args[1]);
            break;
            default:
                System.out.println("Unknown operation");
                return;
        }

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