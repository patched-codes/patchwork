import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestJava {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-4, 3));
    }

    @Test
    void testAPlusBFunction() {
        assertEquals(-1, Test.a_plus_b(Object::toString, "hello", "world"));
        assertEquals(0, Test.a_plus_b(Object::hashCode, 3, 3));
    }
}
