class Test {
    /**
    * Sum of two integers.
    * 
    * @param a First integer to add
    * @param b Second integer to add
    * @return Sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' based on their mapping values using the provided keymap function.
    * Returns -1 if the mapping value of 'a' is less than that of 'b', 
    * 1 if 'a' is greater than 'b', or 0 if they are equal.
    * 
    * @param keymap A function that maps objects to comparable values.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if a < b, 1 if a > b, 0 if a = b.
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