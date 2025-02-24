import java.util.function.Function;

public class TestExample {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example usage of overloaded a_plus_b with keymap for comparison
        Function<Object, Comparable> keymap = obj -> (Comparable) obj;
        int compareResult = Test.a_plus_b(keymap, 100, 50);
        System.out.println("Comparison result: " + compareResult); // Output: Comparison result: 1
    }
}
