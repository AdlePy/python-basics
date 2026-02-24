# exercise 1
def make_cube(num):
    return num**3


# exercise 2
def repeat(param):
    if isinstance("hello", str):
        return param * 3
    else:
        return str(param) * 2


# exercise 3
def create_powers(*nums, power):
    return [num**power for num in nums]


# exercise 4
def reverse_number(num):
    return str(num)[::-1]


# exercsie 5
def fac(n):
    if n == 0 or n == 1:
        return 1

    return n * fac(n - 1)


print(fac(3))
