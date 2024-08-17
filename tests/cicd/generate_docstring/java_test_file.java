class Test {
    /**
    * Adds two integers and returns the sum.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using the provided keymap function.
    * 
    * @param keymap Function that maps objects to comparable values
    * @param a First object to be compared
    * @param b Second object to be compared
    * @return -1 if a is less than b, 1 if a is greater than b, 0 if a is equal to b
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