class VehicleBase:
    def __init__(self, color):
        self.color = color

    def make_sound(self):
        print("no sound")


class Car(VehicleBase):
    def __init__(self, color, wheels):
        super().__init__(color)
        self.wheels = wheels

    def make_sound(self):
        print("beeep")

    def open_trunk(self):
        print("opened trunk")


class Ship(VehicleBase):
    def __init__(self, color, cabins):
        super().__init__(color)
        self.cabins = cabins

    def make_sound(self):
        print("whoooo")

    def set_sail(self):
        print("set sail")


class Amphibian(Car, Ship):
    def __init__(self, color, wheels):
        self.cabins = 0
        self.color = color
        self.wheels = wheels

    def toogle_mode(self):
        print("toggled mode")


car = Car("white", 4)
print(f"{car.color} car with {car.wheels} wheels")

ship = Ship("grey", 5)
print(f"{ship.color} ship with {ship.cabins} cabins")

amphibian = Amphibian("green", 4)
print(f"{amphibian.color} amphibian with {amphibian.wheels} wheels")

car.make_sound()
car.open_trunk()

ship.make_sound()
ship.set_sail()

amphibian.make_sound()
amphibian.set_sail()
amphibian.open_trunk()
amphibian.toogle_mode()
