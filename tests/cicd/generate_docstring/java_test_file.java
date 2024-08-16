class Test {
    /**
    * Calculates the sum of two numbers.
    * 
    * @param a The first number to be added
    * @param b The second number to be added
    * @return The sum of the two numbers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects 'a' and 'b' based on the sorting defined by the keymap function.
    * 
    * @param keymap A function that maps objects to comparable values for sorting.
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