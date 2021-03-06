__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod

from robotic_controller import BBCON
from sensor_object import *
from random import randint
from imager2 import *


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

        self.motor_recommendations = {self.motor: [(self.motor.forward, [0.1])]}

        check = [
            self.sensor_value[2] and self.sensor_value[3],
            self.sensor_value[2], self.sensor_value[3],
            self.sensor_value[1], self.sensor_value[4],
            self.sensor_value[0], self.sensor_value[5]
        ]
        motor_action = [
            (self.motor.forward, []),
            (self.motor.turn_left, [0.5]), (self.motor.turn_right, [0.5]),
            (self.motor.turn_left, [0.8]), (self.motor.turn_right, [0.8]),
            (self.motor.sharp_left, []), (self.motor.sharp_right, [])
        ]

        for i in range(len(check) - 1, -1, -1):
            if check[i]:
                if i > 4:
                    self.match_degree = 1.0
                elif i > 2:
                    self.match_degree = 0.8
                else:
                    self.match_degree = 0.5
                self.motor_recommendations = {self.motor: [motor_action[i]]}
                break


class AvoidObject(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.front_sensor = None
        self.camera = None
        self.color_limit = 0.50
        self.motor_recommendations = {self.motor: [(self.motor.forward, [])]}
        for sensOb in bbcon.sensobs:
            if isinstance(sensOb, FrontSensor):
                self.front_sensor = sensOb
            if isinstance(sensOb, CameraSensor):
                self.camera = sensOb

    def gather_sensor_values(self):
        self.sensor_value = self.front_sensor.get_value()

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def analyze_image(self, image):
        image = Imager(image=image)
        image_percentages = []
        for y in range(image.ymax):
            for x in range(image.xmax):
                pixels = image.get_pixel(x, y)
                try:
                    image_percentages.append(pixels[0] / sum(pixels))
                except:
                    pass

        red_mean = sum(image_percentages) / len(image_percentages)
        print("red:", red_mean)
        return red_mean

    def sense_and_act(self):
        if self.sensor_value < 20:
            print("Object detected")
            self.motor.stop()
            self.match_degree = 1
            image = self.camera.get_image()
            red_value = self.analyze_image(image)
            if red_value > self.color_limit:
                self.motor_recommendations = {self.motor: [(self.motor.backwards, [0.05]), (self.motor.full_turn, []),
                                                           (self.motor.forward, [0.05])]}
            else:
                self.motor_recommendations = {self.motor: [(self.motor.forward, [2.5]), (self.motor.backwards, [2.5])]}
        else:
            self.match_degree = 0.1
            self.motor_recommendations = {self.motor: [(self.motor.forward, [])]}



class SideSight(Behavior):
    def __init__(self, bbcon: BBCON, priority: float):
        super().__init__(bbcon, priority)
        self.side_sensor = None

        for senOb in bbcon.sensobs:
            if isinstance(senOb, SideSensor):
                self.side_sensor = senOb
                break

    def consider_activation(self):
        pass

    def consider_deactivation(self):
        pass

    def gather_sensor_values(self):
        self.sensor_value = self.side_sensor.get_value()

    def sense_and_act(self):
        right = True
        if self.sensor_value[0]:
            right = False
        elif self.sensor_value[1]:
            right = True
        else:
            self.motor_recommendations = {self.motor: [(self.motor.random, [])]}
            return
        self.match_degree = 0.8
        turn = (self.motor.sharp_right, [0.25]) if right else (self.motor.sharp_left, [0.25])
        forward = (self.motor.forward, [1])
        backwards = (self.motor.backwards, [1])
        turn_back = (self.motor.sharp_left, [0.25]) if right else (self.motor.sharp_right, [0.25])

        self.motor_recommendations = {self.motor: [turn, forward, backwards, turn_back]}
