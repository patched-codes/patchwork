import java.util.function.Function;

public class Example {
    public static void main(String[] args) {
        // Example usage of a_plus_b method for integers
        int sum = Test.a_plus_b(5, 3);
        System.out.println("Sum: " + sum); // Output: Sum: 8

        // Example usage of a_plus_b method with keymap function
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        int comparison = Test.a_plus_b(keymap, 5, 3);
        System.out.println("Comparison: " + comparison); // Output: Comparison: 1
    }
}
