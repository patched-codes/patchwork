class Test {
    /**
    * Adds two integers together.
    * 
    * @param a the first integer
    * @param b the second integer
    * @return the sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects based on the key mapping function provided.
    * 
    * @param keymap A function to extract a comparable key from the objects.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if keymap(a) is less than keymap(b), 1 if keymap(a) is greater than keymap(b), 0 if they are equal.
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