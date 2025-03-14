class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two provided integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects `a` and `b` using a key extractor function `keymap`.
     * The `keymap` is applied to both objects, and their results are compared as `Comparable`.
     * 
     * @param keymap A function that extracts a comparable key from the given objects.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the keymap result of `a` is less than that of `b`, 1 if it is greater,
     *         and 0 if they are equal.
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