from switchables.switchable import Switchable


class Lightbulb(Switchable):
    def turn_on(self):
        print(f"{self.__class__.__name__} turned on")

    def turn_off(self):
        print(f"{self.__class__.__name__} turned off")
