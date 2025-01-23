public class Main {
    public static void main(String[] args) {
        // Example of a_plus_b method that adds two integers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Example of keymap comparison with a lambda function
        Function<Object, Integer> keyMap = obj -> (Integer) obj;
        int comparison = Test.a_plus_b(keyMap, 3, 5);
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
