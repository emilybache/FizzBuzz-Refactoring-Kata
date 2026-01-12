#include "FizzBuzz.h"

void FizzBuzz::print(std::ostream& out) {
    for (int i = 1; i < 101; i++) {
        out << convert(i) << std::endl;
    }
}

std::string FizzBuzz::convert(int number) {
    std::string result = "";

    std::vector<Factor> factors = {
            Factor(3, "Fizz"),
            Factor(5, "Buzz")
    };

    for (const auto& factor : factors) {
        if (number % factor.value == 0) {
            result += factor.name;
        }
    }

    if (result == "") {
        return std::to_string(number);
    }
    return result;
}
