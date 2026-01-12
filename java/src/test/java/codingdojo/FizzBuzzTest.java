package codingdojo;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {
    @Test
    @DisplayName("Normal numbers are preserved")
    void normalNumbersArePreserved() {
        assertAll(
                () -> assertEquals("1", new FizzBuzz().convert(1)),
                () -> assertEquals("4", new FizzBuzz().convert(4))
        );
    }

    @Test
    @DisplayName("Multiples of 3 are Fizz")
    void multiplesOf3AreFizz() {
        assertAll(
                () -> assertEquals("Fizz", new FizzBuzz().convert(3)),
                () -> assertEquals("Fizz", new FizzBuzz().convert(6))
        );
    }

    @Test
    @DisplayName("Multiples of Five are Buzz")
    void multiplesOfFiveAreBuzz() {
        assertAll(
                () -> assertEquals("Buzz", new FizzBuzz().convert(5)),
                () -> assertEquals("Buzz", new FizzBuzz().convert(10))
        );
    }

    @Test
    @DisplayName("Multiples of Three and Five are Buzz")
    void multiplesOfThreeAndFiveAreBuzz() {
        assertAll(
                () -> assertEquals("FizzBuzz", new FizzBuzz().convert(15)),
                () -> assertEquals("FizzBuzz", new FizzBuzz().convert(30))
        );
    }

}
