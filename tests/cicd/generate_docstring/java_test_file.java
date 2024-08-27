class Test {
    /**
    * Adds two integers.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The result of adding the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a key mapping function and returns -1, 0, or 1 based on the comparison result.
    * 
    * @param keymap The function used to map objects to Comparable values
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