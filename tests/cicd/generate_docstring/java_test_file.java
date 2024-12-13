class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a An integer value to be added.
     * @param b Another integer value to be added.
     * @return The sum of the two integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects, `a` and `b`, using a provided `keymap` function that extracts
     * a comparable key from each object. Returns -1, 0, or 1 if the key of `a` is less than,
     * equal to, or greater than the key of `b`, respectively.
     * 
     * @param keymap A function that maps an object to a comparable key.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return An integer representing the comparison result: -1 if `a` is less than `b`,
     *         1 if `a` is greater than `b`, and 0 if they are equal.
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