import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusB_Integer() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    void testAPlusB_Comparison() {
        Function<Object, Integer> keymap = obj -> ((String) obj).length();
        assertEquals(-1, Test.a_plus_b(keymap, "a", "abc"));
        assertEquals(1, Test.a_plus_b(keymap, "abcd", "abc"));
        assertEquals(0, Test.a_plus_b(keymap, "abc", "abc"));
    }
}
