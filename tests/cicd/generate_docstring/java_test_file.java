class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a key mapping function and returns an integer indicating their relative order.
     * 
     * @param keymap A function that maps the objects to a comparable key for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return An integer: -1 if the key of `a` is less than the key of `b`, 1 if the key of `a` is greater than the key of `b`, and 0 if they are equal.
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