import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b
        int sum = Test.a_plus_b(10, 20);
        System.out.println("Sum: " + sum);  // Output: Sum: 30

        // Example usage of a_plus_b with function comparator
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        int comparisonResult = Test.a_plus_b(keymap, 5, 15);
        System.out.println("Comparison Result: " + comparisonResult);  // Output: -1
    }
}
