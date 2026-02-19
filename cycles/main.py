# iterating over collections
test_str = "test string"

for char in test_str:
    print(char)

cities = ["Almaty", "Astana", "Oral", "Kyzylorda"]

for city in cities:
    print(city)

odd_set = {1, 3, 5, 7, 9, 11}

for num in odd_set:
    print(num)

test_dict = {
    "foo": "bar",
    "fizz": "buzz",
    "egg": "spam",
}

for k, v in test_dict.items():
    print(k, ":", v)

for k in test_dict.keys():
    print("key:", k)

for v in test_dict.values():
    print("val:", v)

for city in cities:
    print("process city:", city)

    if len(city) < 5:
        print("found city with length less than 5:", city)

    print("next iteration...")

# break, continue and else
for city in cities:
    print("process city:", city)

    if len(city) < 5:
        print("found city with length less than 5:", city)
        break

    print("next iteration...")


for city in cities:
    if city.startswith("A"):
        continue

    print("process city:", city)
    print("next iteration...")

for city in cities:
    print("process city:", city)

    if len(city) < 5:
        print("found city with length less than 5:", city)
        break

    print("next iteration...")
else:
    print("end of loop, no break")

# ranges
for i in range(5):
    print(i)

# NoneType
first_city = None
print("first_city:", first_city, "type:", type(first_city))

# while loop
power = 0
value = 0

while value < 10000:
    power += 1
    value = 2**power
    print("value =", value, "when power is", power)

i = 0
total_amount = 0

while total_amount < 100:
    i += 1
    total_amount += i
    print("value =", total_amount, "when i is", i)
else:
    print("finished loop by condition")

# netsted loops
for i in range(4):
    print("iteration", i)
    for j in range(5):
        print(i, j)
