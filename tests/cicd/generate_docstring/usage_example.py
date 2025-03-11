public class ExampleUsage {
    public static void main(String[] args) {
        // Using a_plus_b for simple summation
        int sum = Test.a_plus_b(3, 5);
        System.out.println("Sum: " + sum); // Output: Sum: 8

        // Using a_plus_b for comparison with keymap
        int comparison = Test.a_plus_b(String::length, "short", "longer");
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
