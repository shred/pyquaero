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

from array import array
from datetime import datetime
import struct
import random


class Backend:
    """Backend that connects to the Aquaero device and offers a set of mid level
    operations.

    This class is threadsafe. Multiple threads can share a Backend instance.
    """

    def __init__(self, unit=0):
        """Create a new Backend instance that is connected to the given Aquaero unit."""
        import threading
        import pyquaero.usb
        self.lock = threading.Lock()
        self.device = pyquaero.usb.get_device(unit)
        self.last_status_ts = None

    def close(self):
        """Close the Backend, releasing all resources. Must be invoked!"""
        self.device.close()

    def write_time(self, time):
        """Set the given time."""
        epoch = datetime(2009, 1, 1)
        seconds = int((time - epoch).total_seconds())
        with self.lock:
            self.device.send_report(6, struct.pack('>BBBI', 0x06, 0x90, 0x88, seconds))

    def read_status(self, max_age=0.0):
        """Read the current status.

        The last status is cached. If it is younger than max_age (in seconds), the cached
        status is returned instead.
        """
        with self.lock:
            if (self.last_status_ts is None
                or (datetime.now() - self.last_status_ts).total_seconds() >= max_age):
                self._cache_status(self.device.read_endpoint(709, endpoint=3))
            return self.last_status

    def _cache_status(self, status):
        """Cache a status."""
        self.last_status = status
        self.last_status_ts = datetime.now()

    def read_settings(self):
        """Read the current settings."""
        with self.lock:
            return self.device.receive_report(11, 2428)

    def read_strings(self):
        """Read the current set of strings."""
        return self.read_memory(0x0009c000, 0x1000)

    def read_memory(self, start, length):
        """Read a fragment from flash memory."""
        page_size = 0x0400
        data_size = page_size + 10 + 4
        rand_id = random.randrange(0, 0x10000)

        query = array('B')
        query.extend(struct.pack('>BBII', 0x09, 0x01, start, length))
        query.extend([0x00] * page_size)
        query.extend(struct.pack('>HH', rand_id, 0x0000))

        rand_id += 1

        with self.lock:
            self.device.send_report(9, query)

            result = array('B')
            while len(result) < length:
                data = self.device.read_endpoint(data_size, endpoint=3)
                if len(data) < data_size:
                    self._cache_status(data)
                    continue

                # check if this is the data package we expected
                pkg_count = struct.unpack('>H', data[-4:-2])[0]
                if pkg_count != rand_id:
                    continue

                result.extend(data[10:-4])
                rand_id += 1

        return result

    def get_firmware(self):
        """Get the firmware version of the Aquaero at the given AquaDevice."""
        from pyquaero.struct.type import Group, UnsignedWord
        with self.lock:
            status = self.device.read_endpoint(1024, endpoint=3)
        scheme = Group(scheme={'firmware_version': UnsignedWord(at=0x000b)})
        return scheme.get(status)['firmware_version']

