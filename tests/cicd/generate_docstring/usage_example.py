// Example use of a_plus_b function in Test class
public class Main {
    public static void main(String[] args) {
        // Simple addition
        int sum = Test.a_plus_b(5, 3);
        System.out.println("Sum: " + sum); // Outputs: Sum: 8

        // Comparison using a function to get the key
        int comparisonResult = Test.a_plus_b(
            obj -> (Integer) obj,
            10,
            5
        );
        System.out.println("Comparison Result: " + comparisonResult); // Outputs: 1
    }
}
