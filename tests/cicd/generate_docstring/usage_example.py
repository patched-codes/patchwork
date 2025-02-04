// Example usage of the Java Test class

import java.util.function.Function;

class Main {
    public static void main(String[] args) {
        // Using a_plus_b with integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15
        
        // Using a_plus_b with a keymap
        Function<Object, Comparable> keymap = (Object o) -> ((String) o).length();
        int compareResult = Test.a_plus_b(keymap, "apple", "banana");
        System.out.println("Compare Result: " + compareResult); // Output: Compare Result: -1
    }
}
