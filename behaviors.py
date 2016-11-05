__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod

from robotic_controller import BBCON
from wrappers.reflectance_sensors import ReflectanceSensors as RefSens


class Behavior(metaclass=ABCMeta):
    def __init__(self, bbcon: BBCON, priority:float):
        self.bbcon = bbcon
        self.active_flag = True
        self.motor_recomendations = {}  # dict[key:motob function, val:function args]
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
    def sense_and_act(self):
        pass

    def update_weight(self):
        self.weigth = self.priority*self.match_degree

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()
            self.update_weight()



class FollowLine(Behavior):

    def __init__(self, bbcon:BBCON, priority:float):
        super().__init__(bbcon, priority)
        self.sensobs = RefSens(auto_calibrate=True)
        self.sensor_readings = []

    def consider_activation(self):
        if any(val for val in self.sensor_readings):
            self.bbcon.activate_behavior(self)

    def consider_deactivation(self):
        if not any(val for val in self.sensor_readings):
            self.bbcon.deactivate_behavior(self)



