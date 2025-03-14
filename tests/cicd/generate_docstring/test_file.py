import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusB_Integer() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(0, 0));
        assertEquals(-1, Test.a_plus_b(-1, 0));
    }

    @Test
    void testAPlusB_Function() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
