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
    * Compares two objects using a key mapping provided as a function.
    * 
    * @param keymap The function used to map objects to comparable values.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if keymap(a) < keymap(b), 1 if keymap(a) > keymap(b), 0 if keymap(a) is equal to keymap(b).
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