import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-1, 0));
    }

    @Test
    void testAPlusBFunction() {
        java.util.function.Function<Object, Comparable> keymap = (Object o) -> ((String)o).length();
        assertEquals(-1, Test.a_plus_b(keymap, "abc", "abcd"));
        assertEquals(1, Test.a_plus_b(keymap, "abcd", "abc"));
        assertEquals(0, Test.a_plus_b(keymap, "abc", "def"));
    }
}

