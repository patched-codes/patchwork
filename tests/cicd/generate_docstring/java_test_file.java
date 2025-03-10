class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a the first integer to be added
     * @param b the second integer to be added
     * @return the sum of the two integers
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a specified key mapping function and returns an integer
     * indicating the result of the comparison. The keymap function is applied to both 
     * objects to get their comparable keys, which are then compared.
     * 
     * @param keymap A function that extracts a Comparable key from an Object.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if object a is less than object b, 1 if object a is greater than object b,
     *         or 0 if they are equal.
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