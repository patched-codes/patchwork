public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integer addition
        int result = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + result); // Output: Sum: 15

        // Example usage of a_plus_b with object comparison
        int comparisonResult = Test.a_plus_b(
            obj -> ((String) obj).length(), 
            "apple", 
            "banana"
        );
        System.out.println("Comparison Result: " + comparisonResult); // Output: -1
    }
}
