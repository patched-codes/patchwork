public class Main {
    public static void main(String[] args) {
        // Example of a_plus_b with integers
        int sum = Test.a_plus_b(3, 4);
        System.out.println("Sum: " + sum); // Output: Sum: 7

        // Example of a_plus_b with keymap function
        int comparison = Test.a_plus_b(String::length, "apple", "banana");
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
