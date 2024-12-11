import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.function.Function;

class TestTest {

    @Test
    void testAPlusBIntegers() {
        int result = Test.a_plus_b(2, 3);
        assertEquals(5, result);
    }

    @Test
    void testAPlusBObjects() {
        Function<Object, Comparable> keymap = obj -> ((CustomObject) obj).getValue();
        CustomObject a = new CustomObject(1);
        CustomObject b = new CustomObject(2);
        int result = Test.a_plus_b(keymap, a, b);
        assertEquals(-1, result);
    }
    
    static class CustomObject {
        private final int value;

        CustomObject(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }
}
