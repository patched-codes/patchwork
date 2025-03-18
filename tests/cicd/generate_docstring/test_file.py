import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        Assertions.assertEquals(5, Test.a_plus_b(2, 3));
        Assertions.assertEquals(-1, Test.a_plus_b(-4, 3));
    }

    @Test
    void testAPlusBFunction() {
        Function<Object, Integer> mockFunction = obj -> (int) obj;
        Assertions.assertEquals(0, Test.a_plus_b(mockFunction, 5, 5));
        Assertions.assertEquals(1, Test.a_plus_b(mockFunction, 10, 5));
        Assertions.assertEquals(-1, Test.a_plus_b(mockFunction, 2, 8));
    }
}
