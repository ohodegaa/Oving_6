__author__ = 'ohodegaa'

from motor_objects import BeltsController
from zumo_button import ZumoButton

def main():
    motor = BeltsController()
    ZumoButton().wait_for_press()

    while True:
        dir_ = input(">>> ")
        if dir_ == "w":
            motor.forward(dur=1)
        elif dir_ == "s":
            motor.backwards(dur=1)
        elif dir_ == "d":
            motor.set_value(1, -1)
        elif dir_ == "a":
            motor.set_value(-1, 1)
        elif dir_ == "stop":
            break

    motor.stop()


main()
