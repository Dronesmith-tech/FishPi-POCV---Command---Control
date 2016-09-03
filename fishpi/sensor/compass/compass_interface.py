#
# FishPi - An autonomous drop in the ocean
#
# Tilt-compensated Compass driver for the LSM303

import logging
from math import atan2, sqrt, sin, cos, pi
from math import pow as fpow

# import hw_platform
from dronekit import *

#from Adafruit_LSM303 import Adafruit_LSM303


class Compass(object):

    def __init__(self, interface="", fmu=Vehicle, hw_interface="-1", debug=False,
            hires="False"):
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        self.device_handler = fmu

        print "[IMU] VERIFICATION TEST."
        print self.read_sensor()

    def tear_down(self):
        logging.info("COMP:\tTear-down complete, " +
                "nothing to be done.")

    def read_sensor(self):
        heading = self.device_handler.attitude.yaw * (180.0 / 3.14159)
        pitch = self.device_handler.attitude.pitch * (180.0 / 3.14159)
        roll = self.device_handler.attitude.roll * (180.0 / 3.14159)

        return heading, pitch, roll


if __name__ == "__main__":
    print("This is the tilt-compensated compass data handler.")
    from time import sleep
    compass = Compass()
    while True:
        heading, pitch, roll = compass.read_sensor()
        print("Heading: %f, Pitch: %f, Roll: %f" % heading, pitch, roll)
        sleep(0.5)
