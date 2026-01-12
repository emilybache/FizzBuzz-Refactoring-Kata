#include "catch2/catch.hpp"
#include "FizzBuzz.h"

TEST_CASE("NonMultipleOfThreeOrFiveArePreserved") {
    FizzBuzz fizzBuzz;
    REQUIRE(fizzBuzz.convert(1) == "1");
    REQUIRE(fizzBuzz.convert(4) == "4");
}

TEST_CASE("MultipleOfThreeAreFizz") {
    FizzBuzz fizzBuzz;
    REQUIRE(fizzBuzz.convert(3) == "Fizz");
    REQUIRE(fizzBuzz.convert(6) == "Fizz");
}

TEST_CASE("MultipleOfFiveAreBuzz") {
    FizzBuzz fizzBuzz;
    REQUIRE(fizzBuzz.convert(5) == "Buzz");
    REQUIRE(fizzBuzz.convert(10) == "Buzz");
}

TEST_CASE("MultipleOfThreeAndFiveAreFizzBuzz") {
    FizzBuzz fizzBuzz;
    REQUIRE(fizzBuzz.convert(15) == "FizzBuzz");
    REQUIRE(fizzBuzz.convert(30) == "FizzBuzz");
}
