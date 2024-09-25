class Test {
    /**
    * Computes the sum of two integers.
    * 
    * @param a The first integer.
    * @param b The second integer.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects a and b using a key mapping function and returns an integer based on their order.
    * 
    * @param keymap A function that maps an object to a comparable key.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if the key of a is less than the key of b, 1 if the key of a is greater than the key of b, and 0 if they are equal.
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