class Test {
    /**
     * Adds two integers together.
     *
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects `a` and `b` based on their mapped values from the provided keymap function.
     * Returns -1, 0, or 1 if the mapped value of `a` is less than, equal to, or greater than the 
     * mapped value of `b`, respectively.
     * 
     * @param keymap Function that maps an Object to a Comparable value for comparison.
     * @param a First object to be compared.
     * @param b Second object to be compared.
     * @return -1 if the mapped value of `a` is less than `b`, 1 if greater, or 0 if equal.
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