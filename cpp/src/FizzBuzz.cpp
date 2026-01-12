#include "FizzBuzz.h"

void FizzBuzz::print(std::ostream& out) {
    for (int i = 1; i < 101; i++) {
        out << convert(i) << std::endl;
    }
}

std::string FizzBuzz::convert(int number) {
    if (number % 15 == 0) {
        return "FizzBuzz";
    }

    if (number % 5 == 0) {
        return "Buzz";
    }

    if (number % 3 == 0) {
        return "Fizz";
    }

    return std::to_string(number);
}
