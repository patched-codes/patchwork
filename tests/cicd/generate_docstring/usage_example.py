import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        // Example usage of a_plus_b with integers
        System.out.println("Sum of 5 and 3: " + Test.a_plus_b(5, 3));

        // Example usage of a_plus_b with keymap functionality
        Function<Object, Comparable> lengthKeyMap = obj -> ((String)obj).length();
        String str1 = "apple";
        String str2 = "banana";
        System.out.println("Comparison of 'apple' and 'banana': " + Test.a_plus_b(lengthKeyMap, str1, str2));
    }
}

class Test {
    public static int a_plus_b(Integer a, Integer b) {
        return a + b;
    }

    public static int a_plus_b(Function<Object, Comparable> keymap, Object a, Object b) {
        if (keymap.apply(a).compareTo(keymap.apply(b)) < 0) {
            return -1;
        } else if (keymap.apply(a).compareTo(keymap.apply(b)) > 0) {
            return 1;
        } else {
            return 0;
        }
    }
}
