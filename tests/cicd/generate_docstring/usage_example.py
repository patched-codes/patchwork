public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        int sum = Test.a_plus_b(10, 20);
        System.out.println("Sum of 10 and 20: " + sum);

        // Example usage of a_plus_b with keymap
        int compareResult = Test.a_plus_b(
            obj -> (Integer) obj,
            10,
            20
        );
        System.out.println("Comparison result of 10 and 20: " + compareResult);
    }
}
