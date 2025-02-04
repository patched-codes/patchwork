public class Main {
    public static void main(String[] args) {
        // Example of adding two numbers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example of comparing two objects using keymap function
        Function<Object, Comparable> keyMap = item -> ((String) item).length();
        int comparisonResult = Test.a_plus_b(keyMap, "apple", "banana");
        System.out.println("Comparison Result: " + comparisonResult); // Output: -1
    }
}
