package codingdojo;

import java.io.PrintStream;

public class FizzBuzz {
    public void print(PrintStream out) {
        for (int i = 1; i < 101; i++) {
            out.println(convert(i));
        }
    }
    public String convert(int number) {
        if (number % 15 == 0)
        {
            return "FizzBuzz";
        }

        if (number % 5 == 0)
        {
            return "Buzz";
        }

        if (number % 3 == 0)
        {
            return "Fizz";
        }

        return "" + number;
    }
}
