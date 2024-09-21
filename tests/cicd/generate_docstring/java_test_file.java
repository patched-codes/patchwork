class Test {
    /**
    * Computes the sum of two Integer values.
    * 
    * @param a the first integer to be added
    * @param b the second integer to be added
    * @return the sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on a key extraction function and returns an integer
    * indicating their relative order.
    * 
    * @param keymap Function that extracts a Comparable key from an object
    * @param a The first object to be compared
    * @param b The second object to be compared
    * @return -1 if the key of 'a' is less than the key of 'b', 1 if the key of 'a' is greater than the key of 'b', 
    *         0 if both keys are equal
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