#
# pyquaero - a Python library for Aquaero fan controllers
#
# Copyright (C) 2014 Richard "Shred" Körber
#   https://github.com/shred/pyquaero
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'Richard "Shred" Körber'

import usb.core
import usb.util


VENDOR_ID = 0x0c70
PRODUCT_ID = 0xf001

class AquaDevice(object):
    """Aquaero USB device object.

    Connect to the Aquaero via USB and offer a set of low level access methods that
    are firmware independent.
    """

    def __init__(self, dev):
        """Initialize the AquaDevice object."""
        self.dev = dev
        self.interface = [self.dev[0][(x, 0)] for x in range(3)]

        # claim the interfaces if held by the kernel
        for intf in self.interface:
            if dev.is_kernel_driver_active(intf.bInterfaceNumber):
                self.dev.detach_kernel_driver(intf.bInterfaceNumber)
                usb.util.claim_interface(self.dev, intf)

    def close(self):
        """Close the AquaDevice object after usage.

        Must be invoked to properly release the USB device!
        """
        for intf in self.interface:
            usb.util.release_interface(self.dev, intf)
            self.dev.attach_kernel_driver(intf.bInterfaceNumber)

    def send_report(self, reportId, data, wIndex=2):
        """Send a USBHID OUT report request to the AquaDevice."""
        self.dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09,
                               wValue=(0x0200 | reportId), wIndex=wIndex,
                               data_or_wLength=data)

    def receive_report(self, reportId, length, wIndex=2):
        """Send a USBHID IN report request to the AquaDevice and receive the answer."""
        return self.dev.ctrl_transfer(bmRequestType=0xa1, bRequest=0x01,
                               wValue=(0x0300 | reportId), wIndex=wIndex,
                               data_or_wLength=length)

    def write_endpoint(self, data, endpoint):
        """Send a data package to the given endpoint."""
        ep = self.interface[endpoint - 1][0]
        ep.write(data)

    def read_endpoint(self, length, endpoint):
        """Reads a number of data from the given endpoint."""
        ep = self.interface[endpoint - 1][0]
        return ep.read(length)


def count_devices():
    """Count the number of Aquaero devices found."""
    devices = list(usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID, find_all=True))
    return len(devices)

def get_device(unit=0):
    """Return an AquaDevice instance for the given Aquaero device unit found."""
    devices = list(usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID, find_all=True))
    if unit >= len(devices):
        raise IndexError('No Aquaero unit %d found' % unit)
    return AquaDevice(devices[unit])
