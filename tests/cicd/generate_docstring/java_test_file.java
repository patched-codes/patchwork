class Test {
    /**
    * Adds two Integer values.
    * 
    * @param a The first Integer value to be added.
    * @param b The second Integer value to be added.
    * @return The sum of the two Integer values.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on a key mapping function and returns an integer indicating their order.
    * 
    * @param keymap A mapping function that takes an object and returns a Comparable key used for comparison.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if the key of `a` is less than the key of `b`; 1 if the key of `a` is greater than the key of `b`; 0 if the keys are equal.
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