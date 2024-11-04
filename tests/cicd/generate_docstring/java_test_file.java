class Test {
    /**
     * Adds two Integer values together and returns the result.
     * 
     * @param a The first Integer value to be added.
     * @param b The second Integer value to be added.
     * @return The sum of the two Integer values.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a specified key mapping function to determine their relative order.
     * 
     * @param keymap A function that maps an object to a comparable value for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return An integer indicating the order of the objects: -1 if a < b, 1 if a > b, and 0 if a == b.
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