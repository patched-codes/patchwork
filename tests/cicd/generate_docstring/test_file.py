import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
    }

    @Test
    void testAPlusBWithKeymap() {
        Function<Object, Comparable> keymap = obj -> (int) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 2, 3));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 3, 3));
    }
}
