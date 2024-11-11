import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusBComparator() {
        Function<Object, Comparable> keymap = x -> (Integer) x;

        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
    }
}
