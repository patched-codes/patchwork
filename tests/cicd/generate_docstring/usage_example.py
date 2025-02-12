// Import Function interface for key mapping
import java.util.function.Function;

class Test {
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    public static int a_plus_b(Function<Object, Comparable> keymap, Object a, Object b) {
        if (keymap.apply(a).compareTo(keymap.apply(b)) < 0) {
            return -1;
        } else if (keymap.apply(a).compareTo(keymap.apply(b)) > 0) {
            return 1;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        int sum = a_plus_b(3, 4);
        System.out.println("Sum: " + sum); // Output: Sum: 7

        // Example usage of a_plus_b with key mapping
        Function<Object, Comparable> keymap = obj -> (Integer) obj; // simple keymap function
        int result = a_plus_b(keymap, 10, 20);
        System.out.println("Compare result: " + result); // Output: Compare result: -1
    }
}
