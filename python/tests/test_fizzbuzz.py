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


def test_convert_custom_factors() -> None:
    factors = {
        3: "Fizz",
        5: "Buzz",
        7: "Whizz",
        11: "Bang",
    }
    assert fizzbuzz.convert(1, factors) == "1"
    assert fizzbuzz.convert(3, factors) == "Fizz"
    assert fizzbuzz.convert(5, factors) == "Buzz"
    assert fizzbuzz.convert(7, factors) == "Whizz"
    assert fizzbuzz.convert(11, factors) == "Bang"
    assert fizzbuzz.convert(3 * 5, factors) == "FizzBuzz"
    assert fizzbuzz.convert(3 * 7, factors) == "FizzWhizz"
    assert fizzbuzz.convert(3 * 5 * 7, factors) == "FizzBuzzWhizz"


def test_end_with_string() -> None:
    factors = {
        3: "Fizz",
        5: "Buzz",
        7: "Whizz",
        11: "Bang",
    }
    all = list(fizzbuzz.for_print(factor_names=factors, end="FizzBuzzWhizzBang"))
    assert all[0] == "1"
    assert all[-1] == "FizzBuzzWhizzBang"
    assert len(all) == 3 * 5 * 7 * 11
