import static org.junit.Assert.assertEquals;

import org.junit.Test;
import java.util.function.Function;

public class TestTest {

    @Test
    public void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-1, 0));
        assertEquals(0, Test.a_plus_b(0, 0));
    }

    @Test
    public void testAPlusBWithKeymap() {
        Function<Object, Comparable> keymapLength = obj -> ((String) obj).length();

        assertEquals(-1, Test.a_plus_b(keymapLength, "apple", "banana"));
        assertEquals(1, Test.a_plus_b(keymapLength, "banana", "apple"));
        assertEquals(0, Test.a_plus_b(keymapLength, "apple", "grape"));
    }
}
