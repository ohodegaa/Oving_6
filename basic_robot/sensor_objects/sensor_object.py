__author__ = 'ohodegaa'

from abc import ABCMeta


class SensorObject(metaclass=ABCMeta):

    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        for sensor in self.sensors:
            sensor.update()

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


class FloorSensor(SensorObject):

    def __init__(self):
        super().__init__()
        self.sensors.append()
