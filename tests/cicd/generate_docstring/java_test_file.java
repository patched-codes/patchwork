class Test {
    /**
    * Computes the sum of two integers.
    * 
    * @param a First integer to be added.
    * @param b Second integer to be added.
    * @return The sum of integers a and b.
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a provided key mapping function and determines their order.
    * 
    * @param keymap A function that maps the objects to a comparable key for comparison.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if the key of the first object is less than the key of the second object,
    *         1 if the key of the first object is greater than the key of the second object,
    *         0 if the keys are equal.
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