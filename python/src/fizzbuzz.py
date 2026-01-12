import sys
from typing import NamedTuple


class Factor(NamedTuple):
    number: int
    name: str


class FizzBuzz:
    def convert(self, num):
        result = ""
        factors = [
            Factor(3, "Fizz"),
            Factor(5, "Buzz")
        ]

        for factor in factors:
            if num % factor.number == 0:
                result += factor.name

        return result if result else str(num)

    def print(self, output):
        output.write("\n".join(
            self.convert(i)
            for i in range(1, 101)) + "\n"
                     )


if __name__ == "__main__":
    FizzBuzz().print(sys.stdout)
