class Test {
    /**
     * Computes the sum of two Integer objects.
     * 
     * @param a The first integer to be added.
     * @param b The second integer to be added.
     * @return The sum of 'a' and 'b' as an integer.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects a and b using a specified key mapping function.
     * The function applies the keymap to both objects and compares the resulting Comparable values.
     * 
     * @param keymap a function that takes an object and returns a Comparable value for comparison
     * @param a the first object to be compared
     * @param b the second object to be compared
     * @return -1 if the Comparable value of a is less than that of b, 1 if it is greater, and 0 if they are equal
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