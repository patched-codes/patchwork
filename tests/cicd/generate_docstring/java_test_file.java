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
     * Compares two objects based on a provided key-mapping function and returns an integer 
     * indicating their relative order.
     * 
     * @param keymap A function that takes an object and returns a comparable key for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return Returns -1 if the key of object 'a' is less than the key of object 'b', 
     *         1 if the key of object 'a' is greater than the key of object 'b', 
     *         and 0 if both keys are equal.
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
