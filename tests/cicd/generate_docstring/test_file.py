import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {
    
    @Test
    void testAPlusB_Integer() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusB_Keymap() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
        assertEquals(-1, Test.a_plus_b(keymap, 2, 3));
        assertEquals(1, Test.a_plus_b(keymap, 5, 3));
    }

    @Test
    void testAPlusB_Exception() {
        assertThrows(ClassCastException.class, () -> {
            Test.a_plus_b((obj) -> (String) obj, "a", "b");
        });
    }
}
