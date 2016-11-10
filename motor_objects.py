__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton


class BeltsController:
    _sharp_turn_dur = 0.35
    _default_speed = 0.4
    _sharp_turn_speed = 0.6

    def __init__(self):
        self.motor = Motors()
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):
        self.motor.set_value([-self._sharp_turn_speed, self._sharp_turn_speed], self._sharp_turn_dur)

    def sharp_right(self):
        self.motor.set_value([self._sharp_turn_speed, -self._sharp_turn_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        self.motor.backward(speed=self._default_speed, dur=dur)

    def forward(self, dur=None):
        self.motor.forward(speed=self._default_speed, dur=dur)

    def turn_left(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.tilt_left()

    def turn_right(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.tilt_right()

    def random(self, rand_int):
        self.motor.set_value([self._default_speed * rand_int, self._default_speed * rand_int])

    def stop(self):
        self.motor.stop()

    def operationalize(self):
        for (func, args) in self.value:
            print(func)
            print(*args)
            func(*args)
