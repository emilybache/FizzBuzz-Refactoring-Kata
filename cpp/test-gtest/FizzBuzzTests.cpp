#include <gtest/gtest.h>
#include "ApprovalTests.hpp"
#include "FizzBuzz.h"
#include <sstream>

TEST(FizzBuzzTests, NonMultipleOfThreeOrFiveArePreserved) {
    FizzBuzz fizzBuzz;
    EXPECT_EQ(fizzBuzz.convert(1), "1");
    EXPECT_EQ(fizzBuzz.convert(4), "4");
}

TEST(FizzBuzzTests, MultipleOfThreeAreFizz) {
    FizzBuzz fizzBuzz;
    EXPECT_EQ(fizzBuzz.convert(3), "Fizz");
    EXPECT_EQ(fizzBuzz.convert(6), "Fizz");
}

TEST(FizzBuzzTests, MultipleOfFiveAreBuzz) {
    FizzBuzz fizzBuzz;
    EXPECT_EQ(fizzBuzz.convert(5), "Buzz");
    EXPECT_EQ(fizzBuzz.convert(10), "Buzz");
}

TEST(FizzBuzzTests, MultipleOfThreeAndFiveAreFizzBuzz) {
    FizzBuzz fizzBuzz;
    EXPECT_EQ(fizzBuzz.convert(15), "FizzBuzz");
    EXPECT_EQ(fizzBuzz.convert(30), "FizzBuzz");
}

TEST(FizzBuzzTests, fizzBuzzUpTo100) {
    std::stringstream bo;
    FizzBuzz().print(bo);
    ApprovalTests::Approvals::verify(bo.str());
}
