"""
this is doc for this  module
"""

some_object = object()
print(f"some_object: {some_object}")


def my_func(a, b):
    """
    this is my_func docstring
    this function swaps a and b
    args: a, b
    """
    return b, a


help(my_func)
print(my_func.__doc__)


class User:
    """
    empty User class
    """


first_user = User()
print(f"class: {User}, class object: {first_user}, type: {type(first_user)}")
print(User.mro())
