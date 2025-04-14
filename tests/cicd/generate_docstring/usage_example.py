import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example of a_plus_b with integers
        int result = Test.a_plus_b(5, 7);
        System.out.println("Sum: " + result); // Output: Sum: 12

        // Example of a_plus_b with keymap functionality
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        int comparison = Test.a_plus_b(keymap, 3, 8);
        System.out.println("Comparison result: " + comparison); // Output: -1
    }
}
