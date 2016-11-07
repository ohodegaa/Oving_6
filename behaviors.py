__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod

from robotic_controller import BBCON
from wrappers.reflectance_sensors import ReflectanceSensors as RefSens
from sensor_object import *



class Behavior(metaclass=ABCMeta):
    def __init__(self, bbcon: BBCON, priority:float):
        self.bbcon = bbcon
        self.active_flag = True
        self.motor_recomendations = {}  # dict[key:motob object, val: [(motob function, (arg1, arg2..)), (...)]
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
        self.FloorSensor = None
        for senOb in bbcon:
            if isinstance(senOb, FloorSensor):
                self.FloorSensor = senOb

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def update(self):
        """
        sets the field motor_recomendations to a new value
        :return: None
        """

    def sense_and_act(self):
        #produce motor recommendations

        if self.sensor_readings[0] > 0.8:




class AvoidObject(Behavior):

    def __init__(self, bbcon:BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.FrontSensor = None

        for senOb in bbcon:
            if isinstance(senOb, FrontSensor):
                self.FrontSensor = senOb

        def consider_activation(self):
            pass

        def consider_deactivation(self):
            pass

        def sense_and_act(self):
            if self.


class Camera(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.sensobs = RefSens(auto_calibrate=True)
        self.sensor_readings = []
        self.FloorSensor = None
        for senOb in bbcon:
            if isinstance(senOb, FloorSensor):
                self.FloorSensor = senOb


    def consider_activation(self):
        pass


    def consider_deactivation(self):
        pass


    def update(self):
        """
        sets the field motor_recomendations to a new value
        :return: None
        """

    def sense_and_act(self):

    # produce motor recommendations

class sideSensors(Behavior):
    def __init__(self, bbcon:BBCON, priority:float):
        super().__init__(bbcon, priority)
        self.sensobs = RefSens(auto_calibrate=True)
        self.sensor_readings = []
        self.FloorSensor = None
        for senOb in bbcon:
            if isinstance(senOb, FloorSensor):
                self.FloorSensor = senOb

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def update(self):
        """
        sets the field motor_recomendations to a new value
        :return: None
        """

    def sense_and_act(self):
        #produce motor recommendations
