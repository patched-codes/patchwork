class Test {
    /**
     * Adds two Integer values and returns their sum.
     * 
     * @param a The first Integer to be added
     * @param b The second Integer to be added
     * @return The sum of the two Integer values
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects `a` and `b` by applying a key mapping function to them.
     * The resulting comparable keys are then compared to determine the order of `a` and `b`.
     * 
     * @param keymap A function that takes an Object and returns a Comparable. The key to compare.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the key of `a` is less than the key of `b`, 1 if the key of `a` is greater than the key of `b`, 
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