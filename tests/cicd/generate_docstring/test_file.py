import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;
import java.util.function.Function;
import org.junit.jupiter.api.Test;

class TestTest {
    
    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusBWithKeyMap() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 3));
        assertEquals(1, Test.a_plus_b(keymap, 4, 2));
        assertEquals(0, Test.a_plus_b(keymap, 5, 5));
    }
}
