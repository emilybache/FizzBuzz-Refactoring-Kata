from io import StringIO

import pytest
from approvaltests import verify

from fizzbuzz import FizzBuzz


def test_non_multiple_of_three_or_five_are_preserved():
    assert FizzBuzz().convert(1) == "1"
    assert FizzBuzz().convert(4) == "4"

def test_multiple_of_three_are_fizz():
    assert FizzBuzz().convert(3) == "Fizz"
    assert FizzBuzz().convert(6) == "Fizz"

def test_multiple_of_five_are_buzz():
    assert FizzBuzz().convert(5) == "Buzz"
    assert FizzBuzz().convert(10) == "Buzz"

def test_multiple_of_three_and_five_are_fizzbuzz():
    assert FizzBuzz().convert(15) == "FizzBuzz"
    assert FizzBuzz().convert(30) == "FizzBuzz"


pytest.mark.slow
def test_fizzbuzz_to_100():
    out = StringIO()
    FizzBuzz().print(out)
    verify(out.getvalue())
