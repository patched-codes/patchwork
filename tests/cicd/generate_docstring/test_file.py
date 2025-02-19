import static org.junit.Assert.*;
import org.junit.Test;

public class TestTest {

    @Test
    public void testAPlusB_integers() {
        int result = Test.a_plus_b(2, 3);
        assertEquals(5, result);
    }

    @Test
    public void testAPlusBWithFunction_firstSmaller() {
        Function<Object, Comparable> keymap = obj -> (Integer)obj;
        int result = Test.a_plus_b(keymap, 2, 3);
        assertEquals(-1, result);
    }

    @Test
    public void testAPlusBWithFunction_firstLarger() {
        Function<Object, Comparable> keymap = obj -> (Integer)obj;
        int result = Test.a_plus_b(keymap, 3, 2);
        assertEquals(1, result);
    }

    @Test
    public void testAPlusBWithFunction_equal() {
        Function<Object, Comparable> keymap = obj -> (Integer)obj;
        int result = Test.a_plus_b(keymap, 3, 3);
        assertEquals(0, result);
    }
}
