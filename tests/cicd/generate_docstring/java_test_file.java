class Test {
    /**
    * Adds two integers.
    * 
    * @param a The first integer to be added.
    * @param b The second integer to be added.
    * @return The sum of the two integers.
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a key mapping function and returns an integer based on the comparison.
    * 
    * @param keymap A Function that converts an object to a Comparable for comparison.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if the key of the first object is less than the key of the second object, 1 if greater, or 0 if equal.
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