#
# FishPi - An autonomous drop in the ocean
#
# HAL for Luci

import os
import logging
from dronekit import *

import hw_platform.hw_config as hw_config


class LuciSupport(object):
    """ Support package for Luci. Exports the overlays from the
        device tree for the used hardware """

    def __init__(self):
        # every support code has to set this to notify drivers on
        # which platform they are working.
        hw_config.platform = 'Luci'
        hw_config.default_ic2 = None

        os.system("LUCI: Connecting")
        self._fmu = connect("0.0.0.0:14551", wait_ready=True)

    def configure_interface(self, name):

        if name == "fmu":
            os.system("FMU Link")
        else:
            logging.error("Luci:\tInterface %s unknown.", name)
            return

        # It's basically just executing a shell command, that exports the
        # device. Each if/elif specifies a string that gets put into the exec
        # command that is issued at the end.

    # TODO: What's up with the different UART numbers here? 1,2,3,4 or 1,2,4,5?
    def lookup_interface(self, bus):
        return "0.0.0.0:14551"

    def getFmu(self):
        return self._fmu
