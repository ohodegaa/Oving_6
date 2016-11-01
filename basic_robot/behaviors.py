__author__ = 'ohodegaa'

from basic_robot import camera, imager2, irproximity_sensor, reflectance_sensors, ultrasonic
from robotic_controller import BBCON
from abc import ABCMeta, abstractmethod


class Behavior(metaclass=ABCMeta):
    def __init__(self, bbcon: BBCON, priority):
        self.bbcon = bbcon
        self.sensobs = bbcon.sensobs
        self.active_flag = True
        self.motor_recomendations = {} #dict[key:motob function, val:function args]
        self.halt_request = False
        self.priority = priority
        self.match_degree = 1
        self.weigth = self.priority * self.match_degree

    @abstractmethod
    def consider_deactivation(self):
        pass

    @abstractmethod
    def consider_activation(self):
        pass

    @abstractmethod
    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

    @abstractmethod
    def sense_and_act(self):
        pass



