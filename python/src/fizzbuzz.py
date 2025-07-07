from typing import Iterable


def convert(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def for_print() -> Iterable[str]:
    return (convert(i) for i in range(1, 101))
