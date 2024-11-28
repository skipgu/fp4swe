## Insertion sort

def insertion_sort(xs: list[int]):
    for i in range(1, len(xs)):
        x: int = xs[i]
        while i > 0 and x < xs[i - 1]:
            xs[i] = xs[i - 1]
            i -= 1
        xs[i] = x


## Merge sort, iterative (bottom-up)

def sort(xs: list[int]) -> list[int]:
    xss = []
    for x in xs:
        xss.append([x])
    while len(xss) > 1:
        temp = []
        for i in range(1, len(xss), 2):
            temp.append(merge(xss[i - 1], xss[i]))
        xss = temp
    return xss[0]


def merge(xs: list[int], ys: list[int]) -> list[int]:
    res = []
    i, j = 0, 0
    while i < len(xs) and j < len(ys):
        if xs[i] <= ys[j]:
            res.append(xs[i])
            i += 1
        else:
            res.append(ys[j])
            j += 1
    for x in xs[i:]:
        res.append(x)
    for y in ys[j:]:
        res.append(y)
    return res


## Recursive merge sort

def sort_rec(xs: list[int]) -> list[int]:
    n = len(xs)
    if n < 2:
        return xs.copy()
    else:
        mid = n // 2
        low = sort_rec(xs[0:mid])
        hgh = sort_rec(xs[mid:])
        return merge_rec(low, hgh)


def merge_rec(xs: list[int], ys: list[int]) -> list[int]:
    if len(xs) < 1 or len(ys) < 1:
        return xs.copy() + ys.copy()
    else:
        if xs[0] < ys[0]:
            return [xs[0]] + merge_rec(xs[1:], ys)
        else:
            return [ys[0]] + merge_rec(xs, ys[1:])


## Pattern matching
def sort_pat(xs: list[int]) -> list[int]:
    match xs:
        case [] | [_]:
            return xs.copy()
        case _:
            mid = len(xs) // 2
            low = sort_pat(xs[0:mid])
            hgh = sort_pat(xs[mid:])
            return merge_pat(low, hgh)


def merge_pat(xs: list[int], ys: list[int]) -> list[int]:
    match xs, ys:
        case [x, *xr], [y, *yr]:
            if x < y:
                return [x] + merge_pat(xr, ys) 
            else:
                return [y] + merge_pat(xs, yr)
        case _:
            return xs.copy() + ys.copy()


## Test

if __name__ == "__main__":
    data = [12, 1, 3, 30, 2, 24, 80, 4, 5, 6]
    print(f"After: {sort_pat(data)}")





## Higher-order functions, abstract away comparison

def sort_by(data, cmp):
    def go(xs):
        match xs:
            case [] | [_]:
                return xs
            case _:
                mid = len(xs) // 2
                return merge_by(go(xs[0:mid]), go(xs[mid:]), cmp)
    return go(data)


def merge_by(left, right, cmp):
    def go(xs, ys):
        match xs, ys:
            case [x, *xr], [y, *yr]:
                return [x] + go(xr, ys) if cmp(x, y) else [y] + go(xs, yr)
            case _:
                return xs + ys
    return go(left, right)


def plain_sort(xs):
    return sort_by(xs, lambda x, y: x > y)

