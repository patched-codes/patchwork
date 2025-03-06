import java.util.function.Function;

class Test {
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    public static int a_plus_b(Function<Object, Comparable> keymap, Object a, Object b) {
        if (keymap.apply(a) < keymap.apply(b)) {
            return -1;
        } else if (keymap.apply(a) > keymap.apply(b)) {
            return 1;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(a_plus_b(5, 3)); // Output: 8

        // Example compare using custom key
        Function<Object, Integer> keymap = obj -> (int) obj; // Simple keymap
        System.out.println(a_plus_b(keymap, 5, 10)); // Output: -1
    }
}
