class Test {
    /**
     * Adds two integers together.
     * 
     * @param a The first integer to add.
     * @param b The second integer to add.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on their mapped comparable keys through a given key function.
     * 
     * @param keymap A function that maps an object to a comparable key for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return Returns -1 if the key of a is less than the key of b, 1 if the key of a is greater 
     *         than the key of b, and 0 if both keys are equal.
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