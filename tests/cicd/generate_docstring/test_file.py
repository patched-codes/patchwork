import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import java.util.function.Function;
import org.junit.jupiter.api.Test;

class TestTest {

    @Test
    void testA_plus_bIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
        assertEquals(-5, Test.a_plus_b(-2, -3));
    }

    @Test
    void testA_plus_bFunction() {
        Function<Object, Comparable> keymap = o -> (Integer) o;

        assertEquals(-1, Test.a_plus_b(keymap, 2, 3));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }

    @Test
    void testA_plus_bInvalidInputs() {
        assertThrows(ClassCastException.class, () -> Test.a_plus_b(null, 3));
        assertThrows(NullPointerException.class, () -> Test.a_plus_b(o -> (Integer) o, null, 2));
    }
}
