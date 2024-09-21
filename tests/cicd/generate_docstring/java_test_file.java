class Test {
    /**
    * Computes the sum of two integers.
    * 
    * @param a The first integer to be added.
    * @param b The second integer to be added.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects, a and b, based on their mapped keys obtained through the provided keymap function.
    * 
    * @param keymap Function that maps an object to a Comparable key.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if the key of `a` is less than the key of `b`, 1 if the key of `a` is greater than the key of `b`, otherwise 0.
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