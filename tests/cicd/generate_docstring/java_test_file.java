class Test {
    /**
    * Computes the sum of two integers.
    * 
    * @param a The first integer
    * @param b The second integer
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mappings provided and returns -1, 0, or 1.
    * 
    * @param keymap A Function that maps an object to a comparable value
    * @param a The first object to compare
    * @param b The second object to compare
    * @return -1 if keymap(a) < keymap(b), 0 if keymap(a) == keymap(b), 1 if keymap(a) > keymap(b)
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