class Test {
    /**
    * This function adds two integers.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The integer sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the provided keymap function.
    * 
    * @param keymap Function that maps objects to Comparable values
    * @param a First object to compare
    * @param b Second object to compare
    * @return -1 if a < b, 1 if a > b, 0 if a equals b based on the keymap comparison
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