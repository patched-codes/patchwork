class Test {
    /**
     * Adds two Integer numbers and returns the sum.
     * 
     * @param a First Integer to be added
     * @param b Second Integer to be added
     * @return The sum of the two Integer numbers
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects a and b using a specified key mapping function.
     * 
     * @param keymap A function that takes an Object and returns a Comparable used for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if keymap(a) is less than keymap(b), 1 if keymap(a) is greater than keymap(b), 
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