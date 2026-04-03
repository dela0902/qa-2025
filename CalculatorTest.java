import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest {

    @Test
    public void testCalculate() {
        double result = Calculator.calculate("2+3*4");
        assertEquals(14, result, 0.001);
    }
}