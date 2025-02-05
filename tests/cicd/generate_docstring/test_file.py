import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestUtils {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    void testAPlusBComparison() {
        Function<Object, Comparable> keyMap = o -> (Integer) o;
        assertEquals(-1, Test.a_plus_b(keyMap, 1, 2));
        assertEquals(0, Test.a_plus_b(keyMap, 2, 2));
        assertEquals(1, Test.a_plus_b(keyMap, 3, 2));
    }
}
