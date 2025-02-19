class TestExample {
    public static void main(String[] args) {
        // Using a_plus_b with integers
        int sum = Test.a_plus_b(5, 3);
        System.out.println("Sum: " + sum); // Output: Sum: 8

        // Comparing with keymap function
        int comparison = Test.a_plus_b(
            obj -> ((MyClass) obj).value,
            new MyClass(2),
            new MyClass(5)
        );
        System.out.println("Comparison: " + comparison); // Output: Comparison: -1
    }
}

class MyClass {
    int value;

    MyClass(int value) {
        this.value = value;
    }
}
