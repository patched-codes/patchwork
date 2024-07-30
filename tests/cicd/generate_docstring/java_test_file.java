class Test {
    /**
    * Returns the sum of two integers.
    * 
    * @param a The first integer
    * @param b The second integer
    * @return The sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares the mapping of two objects using the given key mapping function.
    * 
    * @param keymap The function used to map objects to comparable values
    * @param a The first object to compare
    * @param b The second object to compare
    * @return -1 if the key mapping of a is less than b, 1 if greater, 0 if equal
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