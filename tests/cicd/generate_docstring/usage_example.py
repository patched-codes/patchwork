public class Main {
    public static void main(String[] args) {
        // Example 1: Adding two integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example 2: Comparing two objects using a keymap
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        int comparisonResult = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison Result: " + comparisonResult); // Output: -1
    }
}
