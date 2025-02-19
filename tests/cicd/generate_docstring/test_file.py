import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.function.Function;

public class TestTest {
    
    @Test
    void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    void testAPlusBKeyMap() {
        Function<String, Integer> lengthKeyMap = String::length;
        assertEquals(0, Test.a_plus_b(lengthKeyMap, "test", "four"));
        assertEquals(-1, Test.a_plus_b(lengthKeyMap, "short", "longer"));
        assertEquals(1, Test.a_plus_b(lengthKeyMap, "longer", "short"));
    }
}
