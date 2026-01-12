#ifndef FIZZBUZZ_H
#define FIZZBUZZ_H

#include <string>
#include <ostream>

class FizzBuzz {
public:
    void print(std::ostream& out);
    std::string convert(int number);
};

#endif // FIZZBUZZ_H
