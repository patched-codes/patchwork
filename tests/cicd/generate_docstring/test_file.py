import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestTest {
    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
    }

    @Test
    void testAPlusBKeymap() {
        assertEquals(-1, Test.a_plus_b(Object::hashCode, "a", "b"));
        assertEquals(0, Test.a_plus_b(String::length, "abc", "xyz"));
        assertEquals(1, Test.a_plus_b(String::length, "abcd", "xyz"));
    }
}
