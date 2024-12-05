import org.junit.Test;
import org.junit.Assert;
import java.util.function.Function;

public class TestTest {

    @Test
    public void testAPlusBIntegers() {
        Assert.assertEquals(5, Test.a_plus_b(2, 3));
        Assert.assertEquals(0, Test.a_plus_b(-2, 2));
        Assert.assertEquals(-5, Test.a_plus_b(-2, -3));
    }

    @Test
    public void testAPlusBWithFunction() {
        Function<Object, Integer> keyMap = obj -> (Integer) obj;
        Assert.assertEquals(-1, Test.a_plus_b(keyMap, 1, 2));
        Assert.assertEquals(1, Test.a_plus_b(keyMap, 3, 2));
        Assert.assertEquals(0, Test.a_plus_b(keyMap, 5, 5));
    }
}
