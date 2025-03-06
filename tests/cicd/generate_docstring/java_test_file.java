class Test {
    /**
     * Adds two integers together and returns the result.
     * 
     * @param a The first integer to add.
     * @param b The second integer to add.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on their keys mapped by the provided keymap function.
     * Returns -1, 0, or 1 indicating whether the key of the first object is less than, equal to, or greater than the key of the second object, respectively.
     * 
     * @param keymap A function that maps an object to a comparable key.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return Integer indicating comparison result: -1 if key of 'a' is less than key of 'b', 1 if key of 'a' is greater than key of 'b', or 0 if keys are equal.
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