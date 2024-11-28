from itertools import count
from typing import Callable, Iterator
from hypothesis import given, settings
from hypothesis.strategies import integers


def is_factor_of(n: int, x: int) -> bool:
    return n % x == 0


def factors(n: int) -> list[int]:
    return [x for x in range(1, n+1) if is_factor_of(n, x)]


def is_prime(n: int) -> bool:
    return factors(n) == [1, n]


def primes_up_to(n: int) -> list[int]:
    return [x for x in range(2, n) if is_prime(x)]


if __name__ == "__main__":
    ps: list[int] = primes_up_to(100)
    print(f"The first hunderd primes: {ps}")





## Lazy evaluation, use generators/iterators

def primes() -> Iterator[int]:
    pass


def take(n: int, xs: Iterator[int]) -> list[int]:
    pass


def takeWhile(p: Callable[[int], bool], xs: Iterator[int]) -> list[int]:
    pass


def sieve(ps):
    match ps:
        case []: 
            return []
        case [p, *xs]: 
            return [p] + sieve([x for x in xs if x % p != 0])  # type: ignore




## Tests

@given(integers(min_value=0,max_value=100000))
@settings(max_examples=100)
def test_prime(x):
    if is_prime(x):
        assert x % 2 != 0
    else:
        assert True
