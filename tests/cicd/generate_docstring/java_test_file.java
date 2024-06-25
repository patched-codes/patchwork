class Test {
    /**
    * Takes two Integer values and returns their sum.
    * 
    * @param a the first Integer value
    * @param b the second Integer value
    * @return the sum of the two Integer values
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using the provided keymap function.
    * 
    * @param keymap A function that maps an object to a comparable value
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