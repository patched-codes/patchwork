// Import necessary packages
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Usage example for a_plus_b with integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Usage example for a_plus_b with a keymap function
        String[] words = {"apple", "orange"};
        int comparisonResult = Test.a_plus_b(String::length, words[0], words[1]);
        System.out.println("Comparison: " + comparisonResult); // Output: Comparison: -1
    }
}
