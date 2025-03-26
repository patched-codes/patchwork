import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

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

    @Test
    void testAPlusBInt() {
        assertEquals(5, a_plus_b(2, 3));
        assertEquals(-1, a_plus_b(-5, 4));
        assertEquals(0, a_plus_b(0, 0));
    }

    @Test
    void testAPlusBFunction() {
        Function<Object, Comparable> keymap = o -> o instanceof String ? ((String) o).length() : 0;
        assertEquals(0, a_plus_b(keymap, "abc", "def"));
        assertEquals(-1, a_plus_b(keymap, "abc", "defgh"));
        assertEquals(1, a_plus_b(keymap, "abcdef", "gh"));
    }
}
