public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        int sum = Test.a_plus_b(5, 7);
        System.out.println("Sum: " + sum); // Output: Sum: 12

        // Example usage of a_plus_b with keymap function
        int comparison = Test.a_plus_b(o -> (Integer) o, 3, 9);
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
