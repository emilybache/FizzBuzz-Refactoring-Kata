namespace FizzBuzz;

public class FizzBuzz
{
    public void Print()
    {
        for (int i = 1; i < 101; i++)
        {
            Console.WriteLine(Convert(i));
        }
    }
    
    public string Convert(int number)
    {
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

        return number.ToString();
    }
}