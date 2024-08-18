class Test {
    /**
    * Calculate the sum of two integers.
    * 
    * @param a the first integer
    * @param b the second integer
    * @return the sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using the provided key mapping function.
    * 
    * @param keymap The function used to extract Comparable keys from the objects
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