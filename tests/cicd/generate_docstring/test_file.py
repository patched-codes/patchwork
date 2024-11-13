import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestUnit {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
    }

    @Test
    void testAPlusBWithFunction() {
        Function<Object, Comparable> func = obj -> (Integer) obj;

        assertEquals(-1, Test.a_plus_b(func, 1, 2));
        assertEquals(1, Test.a_plus_b(func, 3, 2));
        assertEquals(0, Test.a_plus_b(func, 2, 2));
    }
}
