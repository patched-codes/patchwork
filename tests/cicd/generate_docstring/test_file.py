import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-3, 2));
    }

    @Test
    void testAPlusBWithKeymap() {
        assertEquals(-1, Test.a_plus_b(o -> ((Comparable) o).toString().length(), "hi", "hello"));
        assertEquals(1, Test.a_plus_b(o -> ((Comparable) o).toString().length(), "world", "hi"));
        assertEquals(0, Test.a_plus_b(o -> ((Comparable) o).toString().length(), "same", "size"));
    }

    @Test
    void testAPlusBWithKeymapThrowsException() {
        assertThrows(NullPointerException.class, () -> {
            Test.a_plus_b(null, null, null);
        });
    }
}
