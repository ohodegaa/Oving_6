__author__ = 'ohodegaa'

from wrappers.motors import Motors
from time import sleep

m = Motors()
sleep(1.0)
m.stop()
print("stopped")
