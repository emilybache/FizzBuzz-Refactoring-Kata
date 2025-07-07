import fizzbuzz


def _get_number_at(index: int) -> str:
    return list(fizzbuzz.for_print())[index - 1]


def test_non_multiple_of_three_or_five_are_preserved() -> None:
    assert _get_number_at(1) == "1"
    assert _get_number_at(4) == "4"


def test_multiple_of_three_are_fizz() -> None:
    assert _get_number_at(3) == "Fizz"
    assert _get_number_at(6) == "Fizz"


def test_multiple_of_five_are_buzz() -> None:
    assert _get_number_at(5) == "Buzz"
    assert _get_number_at(10) == "Buzz"


def test_multiple_of_three_and_five_are_fizzbuzz() -> None:
    assert _get_number_at(15) == "FizzBuzz"
    assert _get_number_at(30) == "FizzBuzz"


def test_print() -> None:
    all = list(fizzbuzz.for_print())
    assert len(all) == 100
    assert all[0] == "1"
    assert all[-1] == "Buzz"
