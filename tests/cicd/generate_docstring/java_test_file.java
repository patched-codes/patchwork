class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects by applying a keymap function and returns an integer based on their comparison.
     * 
     * @param keymap A function that takes an object and returns a comparable key used for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the keymap of a is less than the keymap of b, 1 if the keymap of a is greater than the keymap of b, 
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