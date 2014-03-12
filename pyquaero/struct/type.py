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
import struct


class AquaType:
    """Abstract superclass for all kind of type descriptors."""
    def __init__(self, at, step=0):
        self.at = at
        self.step = step

    def get(self, data, index=0):
        pos = self.at + (index * self.step)
        return self.fetch(data, pos)

    def fetch(self, data, pos):
        raise NotImplementedError()

class UnsignedByte(AquaType):
    """An unsigned byte (8 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>B', data[pos : pos + 1])[0]

class SignedByte(AquaType):
    """A signed byte (8 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>b', data[pos : pos + 1])[0]

class UnsignedWord(AquaType):
    """An unsigned word (16 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>H', data[pos : pos + 2])[0]

class SignedWord(AquaType):
    """A signed word (16 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>h', data[pos : pos + 2])[0]

class UnsignedLong(AquaType):
    """An unsigned long (32 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>L', data[pos : pos + 4])[0]

class SignedLong(AquaType):
    """A signed long (32 bits)."""
    def fetch(self, data, pos):
        return struct.unpack('>l', data[pos : pos + 4])[0]

class Boolean(AquaType):
    """A boolean (bit in a byte)."""
    def __init__(self, at, mask=None, step=0):
        AquaType.__init__(self, at, step)
        self.mask = mask

    def fetch(self, data, pos):
        val = data[pos]
        if self.mask:
            val &= self.mask
        return val != 0

class Color(AquaType):
    """A color (3 words as RGB)."""
    def fetch(self, data, pos):
        colors = struct.unpack('>HHH', data[pos : pos + 6]);
        colors = list(int(x * 255 / 10000) for x in colors)
        # TODO: tuple instead of #RRGGBB
        return ('#%02X%02X%02X' % (colors[0], colors[1], colors[2]))

class Uptime(UnsignedLong):
    """An uptime as datetime.timedelta."""
    def fetch(self, data, pos):
        val = UnsignedLong.fetch(self, data, pos)
        return datetime.timedelta(seconds=val)

class Percent(UnsignedWord):
    """A percentage value between 0 (off) and 100 (full)."""
    def fetch(self, data, pos):
        val = UnsignedWord.fetch(self, data, pos)
        return val / 100.0

class Time(Uptime):
    """A timestamp as datetime.datetime."""
    epoch = datetime.datetime(2009, 1, 1)
    def fetch(self, data, pos):
        val = Time.epoch + Uptime.fetch(self, data, pos)
        return val

class Level(SignedWord):
    """A level as percentage value, or None if not available."""
    undefined = 0x7fff
    def fetch(self, data, pos):
        val = SignedWord.fetch(self, data, pos)
        return val / 100.0 if val < Level.undefined else None

class Temperature(SignedWord):
    """A temperature, or None if not available."""
    undefined = 0x7fff
    def fetch(self, data, pos):
        val = SignedWord.fetch(self, data, pos)
        return val / 100.0 if val < Temperature.undefined else None

class Fraction(SignedWord):
    """A fraction with the given divisor."""
    def __init__(self, at, divisor=1.0, step=0):
        SignedWord.__init__(self, at, step)
        self.divisor = divisor

    def fetch(self, data, pos):
        val = SignedWord.fetch(self, data, pos)
        return val / self.divisor

class CurveTemperatures(AquaType):
    """Unpack temperatures of a curve to an array."""
    undefined = 0x7fff
    def __init__(self, at, items, step=0):
        AquaType.__init__(self, at, step)
        self.items = items

    def fetch(self, data, pos):
        data = struct.unpack('>%dh' % self.items, data[pos : pos + (self.items * 2)])
        mapper = lambda val: val / 100.0 if val < Temperature.undefined else None
        data = list(map(mapper, data))
        return data

class CurvePercents(AquaType):
    """Unpack percents of a curve to an array."""
    def __init__(self, at, items, step=0):
        AquaType.__init__(self, at, step)
        self.items = items

    def fetch(self, data, pos):
        data = struct.unpack('>%dH' % self.items, data[pos : pos + (self.items * 2)])
        data = [x / 100.0 for x in data]
        return data

class Mapped(AquaType):
    """A byte with its value mapped to strings."""
    def __init__(self, at, values, mask=None, step=0):
        AquaType.__init__(self, at, step)
        self.values = values
        self.mask = mask

    def fetch(self, data, pos):
        val = struct.unpack('>b', data[pos : pos + 1])[0]
        if self.mask:
            val &= self.mask
        if val in self.values:
            return self.values[val]
        else:
            return '?%d?' % val

class Group:
    """A group containing a sub-scheme."""
    def __init__(self, scheme):
        self.scheme = scheme

    def get(self, data):
        result = {}
        for key, converter in self.scheme.items():
            result[key] = converter.get(data)
        return result

class Array:
    """An array containing a given number of items."""
    def __init__(self, items, scheme):
        self.items = items
        self.scheme = scheme

    def get(self, data):
        result = []
        for ix in range(self.items):
            result.append({})
            for key, converter in self.scheme.items():
                result[ix][key] = converter.get(data, index=ix)
        return result

