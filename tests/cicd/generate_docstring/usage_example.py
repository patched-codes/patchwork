public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers:
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Outputs: Sum: 15

        // Example usage of a_plus_b with a keymap function:
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        int comparison = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison result: " + comparison); // Outputs: -1
    }
}
