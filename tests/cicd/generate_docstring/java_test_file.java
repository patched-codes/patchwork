class Test {
    /**
     * Adds two Integer numbers and returns the result.
     * 
     * @param a The first Integer number to be added.
     * @param b The second Integer number to be added.
     * @return The sum of the two Integer numbers.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects 'a' and 'b' based on a key mapping function and returns
     * an integer indicating their order relative to one another.
     * 
     * @param keymap A function that takes an Object and returns a Comparable, 
     *               which is used to perform the comparison between 'a' and 'b'.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the key mapped value of 'a' is less than that of 'b', 
     *         1 if it is greater, 
     *         0 if both are equal.
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