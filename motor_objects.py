__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton


class BeltsController:
    _sharp_turn_dur = 0.5
    _default_speed = 0.3

    def __init__(self):
        self.motor = Motors()
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):
        self.motor.set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)

    def sharp_right(self):
        self.motor.set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        self.motor.set_value([-self._default_speed, -self._default_speed], dur)

    def forward(self, dur=None):
        self.motor.set_value([self._default_speed, self._default_speed], dur)

    def turn_left(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.left(speed=speed, dur=dur)

    def turn_right(self, speed=_default_speed, dur=_sharp_turn_dur):
        self.motor.right(speed=speed, dur=dur)

    def random(self, rand_int):
        self.motor.set_value([self._default_speed * rand_int, self._default_speed * rand_int])

    def stop(self):
        self.motor.set_value([0, 0])

    def operationalize(self):
        for (func, args) in self.value:
            print(func)
            print(*args)
            func(*args)
