class Test {
    /**
    * Adds two Integers and returns the result.
    * 
    * @param a The first Integer to be added
    * @param b The second Integer to be added
    * @return The sum of the two input Integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' based on the result of applying the 'keymap' function to them.
    * 
    * @param keymap A function that maps objects to comparable values
    * @param a The first object to be compared
    * @param b The second object to be compared
    * @return -1 if keymap(a) < keymap(b), 1 if keymap(a) > keymap(b), 0 if keymap(a) equals keymap(b)
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