class Test {
    /**
    * Adds two integer values.
    * 
    * @param a the first integer to add
    * @param b the second integer to add
    * @return the sum of the two integers
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on a provided key mapping function.
    * 
    * @param keymap A function that maps an object to a comparable key.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if the key of 'a' is less than the key of 'b', 1 if the key of 'a' is greater than the key of 'b', and 0 if the keys are equal.
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