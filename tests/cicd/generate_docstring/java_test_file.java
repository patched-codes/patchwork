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
    * Compares two objects using the provided key mapping function.
    * 
    * @param keymap Function to map objects to comparable values
    * @param a First object to compare
    * @param b Second object to compare
    * @return -1 if a < b, 1 if a > b, 0 if a == b
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