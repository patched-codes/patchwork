class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to add.
     * @param b The second integer to add.
     * @return The sum of the two integers a and b.
     */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on a key generated from a key mapping function.
     * 
     * This method applies the provided keymap function to both objects `a` and `b`,
     * and compares the resulting keys. It returns -1 if the key for `a` is less
     * than the key for `b`, 1 if it is greater, and 0 if they are equal.
     * 
     * @param keymap Function<Object, Comparable> a function that takes an object 
     *               and returns a Comparable key used for comparison
     * @param a Object the first object to be compared
     * @param b Object the second object to be compared
     * @return int -1 if the key for `a` is less than the key for `b`, 1 if greater, 0 if equal
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