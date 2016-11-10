__author__ = 'ohodegaa'

from abc import ABCMeta, abstractmethod
from wrappers.reflectance_sensors import ReflectanceSensors
from wrappers.camera import Camera
from wrappers.irproximity_sensor import IRProximitySensor
from wrappers.ultrasonic import Ultrasonic


class Sensor(metaclass=ABCMeta):
    def __init__(self):
        """
        Initiates a new Sensor object
        sensors: the sensor(s) used by the sensob
        value: the (return) value of the sensob, will be used by any behavior
        """
        self.sensors = []
        self.value = None
        self.active_flag = True

    @abstractmethod
    def update(self):
        """
        Updates the sensor and sets the sensob value
        :return:
        """
        pass

    def get_value(self):
        """
        Returns the sensob value
        :return: sensob value which will be used by any behavior
        """
        return self.value

    def reset(self):
        """
        Resets the sensor
        :return:
        """
        for sensor in self.sensors:
            sensor.reset()


class FloorSensor(Sensor):
    def __init__(self):
        """
        Initiates a new FloorSensor object
        auto: True indicates that sensors will be auto calibrated, False sets calibration to default, set by user
        limit: a sensor value below limit indicates a dark area, above indicates a bright area
        """
        super().__init__()
        auto = True
        self.sensors.append(ReflectanceSensors(auto_calibrate=auto))
        self.reflectance_sensor = self.sensors[0]
        self.limit = 0.6

    def update(self):
        self.value = self.get_bool_array(self.reflectance_sensor.update())
        # [sens0, sens1, sens2, sens3, sens4, sens5]


    def get_bool_array(self, sensor_array):
        """
        Generates an array with boolean values which indicates whether the sensor spotted an dark or bright area.
        -> True indicates a dark area, False indicates a bright area
        :param sensor_array: sensor readings
        :param limit: dark/bright -limit
        :return: an array with boolean values
        """
        return [val < self.limit for val in sensor_array]

    @staticmethod
    def get_tuple(sensor_array, limit):
        """
        Generates a tuple (a, b) which indicates that the largest dark area is spotted from sensor a to sensor b
        :param sensor_array: sensor readings
        :param limit: dark/bright -limit
        :return: a tuple
        """
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


class SideSensor(Sensor):
    def __init__(self):
        """
        Initiates a new SideSensor object
        """
        super().__init__()
        self.sensors.append(IRProximitySensor())
        self.side_sensor = self.sensors[0]

    def set_value(self):
        """
        Sets the sensob value to the sensor value [left, right].
        -> left/rigth is boolean values indicating whether obstacles are spotted on left/right side of the sumo
        :return:
        """
        self.value = self.side_sensor.get_value()


class FrontSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.sensors.append(Ultrasonic())
        self.front_sensor = self.sensors[0]

    def set_value(self):
        self.value = self.front_sensor.get_value()
        self.value = self.front_sensor.get_value()


class CameraSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.sensors.append(Camera())
        self.camera = self.sensors[0]
        self.image = None

    def get_image(self):
        self.image = self.camera.get_value()
        return self.image()


