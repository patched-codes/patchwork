import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestTest {
    
    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(0, 0));
        assertEquals(-3, Test.a_plus_b(-1, -2));
    }

    @Test
    public void testAPlusBKeymap() {
        Function<Object, Comparable> keymap = obj -> (Integer)obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 2, 1));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
