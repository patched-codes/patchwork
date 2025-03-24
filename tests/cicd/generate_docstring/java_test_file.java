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
     * Compares two objects based on a key mapping function.
     *
     * The method applies the provided key mapping function to both objects and then compares the results.
     * It returns -1 if the key of the first object is less than the key of the second object, 
     * 1 if it is greater, and 0 if they are equal.
     *
     * @param keymap A function that extracts a comparable key from an object.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return -1 if 'a' is less than 'b'; 1 if 'a' is greater than 'b'; 0 if they are equal.
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