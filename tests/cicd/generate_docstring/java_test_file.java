class Test {
    /**
     * Adds two integer values.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on a key mapping function and returns an integer indicating their order.
     * 
     * @param keymap A function that maps an object to a comparable key used for the comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return -1 if the key of the first object is less than the key of the second object,
     *         1 if the key of the first object is greater than the key of the second object, 
     *         and 0 if the keys are equal.
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