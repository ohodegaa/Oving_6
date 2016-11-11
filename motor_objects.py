__author__ = 'ohodegaa'

from wrappers.motors import Motors
import random as r


class BeltsController:
    _sharp_turn_dur = 0.35
    _default_speed = 0.3
    _sharp_turn_speed = 0.4

    def __init__(self):
        self.motor = Motors()
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):
        self.motor.set_value([-self._sharp_turn_speed, self._sharp_turn_speed], dur=self._sharp_turn_dur)

    def sharp_right(self):
        self.motor.set_value([self._sharp_turn_speed, -self._sharp_turn_speed], dur=self._sharp_turn_dur)

    def full_turn(self):
        self.motor.set_value([-self._sharp_turn_speed, self._sharp_turn_speed], dur=1.3)

    def backwards(self, dur=None):
        self.motor.backward(speed=self._default_speed, dur=dur)

    def forward(self, dur=None):
        self.motor.forward(speed=self._default_speed, dur=dur)

    def turn_left(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.tilt_left()

    def turn_right(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.tilt_right()

    def random(self):
        self.motor.set_value([self._default_speed * (-1 + 2*r.random()), self._default_speed * (-1 + 2*r.random())])

    def stop(self):
        self.motor.stop()

    def operationalize(self):
        for (func, args) in self.value:
            print(func.__name__)
            print(*args)
            func(*args)
