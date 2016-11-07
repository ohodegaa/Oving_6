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
        self.motor.set_value([self._default_speed * (1 - degree), self._default_speed], dur=3)

    def turn_right(self, degree):
        self.motor.set_value([self._default_speed, self._default_speed * (1 - degree)], dur=3)

    def operationalize(self):
        for (func, args) in self.value:
            print(*args)
            func(*args)

def main():
    belts = BeltsController()
    ZumoButton().wait_for_press()
    belts.update([(belts.turn_left, [0.99])])

main()