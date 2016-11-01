__author__ = 'ohodegaa'

from basic_robot import camera, imager2, irproximity_sensor, reflectance_sensors, ultrasonic
from robotic_controller import BBCON


class Behavior:

    def __init__(self, bbcon:BBCON, sensobs:list):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        pass

    def sense_and_act(self):
        pass

class Wander(Behavior):
    pass

class FollowRobot(Behavior):
    pass