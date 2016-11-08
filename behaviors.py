__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod

from robotic_controller import BBCON
from sensor_object import *
from random import randint


class Behavior(metaclass=ABCMeta):
    def __init__(self, bbcon: BBCON, priority: float):
        self.bbcon = bbcon
        self.active_flag = True
        self.motor_recommendations = {}  # dict[key:motob object, val: [(motob function, [arg1, arg2..]), (...)]
        self.halt_request = False
        self.priority = priority
        self.match_degree = 1
        self.motor = self.bbcon.belts
        self.weight = self.priority * self.match_degree
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
        self.weight = self.priority * self.match_degree

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
        if self.floor_sensor is None:
            print("Floor sensos not found")

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def gather_sensor_values(self):
        print("floor_sensor.get_value", self.floor_sensor.get_value())
        self.sensor_value = self.floor_sensor.get_value()

    def sense_and_act(self):
        # produce motor recommendations

        check = [
            self.sensor_value[2] and self.sensor_value[3],
            self.sensor_value[2], self.sensor_value[3],
            self.sensor_value[1], self.sensor_value[4],
            self.sensor_value[0], self.sensor_value[5]
        ]

        motor_action = [
            (self.motor.forward, []),
            (self.motor.set_value, [0.8, 1.0]), (self.motor.set_value, [1.0, 0.8]),
            (self.motor.set_value, [0.4, 1.0]), (self.motor.set_value, [1.0, 0.4]),
            (self.motor.sharp_left, []), (self.motor.sharp_right, [])
        ]

        for i in range(len(check)):
            if check[i]:
                self.motor_recommendations = {self.motor, motor_action[i]}
                break
        self.weight = self.match_degree * self.priority


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

        self.motor_recommendations = {self.motor: [motor_action]}
        self.weight = self.match_degree * self.priority


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
        sets the field motor_recommendations to a new value
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
        sets the field motor_recommendations to a new value
        :return: None
        """

    def sense_and_act(self):
        if self.sensor_value is True:
            motor_action = (self.motor.forward, [])
            self.match_degree = 0.6
        else:
            self.consider_deactivation()

        self.motor_recomendations = {self.motor: [motor_action]}
        self.weigth = self.match_degree * self.priority
