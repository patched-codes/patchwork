import java.util.function.Function;

public class TestExample {
    public static void main(String[] args) {
        Integer result1 = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + result1);  // Output: Sum: 15

        Function<Object, Comparable> keymap = o -> (Integer) o;
        int comparisonResult = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison: " + comparisonResult);  // Output: Comparison: -1
    }
}
