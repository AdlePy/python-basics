class User:
    name = None
    age = None


first_user = User()
print(f"first user name: {first_user.name}")
print(f"age user name: {first_user.age}")

first_user.name = "Adilet"
print(f"first user name: {first_user.name}")
print(first_user.__dict__)

second_user = User()
second_user.name = "Sam"
second_user.age = 20
print(second_user.__dict__)
