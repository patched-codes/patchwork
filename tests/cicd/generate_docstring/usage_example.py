public class Main {
    public static void main(String[] args) {
        // Demonstrate a_plus_b with two integers
        int result = Test.a_plus_b(3, 4);
        System.out.println("Sum: " + result);

        // Demonstrate a_plus_b with a key map function
        int comparison = Test.a_plus_b(o -> (Integer) o, 10, 20);
        System.out.println("Comparison result: " + comparison);
    }
}
