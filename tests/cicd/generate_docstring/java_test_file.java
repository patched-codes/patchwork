class Test {
    /**
    * Adds two integers together.
    * 
    * @param a The first integer value
    * @param b The second integer value
    * @return The sum of the two integers
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' using the provided keymap function.
    * 
    * @param keymap A function that maps objects to comparable values
    * @param a The first object to be compared
    * @param b The second object to be compared
    * @return -1 if 'a' is less than 'b', 1 if 'a' is greater than 'b', and 0 if they are equal
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