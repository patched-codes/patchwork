class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be summed.
     * @param b The second integer to be summed.
     * @return The sum of the two integers a and b.
     */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a provided key mapping function and returns an integer value 
     * indicating the order.
     * 
     * @param keymap A function that maps an object to a comparable value for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return -1 if the comparable value of a is less than that of b, 1 if greater, 
     *         and 0 if they are equal.
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