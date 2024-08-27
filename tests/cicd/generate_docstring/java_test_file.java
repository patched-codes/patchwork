class Test {
    /**
    * Adds two integers and returns the sum.
    *
    * @param a The first integer to be added
    * @param b The second integer to be added
    * @return The sum of the two input integers
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a provided key mapping function.
    * 
    * @param keymap A function that maps objects to comparable values
    * @param a The first object to compare
    * @param b The second object to compare
    * @return -1 if a is less than b, 1 if a is greater than b, 0 if they are equal
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