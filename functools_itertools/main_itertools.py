from itertools import (
    zip_longest,
    cycle,
    count,
    combinations,
    combinations_with_replacement,
    permutations,
)

names = ["Sam", "Nick", "John"]
surnames = ["White", "Black", "Smith"]
emails = ["email@email.com", "matho@mail.ru", "prelord123@gmail.com", "sara@vk.ru"]


def demo_zip():
    pairs = zip(names, surnames)
    print(list(pairs))

    accounts = zip(names, surnames, emails)
    print(list(accounts))

    long_accounts = zip_longest(names, surnames, emails)
    print(list(long_accounts))


def demo_cycle():
    emails_demo = ["test@mail.ru", "egg@mail.ru"]
    pairs = zip(names, cycle(emails_demo))
    print(list(pairs))


def demo_count():
    c = count(1)
    result = zip(names, c)
    print(list(result))


def demo_combinations():
    nums = list(range(10))
    print(list(combinations(nums, 2)))
    print(list(combinations_with_replacement(nums, 2)))
    print(list(permutations(nums, 2)))


def main():
    demo_zip()
    demo_cycle()
    demo_count()
    demo_combinations()


if __name__ == "__main__":
    main()
