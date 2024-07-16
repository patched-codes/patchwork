class Test {
    /**
    * Sums up two integers.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of the two input integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mapping function provided.
    * 
    * @param keymap The function used to retrieve comparable keys from objects
    * @param a First object to compare
    * @param b Second object to compare
    * @return -1 if keymap(a) < keymap(b), 1 if keymap(a) > keymap(b), 0 if keymap(a) equals keymap(b)
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