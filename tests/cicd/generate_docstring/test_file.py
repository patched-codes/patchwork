import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestTest {

    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    public void testAPlusBWithKeymap() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 4, 4));
    }
}
