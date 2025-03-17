import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.function.Function;
import org.junit.jupiter.api.Test;

public class TestTest {

    @Test
    void testAPlusB_Basic() {
        assertEquals(4, Test.a_plus_b(2, 2));
    }

    @Test
    void testAPlusB_CompareFunction() {
        Function<Object, Comparable> keymap = x -> (Integer) x;
        assertEquals(0, Test.a_plus_b(keymap, 3, 3));
        assertEquals(-1, Test.a_plus_b(keymap, 2, 5));
        assertEquals(1, Test.a_plus_b(keymap, 8, 3));
    }
}
