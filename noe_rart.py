__author__ = 'ohodegaa'

from motor_objects import Motors

def main():
    motor = Motors()

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