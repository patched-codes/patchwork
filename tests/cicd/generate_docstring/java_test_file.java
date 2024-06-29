class Test {
    /**
    * Adds two integers together.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' based on the result of applying the keymapping function.
    * 
    * @param keymap Function that maps an object to a Comparable value.
    * @param a First object to compare.
    * @param b Second object to compare.
    * @return -1 if the keymap(a) result is less than keymap(b), 1 if greater, 0 if equal.
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