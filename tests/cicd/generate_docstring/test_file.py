import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestExample {

    @Test
    public void testAPlusBInteger() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(0, Test.a_plus_b(-1, 1));
    }

    @Test
    public void testComparableAPlusB() {
        // Assuming the keymap for integers just returns the integer itself
        assertEquals(0, Test.a_plus_b(x -> (Comparable) x, 5, 5));
        assertEquals(-1, Test.a_plus_b(x -> (Comparable) x, 1, 2));
        assertEquals(1, Test.a_plus_b(x -> (Comparable) x, 3, 2));
    }
}
