public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b for basic addition
        int sum = Test.a_plus_b(4, 5);
        System.out.println("Sum: " + sum); // Output: Sum: 9

        // Example usage of a_plus_b for comparison using a keymap
        int comparison = Test.a_plus_b(
            x -> ((Comparable) x.toString()).length(), // keymap function based on string length
            "apple", 
            "banana"
        );
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
