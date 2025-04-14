public class Main {
    public static void main(String[] args) {
        // Using a_plus_b method for integer addition
        System.out.println(Test.a_plus_b(2, 3)); // Output: 5

        // Using a_plus_b method for custom object comparison
        int result = Test.a_plus_b(obj -> ((String) obj).length(), "apple", "banana");
        System.out.println(result); // Output: -1 (because "apple" is shorter than "banana")
    }
}
