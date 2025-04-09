package codingdojo;

import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {

    @Test
    public void NonMultipleOfThreeOrFiveArePreserved() {
        assertEquals("1", new FizzBuzz().convert(1));
        assertEquals("4", new FizzBuzz().convert(4));
    }

    @Test
    public void MultipleOfThreeAreFizz() {
        assertEquals("Fizz", new FizzBuzz().convert(3));
        assertEquals("Fizz", new FizzBuzz().convert(6));
    }

    @Test
    public void MultipleOfFiveAreBuzz() {
        assertEquals("Buzz", new FizzBuzz().convert(5));
        assertEquals("Buzz", new FizzBuzz().convert(10));
    }

    @Test
    public void MultipleOfThreeAndFiveAreFizzBuzz() {
        assertEquals("FizzBuzz", new FizzBuzz().convert(15));
        assertEquals("FizzBuzz", new FizzBuzz().convert(30));
    }

    @Test
    public void PrintsTo100() {
        var stream = new ByteArrayOutputStream();

        new FizzBuzz().print(new PrintStream(stream));

        String output = stream.toString(StandardCharsets.UTF_8);
        String[] allLines = output.split(System.lineSeparator());
        assertEquals(100, allLines.length);
        assertEquals("1", allLines[0]);
        assertEquals("Buzz", allLines[allLines.length - 1]);
    }
}
