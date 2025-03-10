class Test {
    /**
     * Calculates the sum of two integers.
     * 
     * @param a First integer value to be added.
     * @param b Second integer value to be added.
     * @return The sum of the two integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects by applying a given key-mapping function to extract comparable values.
     * Returns -1 if the key of the first object is less than the key of the second object,
     * returns 1 if greater, and returns 0 if they are equal.
     * 
     * @param keymap A function which maps an object to a comparable key.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return An integer -1, 0, or 1 as described above.
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