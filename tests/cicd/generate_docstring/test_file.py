import org.junit.jupiter.api.Test;
import java.util.function.Function;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusBInteger() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
    }

    @Test
    void testAPlusBFunction() {
        Function<Object, Comparable> keymap = obj -> (int) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 3, 3));
    }
}
