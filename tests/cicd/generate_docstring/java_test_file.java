class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two input integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on their mapped comparable values.
     * It uses a specified key mapping function to transform both objects into Comparable values and determines their order.
     * 
     * @param keymap Function that maps an object to a Comparable value for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the mapped value of 'a' is less than 'b', 1 if it is greater, and 0 if they are equal.
     */
    public static int a_plus_b(Function<Object, Comparable> keymap, object a, Object b) {
        if (keymap(a) < keymap(b)) {
            return -1;
        } else if (keymap(a) > keymap(b)) {
            return 1;
        } else {
            return 0;
        }
    }
}