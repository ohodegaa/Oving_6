__author__ = 'ohodegaa'

from wrappers.motors import Motors


class BeltsController:
    _sharp_turn_dur = 0.6
    _default_speed = 0.6

    def __init__(self):
        self.belts = Motors()
        self.value = None  # [(function, *args)...]

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()

    def sharp_left(self):
        self.belts.set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)

    def sharp_right(self):
        self.belts.set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        self.belts.set_value([-self._default_speed, -self._default_speed], dur)

    def forward(self, dur=None):
        self.belts.set_value(([self._default_speed, self._default_speed], dur))



    def operationalize(self):
        for func, args in self.value:
            func(*args)
            self.belts.right(speed=0.6, dur=5)

def main():
    bc = BeltsController()
    bc.update([(bc.forward, [5])])


if __name__ == '__main__':
    main()