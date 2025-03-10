// Demonstration of using the Test class

public class Main {
    public static void main(String[] args) {
        // Example 1: Simple addition using a_plus_b with integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example 2: Comparison using a_plus_b with a keymap (lambda) function
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        int comparisonResult = Test.a_plus_b(keymap, 20, 10);
        System.out.println("Comparison Result: " + comparisonResult); // Output: Comparison Result: 1
    }
}
