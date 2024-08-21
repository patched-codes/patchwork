class Test {
    /**
    * This method calculates the sum of two Integer values.
    * 
    * @param a The first Integer value
    * @param b The second Integer value
    * @return The sum of a and b as an integer
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using the given key mapping function.
    * 
    * @param keymap The function used to extract a comparable key from objects.
    * @param a Object a to be compared.
    * @param b Object b to be compared.
    * @return -1 if keymap(a) is less than keymap(b), 1 if keymap(a) is greater than keymap(b), 0 if they are equal.
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