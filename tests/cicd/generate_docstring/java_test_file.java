class Test {
    /**
     * Adds two integer numbers.
     * 
     * @param a The first integer number to be added.
     * @param b The second integer number to be added.
     * @return The sum of the two integer numbers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a keymap function and returns an integer based on their relative order.
     * 
     * @param keymap A function that maps an object to a comparable type for comparison.
     * @param a The first object to compare.
     * @param b The second object to compare.
     * @return Returns -1 if the first object is less than the second object, 1 if it is greater, and 0 if they are equal according to the keymap function.
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