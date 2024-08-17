class Test {
    /**
    * Adds two Integer numbers.
    * 
    * @param a The first Integer number to be added.
    * @param b The second Integer number to be added.
    * @return The sum of the two Integer numbers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using the provided key mapping function.
    * 
    * @param keymap The function used for mapping objects to comparable values
    * @param a The first object to compare
    * @param b The second object to compare
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