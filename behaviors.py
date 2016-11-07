__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod

from robotic_controller import BBCON
from sensor_object import *
from random import randint


class Behavior(metaclass=ABCMeta):
    def __init__(self, bbcon: BBCON, priority: float):
        self.bbcon = bbcon
        self.active_flag = True
        self.motor_recomendations = {}  # dict[key:motob object, val: [(motob function, [arg1, arg2..]), (...)]
        self.halt_request = False
        self.priority = priority
        self.match_degree = 1
        self.motor = self.bbcon.belts
        self.weigth = self.priority * self.match_degree
        self.sensor_value = None

    @abstractmethod
    def gather_sensor_values(self):
        pass

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
        self.weigth = self.priority * self.match_degree

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.gather_sensor_values()
            self.sense_and_act()
            self.update_weight()


class FollowLine(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.floor_sensor = None
        for senOb in bbcon.sensobs:
            if isinstance(senOb, FloorSensor):
                self.floor_sensor = senOb
                break

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def gather_sensor_values(self):
        self.sensor_value = self.floor_sensor.get_value()

    def sense_and_act(self):
        # produce motor recommendations
        left = 0
        right = 0
        for i in range(len(self.sensor_value) // 2):
            if self.sensor_value[i]:
                left += 1
            if self.sensor_value[-i - 1]:
                right += 1

        if left != right:
            if left > right:
                motor_action = self.motor.turn_right
                if self.sensor_value[0]:
                    self.match_degree = 0.9
                else:
                    self.match_degree = 0.5
            else:
                motor_action = self.motor.turn_left
                if self.sensor_value[5]:
                    self.match_degree = 0.9
                else:
                    self.match_degree = 0.5

            self.motor_recomendations = {self.motor: (motor_action, [self.match_degree])}

        elif left == 0 and right == 0:
            motor_action = self.motor.random
            self.match_degree = 0.8
            self.motor_recomendations = {self.motor: (motor_action, [randint(0, 1)])}

        else:
            motor_action = self.motor.forward
            self.match_degree = 0.4
            self.motor_recomendations = {self.motor: (motor_action, [0.8])}

        self.weigth = self.match_degree * self.priority


class AvoidObject(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.front_sensor = None
        for sensOb in bbcon.sensobs:
            if isinstance(sensOb, FrontSensor):
                self.FrontSensor = sensOb

    def gather_sensor_values(self):
        self.sensor_value = self.front_sensor.get_value()

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def sense_and_act(self):
        if self.sensor_value < 7:
            motor_action = (self.motor.sharp_left, [])
            self.match_degree = 0.9
        else:
            motor_action = (self.motor.random, [randint(0, 1)])
            self.match_degree = 0.4

        self.motor_recomendations = {self.motor: motor_action}
        self.weigth = self.match_degree * self.priority


class Camera(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.camera = None
        for senOb in bbcon.sensobs:
            if isinstance(senOb, Camera):
                self.camera = senOb

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def gather_sensor_values(self):
        self.sensor_value = self.camera.get_value()

    def update(self):
        """
        sets the field motor_recomendations to a new value
        :return: None
        """

    def sense_and_act(self):
        # produce motor recommendations
        pass


class FollowWall(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.side_sensor = None
        for senOb in bbcon.sensobs:
            if isinstance(senOb, SideSensor):
                self.side_sensor = senOb

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def gather_sensor_values(self):
        self.sensor_value = self.side_sensor.get_value()

    def update(self):
        """
        sets the field motor_recomendations to a new value
        :return: None
        """

    def sense_and_act(self):
        # produce motor recommendations
        pass
