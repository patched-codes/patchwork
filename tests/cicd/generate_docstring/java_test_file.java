class Test {
    /**
    * Adds two Integer values and returns the result.
    * 
    * @param a The first integer to add.
    * @param b The second integer to add.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a key mapping function and determines their order based on the mapped values.
    * 
    * @param keymap A function that takes an Object and returns a Comparable used for comparison.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return Returns -1 if the key mapping of 'a' is less than the key mapping of 'b', 1 if greater, and 0 if they are equal.
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