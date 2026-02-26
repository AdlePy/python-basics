def get_weather(city):
    if city != "Moscow":
        raise ValueError("invalid city provided")

    return {
        "temp": 12,
        "humidity": 50,
        "rain_chance": 0,
    }


def rain_tomorrow(city):
    print(f"will it rain tomorrow: {city}")

    try:
        weather = get_weather(city)
    except ValueError:
        return None

    return weather["rain_chance"] > 50


print(rain_tomorrow("Sochi"))


def div_save(num_a, num_b):
    try:
        result = num_a / num_b
    except ZeroDivisionError:
        print("please do not divide by zero")
        return None
    except TypeError as e:
        print("provide number type", e)
        return None
    else:
        return result
    finally:
        print("function finished")


print(div_save(3, 0))


# name mangling
class User:
    def __init__(self, name):
        self.name = name
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new):
        self.__password = new


my_user = User(name="John")
print(my_user.name, my_user.password)
