class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on the result of a key mapping function applied to each object. 
     * Returns -1 if `a` is less than `b`, 1 if `a` is greater than `b`, and 0 if they are equal
     * according to the mapped keys.
     * 
     * @param keymap Function to extract a comparable key from each object.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return an integer indicating the order: -1 for less than, 1 for greater than, and 0 for equal.
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