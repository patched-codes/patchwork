class Test {
    /**
    * Adds two Integer values.
    * 
    * @param a the first Integer to be added
    * @param b the second Integer to be added
    * @return the sum of the two Integer values
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects a and b using the provided key mapping function.
    * 
    * @param keymap A function that maps an object to a comparable value.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if the keymap of a is less than the keymap of b, 1 if greater, or 0 if they are equal.
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