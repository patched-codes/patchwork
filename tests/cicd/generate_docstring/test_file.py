import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestTest {
    @Test
    public void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    public void testAPlusBWithKeymap() {
        Function<Object, Integer> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 1));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
