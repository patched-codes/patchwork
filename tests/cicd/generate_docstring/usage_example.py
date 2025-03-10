import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example 1: Adding two integers
        System.out.println(Test.a_plus_b(5, 7)); // Output: 12

        // Example 2: Comparing two objects with key mapping
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        System.out.println(Test.a_plus_b(keymap, 3, 6)); // Output: -1
    }
}
