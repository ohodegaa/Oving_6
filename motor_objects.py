__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton

class BeltsController:
    _sharp_turn_dur = 0.6
    _default_speed = 0.6

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

    def turn_left(self, degree):
        self.motor.set_value([self._default_speed * (1 - degree), self._default_speed])

    def turn_right(self, degree):
        self.motor.set_value([self._default_speed, self._default_speed * (1 - degree)])

    def random(self, rand_int):
        self.motor.set_value([self._default_speed*rand_int, self._default_speed*rand_int])

    def operationalize(self):
        for (func, args) in self.value:
            func(*args)
"""
def main():
    belts = BeltsController()
    ZumoButton().wait_for_press()
    belts.update([(belts.turn_left, [1.0]), (belts.turn_right, [1.0])])

main()
"""