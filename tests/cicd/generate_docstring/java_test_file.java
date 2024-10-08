class Test {
    /**
    * Adds two Integer values together.
    * 
    * @param a The first Integer operand.
    * @param b The second Integer operand.
    * @return The sum of the two given Integer values.
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a given key mapping function,
    * returning a result that indicates which object is considered less,
    * greater or if both are equal.
    * 
    * @param keymap A function that maps the objects to a comparable key.
    * @param a The first object to be compared.
    * @param b The second object to be compared.
    * @return An integer value: -1 if the key for object 'a' is less than the key for object 'b', 
    *         1 if it is greater, or 0 if the keys are equal.
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