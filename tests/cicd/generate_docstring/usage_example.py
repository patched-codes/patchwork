// Example usage of Test class in Java
public class Main {
    public static void main(String[] args) {
        // Using a_plus_b with integers
        int result1 = Test.a_plus_b(5, 10);
        System.out.println("Result1: " + result1); // Output: Result1: 15

        // Using a_plus_b with custom comparator
        int compareResult = Test.a_plus_b(o -> ((String) o).length(), "apple", "banana");
        System.out.println("CompareResult: " + compareResult); // Output: CompareResult: -1
    }
}
