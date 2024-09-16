class Test {
    /**
    * Adds two Integer values and returns the result.
    * 
    * @param a the first integer value
    * @param b the second integer value
    * @return the sum of the two integer values
    */
    
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    /**
    * Compares two objects using a specified key-mapping function and returns an integer based on their comparison.
    * 
    * @param keymap A function that maps an object to a comparable value.
    * @param a The first object to compare.
    * @param b The second object to compare.
    * @return -1 if the comparable value of 'a' is less than 'b', 1 if it is greater than 'b', or 0 if they are equal.
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