import org.junit.Test;
import java.util.function.Function;
import static org.junit.Assert.assertEquals;

public class TestTest {

    @Test
    public void testAPlusBInt() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    public void testAPlusBFunctionObject() {
        Function<Object, Comparable> keymap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keymap, 1, 2));
        assertEquals(1, Test.a_plus_b(keymap, 3, 2));
        assertEquals(0, Test.a_plus_b(keymap, 2, 2));
    }
}
