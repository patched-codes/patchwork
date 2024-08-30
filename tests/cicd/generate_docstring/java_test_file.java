class Test {
    /**
    * Adds two integers together.
    * 
    * @param a First integer to be added.
    * @param b Second integer to be added.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects based on a specified key mapping function.
     * 
     * @param keymap A function that extracts a comparable key from an object.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the key of 'a' is less than the key of 'b', 1 if the key of 'a' is greater than the key of 'b', and 0 if the keys are equal.
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