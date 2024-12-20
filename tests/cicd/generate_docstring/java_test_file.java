class Test {
    /**
     * Adds two integers and returns the result.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects after applying a key mapping function.
     * 
     * This method applies the provided key mapping function to two objects and returns a comparison result:
     * -1 if the first object maps to a value less than the second,
     *  1 if it maps to a value greater,
     *  0 if both are equal according to their mapped values.
     * 
     * @param keymap A function that accepts an object and returns a Comparable key used for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return An integer indicating the comparison result: -1 if a < b, 1 if a > b, or 0 if a == b.
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