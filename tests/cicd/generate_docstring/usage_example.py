import java.util.function.Function;

class Example {
    public static void main(String[] args) {
        // Example usage of a_plus_b with two numbers
        int sum = Test.a_plus_b(5, 10);
        System.out.println("The sum is: " + sum);
        
        // Example usage of a_plus_b with a keymap function
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        int compareResult = Test.a_plus_b(keymap, 5, 10);
        System.out.println("Comparison result is: " + compareResult);
    }
}
