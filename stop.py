__author__ = 'ohodegaa'

from wrappers.motors import Motors
from zumo_button import ZumoButton

def main():
    m = Motors()
    ZumoButton().wait_for_press()
    m.stop()

if __name__ == '__main__':
    main()