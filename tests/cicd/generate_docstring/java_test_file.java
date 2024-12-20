class Test {
    /**
     * Sums two Integer values.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers as an int.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a key function and returns an integer based on their order.
     * 
     * @param keymap Function that maps an object to a Comparable key used for comparison
     * @param a First object to compare
     * @param b Second object to compare
     * @return -1 if the key of a is less than the key of b, 1 if the key of a is greater than the key of b, or 0 if they are equal
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