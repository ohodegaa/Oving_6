__author__ = 'ohodegaa'

from wrappers.motors import Motors
from time import sleep
from zumo_button import ZumoButton

m = Motors()
sleep(1.0)
ZumoButton.wait_for_press()
m.stop()
print("stopped")
