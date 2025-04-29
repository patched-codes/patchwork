import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestUnit {
    
    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    void testAPlusBFunctionObjects() {
        Function<Object, Comparable> keymap = obj -> ((String) obj).length();
        assertEquals(-1, Test.a_plus_b(keymap, "a", "abc"));
        assertEquals(1, Test.a_plus_b(keymap, "abcd", "ab"));
        assertEquals(0, Test.a_plus_b(keymap, "ab", "cd"));
    }
}
