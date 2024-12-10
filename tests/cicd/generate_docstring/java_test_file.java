class Test {
    /**
     * Computes the sum of two integer values.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on the provided key mapping function.
     * 
     * @param keymap A function that maps an object to a comparable key used for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return An integer -1, 0, or 1 depending on whether the key of 'a' is less than, equal to, or greater than the key of 'b'.
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