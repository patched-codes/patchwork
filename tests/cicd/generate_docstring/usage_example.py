public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with simple numbers
        int sum = Test.a_plus_b(3, 4);
        System.out.println("Sum: " + sum); // Output: Sum: 7

        // Example usage of a_plus_b with custom keymap
        String a = "apple";
        String b = "banana";
        int comparison = Test.a_plus_b(String::length, a, b);
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
