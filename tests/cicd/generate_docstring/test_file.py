import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestClass {

    @Test
    void testAPlusBInteger() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertNotEquals(4, Test.a_plus_b(2, 3));
    }

    @Test
    void testAPlusBFunction() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
    }
}
