import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-3, 2));
    }

    @Test
    void testAPlusBFunctionObjects() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 2, 5));
        assertEquals(0, Test.a_plus_b(keymap, 5, 5));
        assertEquals(1, Test.a_plus_b(keymap, 7, 5));
    }
}
