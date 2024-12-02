import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TestTest {

    @Test
    void testAPlusB_Integer() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-2, 2));
        assertEquals(-5, Test.a_plus_b(-2, -3));
    }

    @Test
    void testAPlusB_Function() {
        assertEquals(-1, Test.a_plus_b(String::length, "a", "abc"));
        assertEquals(1, Test.a_plus_b(String::length, "abcde", "abc"));
        assertEquals(0, Test.a_plus_b(String::length, "abc", "abc"));
    }
}
