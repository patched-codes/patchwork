import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusBInteger() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(0, 0));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusBFunctionObjectObject() {
        Function<Object, Comparable> keymap = o -> (Comparable) o;
        
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 2, 1));
        assertEquals(0, Test.a_plus_b(keymap, 1, 1));
    }
}
