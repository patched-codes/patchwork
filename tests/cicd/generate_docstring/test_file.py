import static org.junit.Assert.assertEquals;
import org.junit.Test;
import java.util.function.Function;

public class TestTest {
    
    @Test
    public void testAPlusB_Integers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    public void testAPlusB_Comparable() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 5, 2));
        assertEquals(0, Test.a_plus_b(keymap, 3, 3));
    }
}
