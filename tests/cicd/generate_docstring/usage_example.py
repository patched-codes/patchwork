import java.util.function.Function;

public class ExampleUsage {
    public static void main(String[] args) {
        // Example of `a_plus_b(Integer, Integer)`
        int result1 = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + result1);  // Output: Sum: 15

        // Example of `a_plus_b(Function<Object, Comparable>, Object, Object)`
        Function<Object, Comparable> keyMapper = obj -> ((String) obj).length();
        int comparisonResult = Test.a_plus_b(keyMapper, "apple", "pear");
        System.out.println("Comparison Result: " + comparisonResult);  // Output: Comparison Result: 0
    }
}
