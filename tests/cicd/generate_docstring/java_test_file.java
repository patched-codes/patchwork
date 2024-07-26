class Test {
    /**
    * Adds two given Integers.
    * 
    * @param a The first Integer to be added
    * @param b The second Integer to be added
    * @return The sum of the two Integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the mapping of a key function.
    * 
    * @param keymap A function that maps objects to comparable values
    * @param a The first object to compare
    * @param b The second object to compare
    * @return -1 if keymap(a) is less than keymap(b), 1 if keymap(a) is greater than keymap(b), 0 if they are equal
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