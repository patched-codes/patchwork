class Test {
    /**
    * Sums up two integers a and b.
    * 
    * @param a The first integer.
    * @param b The second integer.
    * @return The sum of a and b.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the keymapping function provided.
    * 
    * @param keymap The function used to map objects to comparable values
    * @param a The first object to compare
    * @param b The second object to compare
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