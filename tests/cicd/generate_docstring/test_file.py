import org.junit.jupiter.api.Test;
import java.util.function.Function;
import static org.junit.jupiter.api.Assertions.*;

class TestTest {
    
    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
        assertEquals(-5, Test.a_plus_b(-3, -2));
    }

    @Test
    void testAPlusBFunction() {
        Function<Object, Comparable> keymap = x -> ((String)x).length();
        assertEquals(0, Test.a_plus_b(keymap, "same", "same"));
        assertEquals(1, Test.a_plus_b(keymap, "longer", "short"));
        assertEquals(-1, Test.a_plus_b(keymap, "short", "longer"));
    }
}
