class Test {
    /**
    * Computes the sum of two integers.
    * 
    * @param a The first integer to be added.
    * @param b The second integer to be added.
    * @return The sum of the two integers.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects `a` and `b` based on the values obtained from a provided key mapping function `keymap`.
    * The `keymap` function is applied to both objects `a` and `b` to retrieve comparable values.
    * The method returns -1, 0, or 1 if the value of `a` is less than, equal to, or greater than the value of `b`, respectively.
    * 
    * @param keymap Function to map objects to comparable values.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return -1 if `keymap(a)` is less than `keymap(b)`, 1 if `keymap(a)` is greater than `keymap(b)`, and 0 if they are equal.
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