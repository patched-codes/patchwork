class Test {
    /**
     * Adds two integers and returns the result.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers.
     */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a key mapping function and returns an integer 
     * to indicate their relative ordering. 
     * 
     * The method applies the given keymap function to both objects and compares 
     * the resulting Comparable objects. It returns:
     * -1 if the first object is considered less than the second,
     *  1 if the first is greater, 
     *  0 if both are considered equal.
     * 
     * @param keymap A function that maps an object to a Comparable value used for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return An integer indicating the relative ordering: -1 if 'a' is less than 'b', 1 if greater, and 0 if equal.
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