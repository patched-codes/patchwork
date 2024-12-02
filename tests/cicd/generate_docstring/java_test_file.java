class Test {
    /**
     * Adds two Integer numbers.
     * 
     * @param a The first Integer to be added.
     * @param b The second Integer to be added.
     * @return The sum of a and b as an Integer.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects `a` and `b` using a keymapper function that maps each object to a comparable key.
     * 
     * @param keymap A function that takes an object and returns a comparable key, used for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return An integer representing the result of the comparison: 
     *         -1 if the key for `a` is less than the key for `b`,
     *          1 if the key for `a` is greater than the key for `b`,
     *          0 if the keys for both objects are equal.
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