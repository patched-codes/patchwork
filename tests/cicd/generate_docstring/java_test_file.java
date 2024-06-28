class Test {
    /**
    * Calculates the sum of two integers.
    * 
    * @param a The first integer.
    * @param b The second integer.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a key mapping function.
    * 
    * @param keymap The function to extract a comparable key from the objects.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if the key from 'a' is less than the key from 'b', 1 if the key from 'a' is greater than the key from 'b', 0 if both keys are equal.
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