public class Main {
    public static void main(String[] args) {
        // Use a_plus_b to sum two integers
        int sum = Test.a_plus_b(3, 4);
        System.out.println("Sum: " + sum);  // Output: Sum: 7

        // Compare two objects using a custom key map
        int result = Test.a_plus_b(obj -> ((String) obj).length(), "apple", "banana");
        System.out.println("Comparison result: " + result);  // Output: Comparison result: -1
    }
}
