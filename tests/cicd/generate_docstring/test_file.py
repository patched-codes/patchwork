import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.function.Function;

public class TestTest {
    
    @Test
    public void testAPlusBIntegers() {
        assertEquals(5, Test.a_plus_b(2, 3));
        assertEquals(-1, Test.a_plus_b(-2, 1));
    }

    @Test
    public void testAPlusBKeymap() {
        Function<Object, Comparable> mockKeyMap = elem -> (Integer) elem;
        
        assertEquals(-1, Test.a_plus_b(mockKeyMap, 1, 2));
        assertEquals(1, Test.a_plus_b(mockKeyMap, 3, 2));
        assertEquals(0, Test.a_plus_b(mockKeyMap, 3, 3));
    }
}
