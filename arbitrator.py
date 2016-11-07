__author__ = 'ohodegaa'

import random
from behaviors import Behavior

class Arbitrator:
    def __init__(self, bbcon):
        """
        referance to the bbcon object that holds the arbitrator
        :param bbcon:
        """
        self.bbcon = bbcon
        self.last_motor_rec = None
        self.last_weight = None
        self.last_behaviour = None

    #Liste med vekting av forward, backward, left, right
    def choose_action(self, choice = "deterministic"):
        """
        chooses which recomendation that is most important from bbcons behaviours
        :param choice:
        :return:
        """
        max_weight = 0
        best_behaviour = None

        for behaviour in self.bbcon.behaviors:
            if behaviour.weight > max_weight:
                best_behaviour = behaviour

        self.last_behaviour = best_behaviour
        self.last_motor_rec = best_behaviour.motor_recomendations
        self.last_weight = best_behaviour.weight

        return best_behaviour



