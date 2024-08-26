class Test {
    /**
    * Computes the sum of two integers.
    *
    * @param a The first integer to be added.
    * @param b The second integer to be added.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects after applying a key mapping function to each.
    * 
    * @param keymap A function that maps an object to a comparable value.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return An integer representing the comparison result: 
    *         -1 if the first object is less than the second, 
    *         1 if the first object is greater than the second,
    *         0 if they are equal.
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