#ifndef FIZZBUZZ_H
#define FIZZBUZZ_H

#include <string>
#include <ostream>
#include <utility>
#include <vector>

struct Factor {
    int value;
    std::string name;
    Factor(int v, std::string n) : value(v), name(std::move(n)) {}
};

class FizzBuzz {
public:
    void print(std::ostream& out);
    std::string convert(int number);
};

#endif // FIZZBUZZ_H
