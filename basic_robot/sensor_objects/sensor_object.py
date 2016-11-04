__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod
from wrappers.reflectance_sensors import ReflectanceSensors



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
        self.on_line = range(0.0, 0.5)
        self.off_line = range(0.5, 1.0)
        self.sensors.append(ReflectanceSensors(auto_calibrate=auto))
        self.floor_sensor = self.sensors[0]

    def set_value(self):
        self.set_bool_array()

    def set_bool_array(self):
        self.value = [(val in self.on_line) for val in self.floor_sensor.get_value()]

    def set_tuple(self):
        length = 0
        temp_length = -1
        left = -1
        temp_left = -1
        for i in range(len(self.floor_sensor.get_value())):
            if self.floor_sensor.get_value()[i] < 0.5:
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
        self.value = (left, left + length)