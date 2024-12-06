import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
        assertEquals(0, Test.a_plus_b(0, 0));
    }

    @Test
    void testAPlusBKeymap() {
        Function<Object, Comparable> keymap = obj -> ((String) obj).length();
        assertEquals(-1, Test.a_plus_b(keymap, "a", "abc"));
        assertEquals(1, Test.a_plus_b(keymap, "abcd", "abc"));
        assertEquals(0, Test.a_plus_b(keymap, "abc", "abc"));
    }
}
