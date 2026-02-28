from switchables.switchable import Switchable
from switchables.lightbulb import Lightbulb
from power_switch import PowerSwitch


def main():
    print(Switchable)
    bulb = Lightbulb()
    print(bulb)

    bulb.turn_on()
    bulb.turn_off()
    bulb.turn_on()

    switch = PowerSwitch(bulb)
    switch.toggle()
    switch.toggle()
    switch.toggle()


if __name__ == "__main__":
    main()
