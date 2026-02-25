class User:
    def __init__(self):
        self.name = None
        self.age = None


first_user = User()
print(first_user.__dict__)

first_user.name = "Adilet"
first_user.age = 29
print(first_user.__dict__)
