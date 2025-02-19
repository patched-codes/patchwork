class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the two integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a provided key mapping function and returns an integer 
     * indicating the relationship between the two objects' mapped values.
     * 
     * @param keymap A function that takes an object and returns a comparable value used for comparison.
     * @param a The first object to be compared.
     * @param b The second object to be compared.
     * @return -1 if the mapped value of 'a' is less than the mapped value of 'b';
     *         1 if the mapped value of 'a' is greater than the mapped value of 'b';
     *         0 if both mapped values are equal.
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