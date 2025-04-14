import org.junit.jupiter.api.Test;
import java.util.function.Function;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestJava {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(0, 0));
        assertEquals(-2, Test.a_plus_b(-1, -1));
    }

    @Test
    void testAPlusBKeymap() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 3));
        assertEquals(1, Test.a_plus_b(keymap, 5, 2));
        assertEquals(0, Test.a_plus_b(keymap, 4, 4));
    }
}
