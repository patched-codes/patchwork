class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to add.
     * @param b The second integer to add.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on a key mapping function and returns an integer according to the comparison of 
     * the keys produced by the keymap function.
     * 
     * @param keymap A function that maps an object to a Comparable key.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the key of a is less than the key of b, 1 if the key of a is greater than the key of b,
     *         or 0 if the keys are equal.
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