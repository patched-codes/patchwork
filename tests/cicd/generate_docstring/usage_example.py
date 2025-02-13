public class Main {
    public static void main(String[] args) {
        // Adding two integers using a_plus_b
        int sum = Test.a_plus_b(5, 10);
        System.out.println("Sum: " + sum); // Output: Sum: 15

        // Comparing two strings based on their lengths
        int comparison = Test.a_plus_b(String::length, "apple", "banana");
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}
