from functools import reduce, lru_cache, partial
import operator


def demo_reduce():
    result = reduce(operator.mul, [2, 4, 5, 9, 16])
    print(result)

    line = reduce(operator.concat, ["abc", "def", "ghi"])
    print(line)


def demo_reduce_pro():
    numbers = (2, 3, 4, 0, 7, 5)
    print(reduce(min, numbers))
    print(reduce(max, numbers))


@lru_cache
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def demo_fib():
    print(list(map(fib, range(35))))


def mult(a, b):
    return a * b


def demo_partial():
    mul_2 = partial(mult, 2)
    print(mul_2(3))


def main():
    # demo_reduce()
    # demo_fib()
    # demo_partial()
    demo_reduce_pro()


if __name__ == "__main__":
    main()
