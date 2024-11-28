from typing import Callable


def sum(list: list[int]) -> int:  # type: ignore
    match list:
        case []:
            return 0
        case [x, *xs]:
            return x + sum(xs)


def sum_iter(list: list[int]) -> int:
    res = 0
    for x in list:
        res = res + x
    return res


def prod(list: list[int]) -> int: 
    match list:
        case [x, *xs]:
            return x * prod(xs)
        case _:
            return 1


def prod_iter(list: list[int]) -> int:
    res = 1
    for x in list:
        res = res * x
    return res


def concat(list: list[list[int]]) -> list[int]:  # type: ignore
    res = []
    for xs in list:
        res = res + xs
    return res


def fold(op, base, list):
    match list:
        case []:
            return base
        case [x, *xs]:
            return op(x, fold(op, base, xs))


def sum_fold(list):
    return fold(lambda x, acc: x + acc, 0, list)


if __name__ == "__main__":
    data = [12, 1, 3, 30, 2, 24, 80, 4, 5, 6]
    print(f"Sum of the data: {sum_fold(data)}")
