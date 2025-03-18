import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestClass {

    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
    }

    @Test
    public void testAPlusBWithKeymap() {
        assertEquals(-1, Test.a_plus_b(Object::hashCode, "a", "b"));
        assertEquals(1, Test.a_plus_b(Object::hashCode, "b", "a"));
        assertEquals(0, Test.a_plus_b(Object::hashCode, "a", "a"));
    }
}
