import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestTest {

    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-3, 2));
    }
    
    @Test
    public void testAPlusBWithKeyMap() {
        assertEquals(-1, Test.a_plus_b((Object obj) -> ((String) obj).length(), "apple", "banana"));
        assertEquals(1, Test.a_plus_b((Object obj) -> ((String) obj).length(), "banana", "apple"));
        assertEquals(0, Test.a_plus_b((Object obj) -> ((String) obj).length(), "apple", "apple"));
    }
}
