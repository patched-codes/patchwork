import org.junit.Test;
import java.util.function.Function;
import static org.junit.Assert.*;

public class TestTest {

    @Test
    public void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    public void testAPlusBWithKeyMap() {
        Function<Object, Comparable> keyMap = o -> ((String) o).length();
        assertEquals(1, Test.a_plus_b(keyMap, "short", "longer"));
        assertEquals(-1, Test.a_plus_b(keyMap, "longer", "short"));
        assertEquals(0, Test.a_plus_b(keyMap, "equal", "equal"));
    }
}
