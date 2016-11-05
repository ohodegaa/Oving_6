__author__ = 'ohodegaa'

from wrappers.motors import Motors


class BeltsController:

    _sharp_turn_dur = 0.6
    _default_speed = 0.6



    def __init__(self):
        self.motors = []
        self.motors.append(Motors())
        self.belts = self.motors[0]
        self.value = None
        self.recom = (BeltsController.forward, [2, 3, ])

    def update(self, recomendation):


    def sharp_left(self):
        self.belts.set_value([-self._default_speed, self._default_speed], self._sharp_turn_dur)

    def sharp_right(self):
        self.belts.set_value([self._default_speed, -self._default_speed], self._sharp_turn_dur)

    def backwards(self, dur=None):
        self.belts.set_value([-self._default_speed, -self._default_speed], dur)

    def forward(self, dur=None):
        self.belts.set_value(([self._default_speed, self._default_speed], dur))

    