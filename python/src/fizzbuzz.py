from typing import Iterable

_DEFAULT_FACTORS = {
    3: "Fizz",
    5: "Buzz",
}


def convert(
    num: int,
    factor_names: dict[int, str] = _DEFAULT_FACTORS,
) -> str:
    factornames = "".join(
        name for factor, name in factor_names.items() if num % factor == 0
    )
    return factornames or str(num)


def for_print(
    start: int = 1,
    end: int = 100,
    factor_names: dict[int, str] = _DEFAULT_FACTORS,
) -> Iterable[str]:
    return (convert(i, factor_names) for i in range(1, 101))
