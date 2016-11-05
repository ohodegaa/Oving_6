__author__ = 'ohodegaa'

from arbitrator import Arbitrator
from behaviors import Behavior
from motor_objects import BeltsController

class BBCON:


    def __init__(self):
        """
        Initiates the Behavior-Based Robotic Controller
        :param arbitrator: arbitrator, will provide behaviors?
        """
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []

        self.sensobs = []
        self.motobs = []
        self.belts = BeltsController()


        self.arbitrator = Arbitrator()

        self.current_timestep = 0
        self.controlled_robot = "Zumo Robot"

    def add_behavior(self, behavior):
        """
        Adds a behavior object to the behaviors list
        :param behavior: Behavior-object
        :return:
        """
        self.behaviors.append(behavior)
        self.inactive_behaviors.append(behavior)

    def add_sensob(self, sensob):
        """
        Adds a sensob object to the sensob list
        :param sensob: Sensob object
        :return:
        """
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior: Behavior):
        """
        Activates a behavior
        :param behavior: Behavior object
        :return:
        """
        self.active_behaviors.append(self.inactive_behaviors.pop(self.inactive_behaviors.index(behavior)))

    def deactivate_behavior(self, behavior):
        """
        Deactivates a behavior
        :param behavior: Behavior object
        :return:
        """
        self.inactive_behaviors.append(self.active_behaviors.pop(self.active_behaviors.index(behavior)))

    def update_all_sensobs(self):
        """
        Updates all sensob-objects by calling senob.update on all
        :return:
        """
        for sensob in self.active_behaviors:
            sensob.update()

    def update_all_behaviors(self):
        """
        Updates all behaviors
        :return:
        """
        self.update_all_sensobs()

        for behavior in self.active_behaviors:
            behavior.update()

    def choose_action(self):
        """
        Calls arbitrator.choose_action, which returns motor_recom (dict[key: motor object, value: motor settings])
        :return:
        """
        motor_recom, self.halt_request = self.arbitrator.choose_action()
        self.fire_motors(motor_recom)

    @staticmethod
    def fire_motors(motor_recom: dict):
        for motob, setting in motor_recom.items():
            motob.set(setting)

    def wait(self, dur=0):
        pass

    def reset_sensobs(self):
        for sensob in self.sensobs:
            sensob.reset()

    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviors()
        self.choose_action()
        self.wait()
        self.reset_sensobs()

    def restart(self):
        """
        Inits a new robot session
        :return:
        """

        pass