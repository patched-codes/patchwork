class Test {
    /**
     * Adds two Integer objects together and returns the result as an int.
     * 
     * @param a The first Integer to be added.
     * @param b The second Integer to be added.
     * @return The sum of the two input Integer objects as an int.
     */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
     * Compares two objects after mapping them to a comparable form using the provided keymap function.
     * Returns -1, 0, or 1 if the first object is less than, equal to, or greater than the second, respectively,
     * according to the comparable mapping.
     * 
     * @param keymap A function that maps an Object to a Comparable form.
     * @param a The first Object to be compared.
     * @param b The second Object to be compared.
     * @return An integer (-1, 0, or 1) indicating the relative order of the two objects.
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