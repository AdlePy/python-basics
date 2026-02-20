# function declaration
def f(x):
    return x**2


def greet():
    print("hello")


def greet_person(person):
    print(f"Hello, {person}")


def power_number(number, power=2):
    return number**power


def power_numbers(numbers, power=2):
    return [num**power for num in numbers]


def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


def extend_list(new_data, list_to_extend=None):
    if list_to_extend is None:
        list_to_extend = []
    for data in new_data:
        list_to_extend.append(data)
    return list_to_extend


def find_by_key(key, **kwargs):
    if key in kwargs:
        print(f"key {key} found in kwargs, value = {kwargs[key]}")


print(f(2))
greet()
greet_person("Adilet")
greet_person(person="Alisher")
print(power_number(power=2, number=3))
print(power_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
sum_numbers(1, 2)
sum_numbers(1, 2, 3, 4)
print(extend_list([1, 2], []))
find_by_key("spam", foo="bar", fizz="buzz", spam="egg")


# anonymous functions
print(list(map(power_number, [1, 2, 3, 4, 5])))
print(list(zip((1, 2), (2, 4))))
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))
