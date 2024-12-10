import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJava {

    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
        assertEquals(-5, Test.a_plus_b(-2, -3));
    }

    @Test
    public void testAPlusBWithKeymap() {
        assertEquals(0, Test.a_plus_b(Object::hashCode, "a", "a"));
        assertEquals(-1, Test.a_plus_b(o -> ((String) o).length(), "a", "ab"));
        assertEquals(1, Test.a_plus_b(o -> ((String) o).length(), "ab", "a"));
    }
}
