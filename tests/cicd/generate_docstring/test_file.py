import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class TestTest {
    
    @Test
    public void testAPlusBInteger() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
    }

    @Test
    public void testAPlusBFunction() {
        Function<Object, Comparable> keymap = o -> (Integer) o;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
    }
}
