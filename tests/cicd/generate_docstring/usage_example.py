public class UsageExample {
    public static void main(String[] args) {
        // Example 1: Simple addition using a_plus_b
        int result1 = Test.a_plus_b(5, 3);
        System.out.println("Sum: " + result1);  // Output: Sum: 8

        // Example 2: Comparing integers using a custom keymap
        Function<Integer, Integer> keyMap = (Integer x) -> x % 10;
        int compareResult = Test.a_plus_b(keyMap, 23, 37);
        System.out.println("Comparison: " + compareResult);  // Output: Comparison: -1
    }
}
