import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Simple addition
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Compare using custom keymap
        Function<Object, Integer> keymap = obj -> obj.hashCode();
        int comparisonResult = Test.a_plus_b(keymap, "apple", "banana");
        System.out.println("Comparison Result: " + comparisonResult); 
    }
}
