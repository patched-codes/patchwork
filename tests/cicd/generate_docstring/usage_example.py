// Example usage for tests/cicd/generate_docstring/java_test_file.java

public class JavaTest {
    public static void main(String[] args) {
        // Example 1: Simple addition using integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example 2: Custom comparator using keymap function
        Function<Object, Comparable> keymap = object -> (Integer) object * 2;
        int comparison = Test.a_plus_b(keymap, 10, 20);
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
