__author__ = 'ohodegaa'

from motor_objects import Motors
from zumo_button import ZumoButton

def main():
    motor = Motors()
    ZumoButton().wait_for_press()

    while True:
        dir_ = input(">>> ")
        if dir_ == "w":
            motor.forward(dur=1)
        elif dir_ == "s":
            motor.backward(dur=1)
        elif dir_ == "d":
            motor.right(dur=1)
        elif dir_ == "a":
            motor.left(dur=1)
        elif dir_ == "stop":
            break

    motor.stop()