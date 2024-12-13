class Test {
    /**
     * Calculates the sum of two integers.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of the integers a and b.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects using a specified keymap function.
     * 
     * This method applies the keymap function to both objects 'a' and 'b',
     * and compares the resulting Comparable values. It returns -1 if the key
     * of 'a' is less than the key of 'b', 1 if the key of 'a' is greater, and 0 if they are equal.
     * 
     * @param keymap a function that extracts a Comparable key from an object
     * @param a the first object to compare
     * @param b the second object to compare
     * @return -1 if key of 'a' < key of 'b', 1 if key of 'a' > key of 'b', 0 if they are equal
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