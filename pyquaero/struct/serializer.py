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

import datetime
import json


class AquaSerializer:
    """An abstract class for serializing and deserializing data packages.

    There are implementations for different ranges of firmware versions, to reflect
    new properties or different offsets.
    """

    def unpack_status(self, data):
        """Unpack a status package."""
        raise NotImplementedError()

    def unpack_settings(self, data):
        """Unpack a settings package."""
        raise NotImplementedError()

def create_serializer(structure, firmware):
    """Create an AquaSerializer instance for the given structure and firmware version."""
    if structure == 1013 and 1028 <= firmware <= 1030:
        from .struct1013 import AquaSerializer1013Fw1030
        return AquaSerializer1013Fw1030()

    if structure == 1013 and firmware > 1030:
        from .struct1013 import AquaSerializer1013
        return AquaSerializer1013()

    if structure == 1200 and 2007 <= firmware <= 2099:
        from .struct1200 import AquaSerializer1200Fw2007
        return AquaSerializer1200Fw2007()

    if structure == 1200:
        from .struct1200 import AquaSerializer1200
        return AquaSerializer1200()

    raise LookupError('firmware version %d (structure version %d) is not supported' % (firmware, structure))



class AquaJSONEncoder(json.JSONEncoder):
    """A json.JSONEncoder that is able to generate JSON output for all AquaType."""
    def default(self, obj):
        if isinstance(obj, datetime.timedelta):
            return int(obj.total_seconds())
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def from_json(text):
    """Convert JSON to an unserialized dictionary."""
    return json.loads(text)

def to_json(result, indent=None):
    """Convert an unserialized dictionary to JSON."""
    return json.dumps(result, indent=indent, cls=AquaJSONEncoder, sort_keys=True)
