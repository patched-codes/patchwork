import java.util.Comparator;
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with two integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum of 5 and 10: " + sum);  // Output: Sum of 5 and 10: 15

        // Example usage of a_plus_b with a keymap for comparison
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        int comparisonResult = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison result: " + comparisonResult);  // Output: Comparison result: -1
    }
}
