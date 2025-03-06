import org.junit.jupiter.api.Test;
import java.util.function.Function;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
        assertEquals(-5, Test.a_plus_b(-2, -3));
    }

    @Test
    void testAPlusBWithKeymap() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
    }
}
