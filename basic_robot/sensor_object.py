__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod
from wrappers.reflectance_sensors import ReflectanceSensors
from wrappers.camera import Camera
from wrappers.irproximity_sensor import IRProximitySensor
from wrappers.ultrasonic import Ultrasonic


class SensorObject(metaclass=ABCMeta):
    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.set_value()

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()

    @abstractmethod
    def set_value(self):
        pass


class FloorSensor(SensorObject):
    def __init__(self):
        super().__init__()
        auto = True
        self.limit = 0.5
        self.sensors.append(ReflectanceSensors(auto_calibrate=auto))
        self.floor_sensor = self.sensors[0]

    def set_value(self):
        self.value = self.get_bool_array(self.floor_sensor.get_value, self.limit)

    @staticmethod
    def get_bool_array(sensor_array, limit):
        return [val < limit for val in sensor_array]

    @staticmethod
    def get_tuple(sensor_array, limit):
        length = 0
        temp_length = -1
        left = -1
        temp_left = -1
        for i in range(len(sensor_array)):
            if sensor_array[i] < limit:
                if temp_length == -1:
                    temp_left = i
                temp_length += 1
            else:
                if temp_length > length:
                    length = temp_length
                    left = temp_left
                temp_length = -1
        if temp_length >= length:
            length = temp_length
            left = temp_left
        elif temp_left == -1:
            length = 0
        return left, left + length


class SideSensor(SensorObject):
    def __init__(self):
        super().__init__()
        self.sensors.append(IRProximitySensor())
        self.side_sensor = self.sensors[0]

    def set_value(self):
        self.value = self.side_sensor.get_value()


class FrontSensor(SensorObject):
    def __init__(self):
        super().__init__()
        self.sensors.append(Ultrasonic())
        self.front_sensor = self.sensors[0]

    def set_value(self):
        self.value = self.front_sensor.get_value()