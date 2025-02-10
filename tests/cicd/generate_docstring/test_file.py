import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusB_Integers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-3, 3));
    }

    @Test
    void testAPlusB_Comparator() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 1));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
