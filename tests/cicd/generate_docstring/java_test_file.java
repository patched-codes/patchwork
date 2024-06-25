class Test {
    /**
    * A method that takes two integers as parameters and returns the sum of them.
    * 
    * @param a The first integer input
    * @param b The second integer input
    * @return The sum of the two input integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the result of key mapping.
    * 
    * @param keymap Function that maps objects to comparable values
    * @param a Object to compare
    * @param b Object to compare
    * @return -1 if keymap(a) is less than keymap(b), 1 if keymap(a) is greater than keymap(b), 0 if keymap(a) equals keymap(b)
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