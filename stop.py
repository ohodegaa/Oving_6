__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton


m = Motors()
print("stop")
ZumoButton().wait_for_press()
m.stop()