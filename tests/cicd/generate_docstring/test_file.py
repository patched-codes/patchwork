import static org.junit.Assert.assertEquals;
import java.util.function.Function;
import org.junit.Test;

public class TestTest {

    @Test
    public void testAPlusBIntegers() {
        int result = Test.a_plus_b(3, 4);
        assertEquals(7, result);
    }

    @Test
    public void testAPlusBFunction() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        int result = Test.a_plus_b(keymap, 3, 4);
        assertEquals(-1, result);

        result = Test.a_plus_b(keymap, 4, 3);
        assertEquals(1, result);

        result = Test.a_plus_b(keymap, 3, 3);
        assertEquals(0, result);
    }
}
