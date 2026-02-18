# conditionals
# 0, 0.0, '', "", [], (), {} are falsy values
isAdult = 18
age = 61
old = 60

if age >= isAdult and age < old:
    print("you are adult")
elif age >= old:
    print("you are old")
else:
    print("you are not adult")
