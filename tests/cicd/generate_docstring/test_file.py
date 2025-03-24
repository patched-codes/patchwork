import static org.junit.Assert.assertEquals;
import java.util.function.Function;
import org.junit.Test;

public class TestTest {

    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(0, 0));
        assertEquals(-5, Test.a_plus_b(-2, -3));
    }
    
    @Test
    public void testAPlusBFunction() {
        Function<Object, Comparable> keyMap = obj -> (Integer) obj;
        assertEquals(-1, Test.a_plus_b(keyMap, 1, 2));
        assertEquals(1, Test.a_plus_b(keyMap, 2, 1));
        assertEquals(0, Test.a_plus_b(keyMap, 2, 2));
    }
}
