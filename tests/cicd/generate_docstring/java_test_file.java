class Test {
    /**
     * Calculates the sum of two Integer numbers.
     * 
     * @param a The first Integer to be added.
     * @param b The second Integer to be added.
     * @return The sum of the two Integer parameters as an int.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a key mapping function and returns an integer indicating the order.
     * 
     * @param keymap A function that takes an object and returns a comparable value for comparison.
     * @param a      The first object to be compared.
     * @param b      The second object to be compared.
     * @return       -1 if the first object's key is less than the second's, 1 if greater, or 0 if equal.
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