import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

public class TestTest {
    
    @Test
    void testAPlusB_Integer() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-3, Test.a_plus_b(-5, 2));
    }

    @Test
    void testAPlusB_withFunction() {
        Function<Object, Integer> keymap = o -> (Integer) o;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 1));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
