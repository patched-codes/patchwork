class Test {
    /**
    * Sums two integers.
    * 
    * @param a The first integer to be summed
    * @param b The second integer to be summed
    * @return The result of adding the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' using the provided key map function.
    * 
    * @param keymap A function that maps objects to comparable values.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if keymap(a) < keymap(b), 1 if keymap(a) > keymap(b), and 0 if keymap(a) equals keymap(b).
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