class Test {
    /**
     * Adds two integers and returns the sum.
     * 
     * @param a First integer to be added.
     * @param b Second integer to be added.
     * @return The sum of the two integers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects a and b using a key mapping function and returns an integer based on their comparison.
     * 
     * @param keymap A function that maps an Object to a Comparable for comparison purposes.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the key of a is less than the key of b, 
     *          1 if the key of a is greater than the key of b, 
     *          0 if they are equal.
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