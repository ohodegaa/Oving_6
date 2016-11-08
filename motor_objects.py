__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton


class BeltsController:
    _sharp_turn_dur = 0.8
    _default_speed = 0.4

    def __init__(self):
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):

        #self.motor.set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)
        Motors().set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)

    def sharp_right(self):
        #self.motor.set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)
        Motors().set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        Motors().set_value([-self._default_speed, -self._default_speed], dur)

    def forward(self, dur=None):
        Motors().set_value([self._default_speed, self._default_speed], dur)

    def set_value(self, left_val, right_val):
        print("left: ", left_val)
        print("Right: ", right_val)
        #self.motor.set_value([left_val*self._default_speed, right_val*self._default_speed])
        Motors().set_value([left_val * self._default_speed, right_val * self._default_speed])

    def random(self, rand_int):
        Motors().set_value([self._default_speed * rand_int, self._default_speed * rand_int])

    def stop(self):
        Motors().set_value([0, 0])

    def operationalize(self):
        for (func, args) in self.value:
            print(func)
            print(*args)
            func(*args)
