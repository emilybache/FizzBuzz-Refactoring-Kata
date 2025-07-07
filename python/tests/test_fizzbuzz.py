import fizzbuzz


def test_non_multiple_of_three_or_five_are_preserved() -> None:
    assert fizzbuzz.convert(1) == "1"
    assert fizzbuzz.convert(4) == "4"


def test_multiple_of_three_are_fizz() -> None:
    assert fizzbuzz.convert(3) == "Fizz"
    assert fizzbuzz.convert(6) == "Fizz"


def test_multiple_of_five_are_buzz() -> None:
    assert fizzbuzz.convert(5) == "Buzz"
    assert fizzbuzz.convert(10) == "Buzz"


def test_multiple_of_three_and_five_are_fizzbuzz() -> None:
    assert fizzbuzz.convert(15) == "FizzBuzz"
    assert fizzbuzz.convert(30) == "FizzBuzz"


def test_print() -> None:
    all = list(fizzbuzz.for_print())
    assert len(all) == 100
    assert all[0] == "1"
    assert all[-1] == "Buzz"
