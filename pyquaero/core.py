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

import pyquaero.backend


class Aquaero:
    """Main class for communication with an Aquaero device.

    Its intention is to return an easy to use API and hide all firmware and communication
    related stuff from the invoker.
    """

    def __init__(self, unit=0):
        """Create a new Aquaero instance for the given unit."""
        from .struct.serializer import create_serializer
        self.backend = pyquaero.backend.Backend(unit)
        self.firmware = self.backend.get_firmware()
        self.structure = self.backend.get_structure()
        self.serializer = create_serializer(self.structure, self.firmware)

    def __enter__(self):
        return self

    def __exit__(self, exType, exValue, exTrackback):
        self.close()

    def close(self):
        """Close the Aquaero connection, releasing all resources. Must be invoked."""
        self.backend.close()

    def set_time(self, time=None):
        """Set the given (or current) time."""
        if self.firmware < 1036:
            raise RuntimeError('Firmware 1036 or higher is required for setting the time')
        from datetime import datetime
        if time is None:
            time = datetime.utcnow()
        self.backend.write_time(time)

    def get_status(self):
        """Get the current status of the Aquaero device."""
        status = self.serializer.read_status(self.backend)
        return self.serializer.unpack_status(status)

    def get_settings(self):
        """Get the current settings."""
        settings = self.serializer.read_settings(self.backend)
        return self.serializer.unpack_settings(settings)

    def get_strings(self):
        """Get the strings currently set."""
        strings = self.serializer.read_strings(self.backend)
        return self.serializer.unpack_strings(strings)
