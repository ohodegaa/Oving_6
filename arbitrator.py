__author__ = 'ohodegaa'

import random
from behaviors import Behavior

class Arbitrator:
    rec_dict = {}
    #Liste med vekting av farward, backward, left, right
    def choose_action(self):
        choice = 'random'
        if choice == 'random':
            self.stochastic()
        else:
            self.deterministic()

    def stochastic(self):
        return random.choice(list(self.rec_dict.keys()))

    def deterministic(self):
        max_value = 0
        key_name  = ''
        for key, value in self.rec_dict.items():
            if value > max_value:
                max_value = value
                key_name = key

        return key_name
