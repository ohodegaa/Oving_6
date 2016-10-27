__author__ = 'ohodegaa'

import basic_robot

class BBCON:


    def __init__(self, arbitrator):
        """
        Initiates the Behavior-Based Robotic Controller
        :param arbitrator: arbitrator, will provide behaviors?
        """
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = arbitrator

