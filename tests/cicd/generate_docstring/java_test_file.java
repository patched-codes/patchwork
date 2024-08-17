class Test {
    /**
    * Adds two integers together.
    * 
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of the two integers
    */
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares the values of two objects using the provided key mapping function.
    * 
    * @param keymap The function used to extract comparable keys from objects
    * @param a The first object to be compared
    * @param b The second object to be compared
    * @return -1 if keymap(a) &lt; keymap(b), 1 if keymap(a) &gt; keymap(b), 0 if keymap(a) = keymap(b)
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