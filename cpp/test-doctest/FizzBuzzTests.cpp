#define DOCTEST_CONFIG_ASSERTS_RETURN_VALUES
#include "doctest/doctest.h"
#include "ApprovalTests.hpp"
#include "FizzBuzz.h"
#include <sstream>

TEST_CASE("NonMultipleOfThreeOrFiveArePreserved") {
    FizzBuzz fizzBuzz;
    CHECK(fizzBuzz.convert(1) == "1");
    CHECK(fizzBuzz.convert(4) == "4");
}

TEST_CASE("MultipleOfThreeAreFizz") {
    FizzBuzz fizzBuzz;
    CHECK(fizzBuzz.convert(3) == "Fizz");
    CHECK(fizzBuzz.convert(6) == "Fizz");
}

TEST_CASE("MultipleOfFiveAreBuzz") {
    FizzBuzz fizzBuzz;
    CHECK(fizzBuzz.convert(5) == "Buzz");
    CHECK(fizzBuzz.convert(10) == "Buzz");
}

TEST_CASE("MultipleOfThreeAndFiveAreFizzBuzz") {
    FizzBuzz fizzBuzz;
    CHECK(fizzBuzz.convert(15) == "FizzBuzz");
    CHECK(fizzBuzz.convert(30) == "FizzBuzz");
}

TEST_CASE("FizzBuzz up to 100") {
    std::stringstream bo;
    FizzBuzz().print(bo);
    ApprovalTests::Approvals::verify(bo.str());
}
