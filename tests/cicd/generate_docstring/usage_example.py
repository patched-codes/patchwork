import java.util.function.Function;

public class Example {
    public static void main(String[] args) {
        // Demonstration of a_plus_b with two integers
        int sum = Test.a_plus_b(5, 3);
        System.out.println("Sum of 5 and 3: " + sum); // Outputs: Sum of 5 and 3: 8

        // Demonstration of a_plus_b with key mapping and comparison
        Function<Object, Comparable> keymap = obj -> ((String)obj).length();
        int comparison = Test.a_plus_b(keymap, "apple", "banana");
        System.out.println("Comparison result: " + comparison); // Outputs: -1, 0, or 1 based on length
    }
}
