class Test {
    /**
    * Returns the sum of two integers.
    * 
    * @param a The first integer for addition
    * @param b The second integer for addition
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on a key mapping function.
    * 
    * @param keymap The key mapping function to extract comparable keys from objects.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if the key mapped from a is less than the key mapped from b, 1 if greater, 0 if equal.
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