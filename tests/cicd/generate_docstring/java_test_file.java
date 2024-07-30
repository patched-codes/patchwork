class Test {
    /**
    * Adds two integers together.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of a and b
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares the keys of two objects using the provided keymap function.
    * 
    * @param keymap Function that maps objects to comparable keys
    * @param a Object A to compare
    * @param b Object B to compare
    * @return -1 if key(a) is less than key(b), 1 if key(a) is greater than key(b), 0 if keys are equal
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