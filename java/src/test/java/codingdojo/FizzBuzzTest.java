package codingdojo;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {

@Test
    public void NonMultipleOfThreeOrFiveArePreserved()
    {
        assertEquals("1", new FizzBuzz().convert(1));
        assertEquals("4", new FizzBuzz().convert(4));
    }   
    @Test
    public void MultipleOfThreeAreFizz()
    {
        assertEquals("Fizz", new FizzBuzz().convert(3));
        assertEquals("Fizz", new FizzBuzz().convert(6));
    }
        
    @Test
    public void MultipleOfFiveAreBuzz()
    {
        assertEquals("Buzz", new FizzBuzz().convert(5));
        assertEquals("Buzz", new FizzBuzz().convert(10));
    }
        
    @Test
    public void MultipleOfThreeAndFiveAreFizzBuzz()
    {
        assertEquals("FizzBuzz", new FizzBuzz().convert(15));
        assertEquals("FizzBuzz", new FizzBuzz().convert(30));
    }

    @Test
    public void MultipleOfThreeAndFiveAndSevenAreFizzBuzzWhizz()
    {
        assertEquals("FizzBuzzWhizz", new FizzBuzz().convert(105));
        assertEquals("BuzzBang", new FizzBuzz().convert(110));
    }
}
