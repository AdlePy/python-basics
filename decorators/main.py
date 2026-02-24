from functools import wraps
from timeit import default_timer


def my_decorator(func_to_decorate):
    print("my decorator: create a new func")

    def replacement_function():
        print("running replacement function")
        func_to_decorate()
        print("finished running replacement funtion")

    return replacement_function


@my_decorator
def my_function():
    print("my function runs")


my_function()


def dec_with_one_arg(func):
    @wraps(func)
    def wrapper(arg):
        print(f"call func {func} with arg {arg}")
        result = func(arg)
        print(f"result: {result}")
        return result

    return wrapper


@dec_with_one_arg
def cube(num):
    return num**3


cube(4)


def show_timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_timer = default_timer()
        func(*args, **kwargs)
        end_timer = default_timer()
        total_time = end_timer - start_timer
        print(f"executed func {func} in {total_time:.10f} sec")

    return wrapper


@show_timing
def power_numbers(*nums, power=2):
    return [n**power for n in nums]


power_numbers(2, 4)
