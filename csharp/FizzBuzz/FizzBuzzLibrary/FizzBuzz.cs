namespace FizzBuzz;

public class FizzBuzz
{
    public record Factor(int Value, string Name);

    public void Print(TextWriter writer)
    {
        for (int i = 1; i < 101; i++)
        {
            writer.WriteLine(Convert(i));
        }
    }
    
    public string Convert(int number)
    {
        var result = "";

        var factors = new List<Factor>
        {
            new Factor(3, "Fizz"),
            new Factor(5, "Buzz")
        };

        foreach (var factor in factors)
        {
            if (number % factor.Value == 0)
            {
                result += factor.Name;
            }
        }

        if (result == "")
            return "" + number;
        return result;
    }
}