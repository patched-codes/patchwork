import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        int sum = Test.a_plus_b(3, 4);
        System.out.println("Sum: " + sum);

        // Example usage of a_plus_b method with a comparator function
        int comparison = Test.a_plus_b(Object::toString, "apple", "banana");
        System.out.println("Comparison: " + comparison);
    }
}
