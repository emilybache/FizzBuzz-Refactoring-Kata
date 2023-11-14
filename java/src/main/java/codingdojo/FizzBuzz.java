package codingdojo;

import java.util.List;

public class FizzBuzz {

    private List<Factor> factors = List.of(
            new Factor(3, "Fizz"),
            new Factor(5, "Buzz"),
            new Factor(7, "Whizz"),
            new Factor(11, "Bang")

    );

    public void print(int maxiumum) {
        for (int i = 1; i < maxiumum; i++) {
            System.out.println(convert(i));
        }
    }
    public String convert(int number) {
        var result = "";

        for (Factor factor : factors) {
            if (number % factor.factor() == 0)
            {
                result += factor.name();
            }
        }

        if ("".equals(result))
            return "" + number;
        return result;
    }
}
