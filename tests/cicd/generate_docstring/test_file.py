import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class TestTest {

    @Test
    void testAPlusBWithIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusBWithKeymap() {
        assertEquals(-1, Test.a_plus_b(x -> (Integer) x, 1, 2));
        assertEquals(1, Test.a_plus_b(x -> (Integer) x, 3, 2));
        assertEquals(0, Test.a_plus_b(x -> (Integer) x, 3, 3));
    }
}
