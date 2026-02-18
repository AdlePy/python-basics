# tuples
my_tuple = (1, 2, 3)
print(my_tuple, ":", type(my_tuple))
print("my_tuple length:", len(my_tuple))
print("first element:", my_tuple[0])

first_number, second_number, third_number = my_tuple
print("first number:", first_number)
print("second number:", second_number)
print("third number:", third_number)

var_swap = 3
var_to_swap = 4

var_swap, var_to_swap = var_to_swap, var_swap
print("swapped variables:", var_swap, var_to_swap)

# lists
my_list = ["abc", "def", "ghi"]
print("my_list:", my_list)

my_list.append("jkl")
print("my_list:", my_list)

another_list = my_list
another_list.append("pqr")
print("my_list:", my_list)
print("another_list:", another_list)

copied_list = my_list.copy()
copied_list.append("stu")
print("my_list:", my_list)
print("copied_list:", copied_list)

reversed_list = my_list[::-1]
print("my_list:", my_list)
print("reversed_list:", reversed_list)

another_list.remove("def")
print("another_list:", another_list)

popped_item = another_list.pop()
print("popped_item:", popped_item, "another_list:", another_list)

# dictionaries
my_dict = {1: "one", 2: "two", 3: "three"}
print("my_dict:", my_dict)

print("first key:", my_dict[1])
print("dict:", my_dict.items())
print("my_dict keys:", my_dict.keys())
print("my_dict values:", my_dict.values())

copied_dict = my_dict.copy()
print("my_dict:", my_dict)
print("coped_dict:", copied_dict)

popped_dict_item = copied_dict.pop(1)
print("popped item:", popped_dict_item, "coped_dict:", copied_dict)

copied_dict.clear()
print("cleared dict:", copied_dict)

# sets
my_set = {1, 2, 3, 4, 5}
another_set = {1, 2, 6, 7}
print("my_set:", my_set)

my_set.add(1)
my_set.add(6)
print("my_set:", my_set)

print(1 in my_set)
print(11 in my_set)

print(my_set.difference(another_set))
print(my_set.intersection(another_set))
print(my_set.issubset(another_set))
print(my_set.union(another_set))

# comprehensions
list_comprehension = [char for char in "adilet"]
print("list comprehension:", list_comprehension)

dict_comprehension = {char: ord(char) for char in "askar"}
print("dict comprehension:", dict_comprehension)

set_comprehension = {char for char in "erlanuly"}
print("set comprehension:",  set_comprehension)