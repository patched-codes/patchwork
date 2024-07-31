class Test {
    /**
    * Takes two integers as input and returns their sum.
    * 
    * @param a The first integer
    * @param b The second integer
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the mapping provided by a keymap function.
    * 
    * @param keymap Function that maps objects to Comparable values
    * @param a Object to be compared
    * @param b Object to be compared
    * @return -1 if value of a in keymap is less than value of b, 1 if greater, 0 if equal
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