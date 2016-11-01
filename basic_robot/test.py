__author__ = 'ohodegaa'

from robotic_controller import BBCON
from time import sleep
import random
import imager2 as IMR
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton

def main():
    bbcon = BBCON()
    m = Motors()
    m.forward(0.5, 2)