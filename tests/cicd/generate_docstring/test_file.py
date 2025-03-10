import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import java.util.function.Function;

class Test {
    
    @Test
    void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
        assertEquals(-3, Test.a_plus_b(-1, -2));
    }

    @Test
    void testAPlusBWithKeymap() {
        Function<Object, Comparable> keymap = (obj) -> (Comparable) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 2, 1));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
    
    @Test
    void testAPlusBWithKeymapNullValues() {
        Function<Object, Comparable> keymap = (obj) -> obj == null ? 0 : (Comparable) obj;
        assertEquals(0, Test.a_plus_b(keymap, null, null));
    }
}
