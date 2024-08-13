class Test {
    /**
    * Calculates the sum of two Integers.
    * 
    * @param a the first Integer
    * @param b the second Integer
    * @return the sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mapping function provided.
    * 
    * @param keymap Function that maps an object to a comparable key
    * @param a First object to compare
    * @param b Second object to compare
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