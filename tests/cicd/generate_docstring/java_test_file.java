class Test {
    /**
     * Calculates the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects `a` and `b` by applying a key-mapping function and returns an integer indicating their comparison result.
     * 
     * @param keymap A function that takes an Object and returns a Comparable object to be used for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return An integer: -1 if `a` is less than `b`, 1 if `a` is greater than `b`, and 0 if they are equal according to the key-mapped values.
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