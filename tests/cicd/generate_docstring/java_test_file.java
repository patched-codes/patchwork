class Test {
    /**
    * Calculates the sum of two integers.
    * 
    * @param a The first integer
    * @param b The second integer
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mapping provided by the Function.
    * 
    * @param keymap The function to map the objects to Comparable values
    * @param a The first object to be compared
    * @param b The second object to be compared
    * @return -1 if the key mapping of 'a' is less than 'b', 1 if greater, and 0 if equal
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