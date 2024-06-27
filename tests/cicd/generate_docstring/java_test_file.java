class Test {
    /**
    * Adds two Integer numbers.
    * 
    * @param a The first Integer number to be added
    * @param b The second Integer number to be added
    * @return The sum of the two Integer numbers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mapping provided using the keymap function.
    * 
    * @param keymap Function that maps objects to comparable values
    * @param a First object to compare
    * @param b Second object to compare
    * @return -1 if a is less than b, 1 if a is greater than b, 0 if they are equal
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