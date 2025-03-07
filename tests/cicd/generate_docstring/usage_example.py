public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b method
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum of 5 and 10 is: " + sum);

        // Example usage of overloaded a_plus_b method using a keymap for comparison
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        int comparisonResult = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison result of 5 and 10 is: " + comparisonResult);
    }
}
