class Test {
    /**
     * Computes the sum of two integers.
     * 
     * @param a The first integer value to be added.
     * @param b The second integer value to be added.
     * @return The sum of the two integer values a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a key mapping function to extract Comparable keys.
     * 
     * @param keymap Function to map objects a and b to Comparable keys.
     * @param a First object for comparison.
     * @param b Second object for comparison.
     * @return  -1 if the key of object a is less than the key of object b, 
     *           1 if the key of object a is greater than the key of object b,
     *           0 if both keys are equal.
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