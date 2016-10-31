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

        #self.current_timestep = 0
        self.inactive_behaviors = []
        #self.controlled_robot = ""

    def add_behavior(self, behavior):
        """
        Adds a behavior object to the behaviors list
        :param behavior: Behavior-object
        :return:
        """
        self.behaviors.append(behavior)
        self.inactive_behaviors.append(behavior)

    def add_sensob(self, sensob):
        """
        Adds a sensob object to the sensob list
        :param sensob: Sensob object
        :return:
        """
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        """
        Activates a behavior
        :param behavior: Behavior object
        :return:
        """
        self.active_behaviors.append(self.inactive_behaviors.pop(self.inactive_behaviors.index(behavior)))

    def deactivate_behavior(self, behavior):
        """´
        Deactivates a behavior
        :param behavior: Behavior object
        :return:
        """
        self.inactive_behaviors.append(self.active_behaviors.pop(self.active_behaviors.index(behavior)))

