package codingdojo;

import java.io.PrintStream;
import java.util.List;

public class FizzBuzz {
    public void print(PrintStream out) {
        for (int i = 1; i < 101; i++) {
            out.println(convert(i));
        }
    }
    public String convert(int number) {
        var result = "";

        var factors = List.of(
                new Factor(3, "Fizz"),
                new Factor(5, "Buzz")
        );

        for (Factor factor : factors) {
            if (number % factor.factor() == 0) {
                result += factor.name();
            }
        }

        if ("".equals(result))
            return "" + number;
        return result;
    }
}
