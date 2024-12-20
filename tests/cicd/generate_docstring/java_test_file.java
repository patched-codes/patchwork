class Test {
    /**
     * Computes the sum of two integer values.
     * 
     * @param a The first integer value.
     * @param b The second integer value.
     * @return The sum of the two integer values a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a provided key mapping function and returns an integer
     * based on the comparison result.
     * 
     * @param keymap A function that takes an object and returns a comparable for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return -1 if the key of a is less than the key of b, 1 if the key of a is greater than
     *         the key of b, and 0 if the keys are equal.
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