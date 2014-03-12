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

from .serializer import AquaSerializer
from .type import *  # @UnusedWildImport


class DataSource(AquaType):
    """A word containing a data source."""
    sources = {
        - 1: None,
        0x00: 'sensor 1',
        0x01: 'sensor 2',
        0x02: 'sensor 3',
        0x03: 'sensor 4',
        0x04: 'sensor 5',
        0x05: 'sensor 6',
        0x06: 'sensor 7',
        0x07: 'sensor 8',
        0x08: 'sensor 9',
        0x09: 'sensor 10',
        0x0a: 'sensor 11',
        0x0b: 'sensor 12',
        0x0c: 'sensor 13',
        0x0d: 'sensor 14',
        0x0e: 'sensor 15',
        0x0f: 'sensor 16',
        0x10: 'soft sensor 1',
        0x11: 'soft sensor 2',
        0x12: 'soft sensor 3',
        0x13: 'soft sensor 4',
        0x14: 'soft sensor 5',
        0x15: 'soft sensor 6',
        0x16: 'soft sensor 7',
        0x17: 'soft sensor 8',
        0x18: 'virtual sensor 1',
        0x19: 'virtual sensor 2',
        0x1a: 'virtual sensor 3',
        0x1b: 'virtual sensor 4',
        0x2c: 'fan amp 1',
        0x2d: 'fan amp 2',
        0x2e: 'fan amp 3',
        0x2f: 'fan amp 4',
        0x30: 'fan amp 5',
        0x31: 'fan amp 6',
        0x32: 'fan amp 7',
        0x33: 'fan amp 8',
        0x34: 'fan amp 9',
        0x35: 'fan amp 10',
        0x36: 'fan amp 11',
        0x37: 'fan amp 12',
        0x38: 'cpu',
        0x40: 'target value controller 1',
        0x41: 'target value controller 2',
        0x42: 'target value controller 3',
        0x43: 'target value controller 4',
        0x44: 'target value controller 5',
        0x45: 'target value controller 6',
        0x46: 'target value controller 7',
        0x47: 'target value controller 8',
        0x48: 'two point controller 1',
        0x49: 'two point controller 2',
        0x4a: 'two point controller 3',
        0x4b: 'two point controller 4',
        0x4c: 'two point controller 5',
        0x4d: 'two point controller 6',
        0x4e: 'two point controller 7',
        0x4f: 'two point controller 8',
        0x50: 'two point controller 9',
        0x51: 'two point controller 10',
        0x52: 'two point controller 11',
        0x53: 'two point controller 12',
        0x54: 'two point controller 13',
        0x55: 'two point controller 14',
        0x56: 'two point controller 15',
        0x57: 'two point controller 16',
        0x58: 'curve controller 1',
        0x59: 'curve controller 2',
        0x5a: 'curve controller 3',
        0x5b: 'curve controller 4',
        0x5c: 'led red',
        0x5d: 'led blue',
        0x5e: 'led green',
        0x60: 'preset 1',
        0x61: 'preset 2',
        0x62: 'preset 3',
        0x63: 'preset 4',
        0x64: 'preset 5',
        0x65: 'preset 6',
        0x66: 'preset 7',
        0x67: 'preset 8',
        0x68: 'preset 9',
        0x69: 'preset 10',
        0x6a: 'preset 11',
        0x6b: 'preset 12',
        0x6c: 'preset 13',
        0x6d: 'preset 14',
        0x6e: 'preset 15',
        0x6f: 'preset 16',
        0x70: 'preset 17',
        0x71: 'preset 18',
        0x72: 'preset 19',
        0x73: 'preset 20',
        0x74: 'preset 21',
        0x75: 'preset 22',
        0x76: 'preset 23',
        0x77: 'preset 24',
        0x78: 'preset 25',
        0x79: 'preset 26',
        0x7a: 'preset 27',
        0x7b: 'preset 28',
        0x7c: 'preset 29',
        0x7d: 'preset 30',
        0x7e: 'preset 31',
        0x7f: 'preset 32',
        0x80: 'flow sensor 1',
        0x81: 'flow sensor 2',
        0x82: 'flow sensor 3',
        0x83: 'flow sensor 4',
        0x84: 'flow sensor 5',
        0x85: 'flow sensor 6',
        0x86: 'flow sensor 7',
        0x87: 'flow sensor 8',
        0x88: 'flow sensor 9',
        0x89: 'flow sensor 10',
        0x8a: 'flow sensor 11',
        0x8b: 'flow sensor 12',
        0x8c: 'flow sensor 13',
        0x8d: 'flow sensor 14',
        0x8e: 'fan speed 1',
        0x8f: 'fan speed 2',
        0x90: 'fan speed 3',
        0x91: 'fan speed 4',
        0x92: 'fan speed 5',
        0x93: 'fan speed 6',
        0x94: 'fan speed 7',
        0x95: 'fan speed 8',
        0x96: 'fan speed 9',
        0x97: 'fan speed 10',
        0x98: 'fan speed 11',
        0x99: 'fan speed 12',
        0xa6: 'fan voltage 1',
        0xa7: 'fan voltage 2',
        0xa8: 'fan voltage 3',
        0xa9: 'fan voltage 4',
        0xaa: 'fan voltage 5',
        0xab: 'fan voltage 6',
        0xac: 'fan voltage 7',
        0xad: 'fan voltage 8',
        0xae: 'fan voltage 9',
        0xaf: 'fan voltage 10',
        0xb0: 'fan voltage 11',
        0xb1: 'fan voltage 12',
        0xb2: 'fan current 1',
        0xb3: 'fan current 2',
        0xb4: 'fan current 3',
        0xb5: 'fan current 4',
        0xb6: 'fan current 5',
        0xb7: 'fan current 6',
        0xb8: 'fan current 7',
        0xb9: 'fan current 8',
        0xba: 'fan current 9',
        0xbb: 'fan current 10',
        0xbc: 'fan current 11',
        0xbd: 'fan current 12',
        0xc6: 'fill level 1',
        0xc7: 'fill level 2',
        0xc8: 'fill level 3',
        0xc9: 'fill level 4',
        0xca: 'power consumption 1',
        0xcb: 'power consumption 2',
        0xcc: 'power consumption 3',
        0xcd: 'power consumption 4',
    }
    def fetch(self, data, pos):
        val = struct.unpack('>h', data[pos : pos + 2])[0]
        if val in DataSource.sources:
            return DataSource.sources[val]
        else:
            return "?%d?" % val


class Action(AquaType):
    """A word containing an action."""
    actions = {
        - 1: None,
        0: 'speed signal generation on',
        1: 'speed signal generation off',
        2: 'alarm buzzer on',
        3: 'alarm buzzer off',
        4: 'alarm buzzer signal',
        5: 'alarm buzzer beep',
        6: 'relay on',
        7: 'relay off',
        8: 'relay switch 2 sec',
        9: 'relay switch 10 sec',
        10: 'load profile 1',
        11: 'load profile 2',
        12: 'load profile 3',
        13: 'load profile 4',
        14: 'keyboard power key',
        15: 'keyboard sleep key',
        16: 'keyboard wakeup key',
        17: 'keyboard play key',
        18: 'keyboard volume up key',
        19: 'keyboard volume down key',
        20: 'keyboard mute key',
    }
    def fetch(self, data, pos):
        val = struct.unpack('>h', data[pos : pos + 2])[0]
        if val in Action.actions:
            return Action.actions[val]
        else:
            return "?%d?" % val


class PageType(AquaType):
    """A byte containing a page type."""
    types = {
        0x00: 'logdata 1',
        0x01: 'logdata 2',
        0x02: 'logdata 3',
        0x03: 'logdata 4',
        0x04: 'logdata 5',
        0x05: 'logdata 6',
        0x06: 'logdata 7',
        0x07: 'logdata 8',
        0x08: 'logdata 9',
        0x09: 'logdata 10',
        0x0a: 'logdata 11',
        0x0b: 'logdata 12',
        0x0c: 'logdata 13',
        0x0d: 'logdata 14',
        0x0e: 'logdata 15',
        0x0f: 'logdata 16',
        0x10: 'sensor 1-2',
        0x11: 'sensor 3-4',
        0x12: 'sensor 5-6',
        0x13: 'sensor 7-8',
        0x14: 'poweradjust 1-2',
        0x15: 'poweradjust 3-4',
        0x16: 'poweradjust 5-6',
        0x17: 'poweradjust 7-8',
        0x18: 'software sensor 1-2',
        0x19: 'software sensor 3-4',
        0x1a: 'software sensor 5-6',
        0x1b: 'software sensor 7-8',
        0x1c: 'virtual sensor 1-2',
        0x1d: 'virtual sensor 3-4',
        0x1e: 'mps 1',
        0x1f: 'mps 2',
        0x20: 'mps 3',
        0x21: 'mps 4',
        0x22: 'aquastream xt',
        0x23: 'sensor 39-40',
        0x24: 'sensor 1-4',
        0x25: 'sensor 5-8',
        0x26: 'poweradjust 1-4',
        0x27: 'poweradjust 5-8',
        0x28: 'software sensor 1-4',
        0x29: 'software sensor 5-8',
        0x2a: 'virtual sensors',
        0x2b: 'mps 1-2',
        0x2c: 'mps 3-4',
        0x2d: 'aquastream',
        0x2e: 'sensor 41-44',
        0x2f: 'fan amp 1-4',
        0x30: 'fan amp 5-8',
        0x31: 'fan amp 9-12',
        0x32: 'sensor 56-60',
        0x33: 'sensor 61-64',
        0x34: 'fan 1-4 power',
        0x35: 'fan 5-8 power',
        0x36: 'fan 9-12 power',
        0x37: 'fan 1-4 speed',
        0x38: 'fan 5-8 speed',
        0x39: 'fan 9-12 speed',
        0x3a: 'fan 1',
        0x3b: 'fan 2',
        0x3c: 'fan 3',
        0x3d: 'fan 4',
        0x3e: 'fan 5',
        0x3f: 'fan 6',
        0x40: 'fan 7',
        0x41: 'fan 8',
        0x42: 'fan 9',
        0x43: 'fan 10',
        0x44: 'fan 11',
        0x45: 'fan 12',
        0x46: 'flow 1',
        0x47: 'flow 2',
        0x48: 'flow 3',
        0x49: 'flow 4',
        0x4a: 'flow 5',
        0x4b: 'flow 6',
        0x4c: 'flow 7',
        0x4d: 'flow 8',
        0x4e: 'flow 9',
        0x4f: 'flow 10',
        0x50: 'flow 11',
        0x51: 'flow 12',
        0x52: 'flow 13',
        0x53: 'flow 14',
        0x54: 'aquastream xt 1',
        0x55: 'aquastream xt 2',
        0x56: 'multiswitch 1',
        0x57: 'multiswitch 2',
        0x58: 'fill level 1',
        0x59: 'fill level 2',
        0x5a: 'fill level 3',
        0x5b: 'fill level 4',
        0x5c: 'power consumption 1',
        0x5d: 'power consumption 2',
        0x5e: 'power consumption 3',
        0x5f: 'power consumption 4',
        0x60: 'aquaero info',
        0x61: 'time',
        0x62: 'usb lcd',
        0x63: 'relay and power',
        0x64: 'user defined logo',
    }
    def fetch(self, data, pos):
        val = struct.unpack('>b', data[pos : pos + 1])[0]
        if val in PageType.types:
            return PageType.types[val]
        else:
            return "?%d?" % val


class AquaSerializer1036(AquaSerializer):
    """An AquaSerializer for firmware version 1036."""

    status_scheme = Group(scheme={
        'time':                 Time(at=0x0001),
        'serial_major':         UnsignedWord(at=0x0007),
        'serial_minor':         UnsignedWord(at=0x0009),
        'firmware_version':     UnsignedWord(at=0x000b),
        'bootloader_version':   UnsignedWord(at=0x000d),
        'hardware_version':     UnsignedWord(at=0x000f),
        'uptime':               Uptime(at=0x0011),
        'total_uptime':         Uptime(at=0x0015),
        'temperatures':         Group(scheme={
            'sensor':               Array(items=16, scheme={
                 'temp':                Temperature(at=0x0069, step=2),
                                    }),
            'virtual':              Array(items=4, scheme={
                 'temp':                Temperature(at=0x0099, step=2),
                                    }),
            'software':             Array(items=8, scheme={
                 'temp':                Temperature(at=0x0089, step=2),
                                    }),
            'fan_vrm':              Array(items=12, scheme={
                 'temp':                Temperature(at=0x00c1, step=2),
                                    }),
            'cpu':                  Array(items=8, scheme={
                 'temp':                Temperature(at=0x00d9, step=2),
                                    }),
            'other':                Array(items=16, scheme={
                 'temp':                Temperature(at=0x00a1, step=2),
                                    }),
                                }),
        'fans':                 Array(items=12, scheme={
            'speed':                UnsignedWord(at=0x016b, step=12),
            'power':                Percent(at=0x016d, step=12),
            'voltage':              Fraction(divisor=100.0, at=0x016f, step=12),
            'current':              Fraction(divisor=100.0, at=0x0171, step=12),
                                }),
        'flow_meters':          Array(items=14, scheme={
            'rate':                 Fraction(divisor=10.0, at=0x00fd, step=2),
                                }),
        'levels':               Array(items=14, scheme={
            'level':                Level(at=0x0149, step=2),
                                }),
        'aquastream':           Array(items=2, scheme={
            'status':               Mapped(at=0x01fb, step=8, values={
                                        1: 'available',
                                        2: 'alarm',
                                    }),
            'mode':                 Mapped(at=0x01fc, step=8, values={
                                        0: 'automatic',
                                        1: 'manual',
                                        2: 'deairation',
                                        - 1: 'offline',
                                    }),
            'frequency':            SignedWord(at=0x01fd, step=8),
            'voltage':              Fraction(divisor=100.0, at=0x01ff, step=8),
            'current':              Fraction(divisor=100.0, at=0x0201, step=8),
                                }),
    })

    settings_scheme = Group(scheme={
        'keys':                 Group(scheme={
            'disabled':             Boolean(at=0x0010),
            'brightness_in_use':    Percent(at=0x0027),
            'brightness_idle':      Percent(at=0x0029),
            'illumination_mode':    Mapped(at=0x002b, values={
                                        0: 'auto off',
                                        1: 'always on',
                                    }),
            'tone':                 Mapped(at=0x00c9, values={
                                        0: 'off',
                                        1: 'quiet',
                                        2: 'normal',
                                        3: 'loud',
                                    }),
            'sensitivity':          Group(scheme={
                'up':                   UnsignedWord(at=0x000d),
                'down':                 UnsignedWord(at=0x0009),
                'enter':                UnsignedWord(at=0x000b),
                'f1':                   UnsignedWord(at=0x0017),
                'f2':                   UnsignedWord(at=0x0015),
                'f3':                   UnsignedWord(at=0x0013),
                'f4':                   UnsignedWord(at=0x0011),
            }),
        }),
        'language':             Mapped(at=0x001a, values={
                                    0: 'english',
                                    1: 'german',
                                }),
        'display':              Group(scheme={
            'contrast':             Percent(at=0x001b),
            'brightness_in_use':    Percent(at=0x001f),
            'brightness_idle':      Percent(at=0x0021),
            'illumination_time':    UnsignedWord(at=0x0023),
            'illumination_mode':    Mapped(at=0x0025, values={
                                        0: 'auto off',
                                        1: 'always on',
                                    }),
            'mode':                 Mapped(at=0x0026, values={
                                        0: 'normal',
                                        1: 'inverted',
                                    }),
            'menu_duration':        UnsignedWord(at=0x002c),
            'page_duration':        UnsignedWord(at=0x00d4),
        }),
        'info_pages':           Array(items=32, scheme={
            'display_mode':         Mapped(at=0x0031, step=4, values={
                                        0: 'hide',
                                        1: 'show',
                                        2: 'permanent',
                                    }),
            'display_time':         UnsignedWord(at=0x0032, step=4),
            'type':                 PageType(at=0x0034, step=4),
        }),
        'units':                Group(scheme={
            'temperature':          Mapped(at=0x00c5, values={
                                        0: 'celsius',
                                        1: 'fahrenheit',
                                        2: 'kelvin',
                                    }),
            'flow':                 Mapped(at=0x00c6, values={
                                        0: 'l/h',
                                        1: 'l/min',
                                        2: 'USgal/h',
                                        3: 'USgal/min',
                                        4: 'UKgal/h',
                                        5: 'UKgal/min',
                                    }),
            'pressure':             Mapped(at=0x00c7, values={
                                        0: 'bar',
                                        1: 'psi',
                                    }),
            'decimal_separator':    Mapped(at=0x00c8, values={
                                        0: '.',
                                        1: ',',
                                    }),
        }),
        'time':                 Group(scheme={
            'timezone':             SignedByte(at=0x002f),
            'dst':                  Mapped(at=0x0030, mask=0x01, values={
                                        0x00: 'off',
                                        0x01: 'auto',
                                    }),
            'date_format':          Mapped(at=0x0030, mask=0x04, values={
                                        0x00: 'YMD',
                                        0x04: 'DMY',
                                    }),
            'time_format':          Mapped(at=0x0030, mask=0x02, values={
                                        0x00: '12h',
                                        0x02: '24h',
                                    }),
         }),
        'standby':              Group(scheme={
            'contrast':             Percent(at=0x001d),
            'lcd_brightness':       Percent(at=0x00ca),
            'key_brightness':       Percent(at=0x00ce),
            'timeout':              UnsignedWord(at=0x00cc),
            'action_power_down':    Action(at=0x00d2),
            'action_power_up':      Action(at=0x00d0),
        }),
        'temperatures':         Group(scheme={
            'sensor':               Array(items=16, scheme={
                 'offset':              Percent(at=0x00dc, step=2),
                                    }),
            'virtual':              Array(items=4, scheme={
                 'offset':              Percent(at=0x010c, step=2),
                                    }),
            'software':             Array(items=8, scheme={
                 'offset':              Percent(at=0x00fc, step=2),
                                    }),
            'fan_vrm':              Array(items=12, scheme={
                 'temp':                Percent(at=0x0134, step=2),
                                    }),
            'cpu':                  Array(items=8, scheme={
                 'temp':                Percent(at=0x014c, step=2),
                                    }),
            'other':                Array(items=16, scheme={
                 'temp':                Percent(at=0x0114, step=2),
                                    }),
                                }),
        'virtual_sensors':      Array(items=4, scheme={
            'source1':              DataSource(at=0x015c, step=7),
            'source2':              DataSource(at=0x015e, step=7),
            'source3':              DataSource(at=0x0161, step=7),
            'mode':                 Mapped(at=0x0163, step=7, values={
                                        - 1: 'disabled',
                                        0: 'max',
                                        1: 'min',
                                        2: 'average',
                                        3: 'difference',
                                        4: 'absolute',
                                    }),
        }),
        'software_sensors':     Array(items=8, scheme={
            'state':                UnsignedByte(at=0x0178, step=5),
            'fallback':             UnsignedWord(at=0x0179, step=5),
            'timeout':              UnsignedWord(at=0x017b, step=5),
        }),
        'flow_sensors':         Array(items=14, scheme={
            'calibration':          SignedWord(at=0x01a0, step=6),
            'lower_limit':          UnsignedWord(at=0x01a2, step=6),
            'upper_limit':          UnsignedWord(at=0x01a4, step=6),
        }),
        'power_sensors':        Array(items=4, scheme={
            'flow_source':          DataSource(at=0x01f4, step=6),
            'temp_source1':         DataSource(at=0x01f6, step=6),
            'temp_source2':         DataSource(at=0x01f8, step=6),
        }),
        'fans':                 Array(items=12, scheme={
            'min_speed':            UnsignedWord(at=0x020d, step=20),
            'max_speed':            UnsignedWord(at=0x020f, step=20),
            'min_power':            Percent(at=0x0211, step=20),
            'max_power':            Percent(at=0x0213, step=20),
            'boost_power':          Percent(at=0x0215, step=20),
            'boost_duration':       UnsignedWord(at=0x0217, step=20),
            'pulses':               UnsignedWord(at=0x0219, step=20),
            'regulation':           Mapped(at=0x021c, mask=0x01 , values={
                                        0: 'power',
                                        1: 'speed',
                                    }),
            'hold_minimum':         Boolean(at=0x021b, mask=0x01),
            'enable_fuse':          Boolean(at=0x021b, mask=0x02),
            'enable_boost':         Boolean(at=0x021b, mask=0x04),
            'source':               DataSource(at=0x021d, step=20),
            'fuse':                 UnsignedWord(at=0x021f, step=20),
        }),
        'aquastream':           Array(items=2, scheme={
            'mode':                 Mapped(at=0x02fd, step=3, values={
                                        0: 'automatic',
                                        1: 'manual',
                                        2: 'deairation',
                                    }),
            'frequency':            UnsignedWord(at=0x02fe, step=3),
        }),
        'power_output':         Array(items=2, scheme={
            'min_power':            Percent(at=0x030c, step=7),
            'max_power':            Percent(at=0x030e, step=7),
            'source':               DataSource(at=0x0310, step=7),
            'enabled':              Boolean(at=0x0312, step=7),
        }),
        'relay':                Group(scheme={
            'source':               DataSource(at=0x031a),
            'control':              Mapped(at=0x031c, values = {
                                        0: 'source',
                                        1: 'on',
                                        2: 'off',
                                        3: 'event',
                                    }),
            'threshold':            Percent(at=0x031d),
        }),
        'rgb_led':              Group(scheme={
            'source':               DataSource(at=0x0608),
            'pulsating':            Mapped(at=0x060a, values={
                                        0: 'off',
                                        1: 'variant 1',
                                        2: 'variant 2',
                                        3: 'variant 3',
                                    }),
            'low':                  Group(scheme={
                'temp':                 Temperature(at=0x060b),
                'color':                Color(at=0x060d),
            }),
            'optimum':              Group(scheme={
                'temp':                 Temperature(at=0x0613),
                'color':                Color(at=0x0615),
            }),
            'high':                 Group(scheme={
                'temp':                 Temperature(at=0x061b),
                'color':                Color(at=0x061d),
            }),
        }),
        'controllers':          Group(scheme={
            'twopoint':             Array(items=16, scheme={
                'source':               DataSource(at=0x03e8, step=6),
                'upper':                Percent(at=0x03ea, step=6),
                'lower':                Percent(at=0x03ec, step=6),
            }),
            'presetvalue':          Array(items=32, scheme={
                'value':                Percent(at=0x0448, step=2),
            }),
            'targetvalue':          Array(items=8, scheme={
                'source':               DataSource(at=0x488, step=14),
                'value':                Percent(at=0x48a, step=14),
                'p':                    UnsignedWord(at=0x48c, step=14),
                'i':                    Fraction(divisor=10.0, at=0x48e, step=14),
                'd':                    UnsignedWord(at=0x490, step=14),
                'reset_time':           Fraction(divisor=10.0, at=0x492, step=14),
                'hysteresis':           Percent(at=0x0494, step=14),
            }),
            'curve':                Array(items=4, scheme={
                'source':               DataSource(at=0x04f8, step=68),
                'startup_temp':         Temperature(at=0x04fa, step=68),
                'curve_temps':          CurveTemperatures(at=0x04fc, items=16, step=68),
                'curve_speed':          CurvePercents(at=0x051c, items=16, step=68),
            }),
        }),
        'data_loggers':         Array(items=16, scheme={
            'interval':             Mapped(at=0x0623, step=3, values={
                                        0: 'off',
                                        1: '2 sec',
                                        2: '10 sec',
                                        3: '30 sec',
                                        4: '1 min',
                                        5: '5 min',
                                        6: '10 min',
                                        7: '30 min',
                                        8: '1 hour',
                                    }),
            'source':               DataSource(at=0x0624, step=3),
        }),
        'alarms':               Array(items=8, scheme={
            'action1':              Action(at=0x0653, step=6),
            'action2':              Action(at=0x0655, step=6),
            'action3':              Action(at=0x0657, step=6),
        }),
        'suppress_alarm_at_poweron': UnsignedWord(at=0x0683),
        'temp_alarms':          Array(items=16, scheme={
            'source':               DataSource(at=0x0685, step=9),
            'config':               Mapped(at=0x0687, step=9, values = {
                                        0: 'exceed limit',
                                        1: 'below limit',
                                        2: 'off',
                                    }),
            'warn_limit':           Percent(at=0x0688, step=9),
            'warn_level':           SignedByte(at=0x068a, step=9),
            'alarm_limit':          Percent(at=0x068b, step=9),
            'alarm_level':          SignedByte(at=0x068d, step=9),
        }),
        'fan_alarms':           Array(items=12, scheme={
            'warn_limit':           Mapped(at=0x0715, step=4, values = {
                                        0: 'stopped for 6 sec',
                                        1: 'stopped for 12 sec',
                                        2: 'stopped for 24 sec',
                                        3: 'off',
                                    }),
            'warn_level':           SignedByte(at=0x0716, step=4),
            'alarm_limit':          Mapped(at=0x0717, step=4, values = {
                                        0: 'stopped for 6 sec',
                                        1: 'stopped for 12 sec',
                                        2: 'stopped for 24 sec',
                                        3: 'off',
                                    }),
            'alarm_level':          SignedByte(at=0x0718, step=4),
        }),
        'flow_alarms':          Array(items=4, scheme={
            'source':               DataSource(at=0x0745, step=9),
            'config':               Mapped(at=0x0747, step=9, values = {
                                        0: 'below limit',
                                        1: 'exceed limit',
                                        2: 'off',
                                    }),
            'warn_limit':           Percent(at=0x0748, step=9),
            'warn_level':           SignedByte(at=0x074a, step=9),
            'alarm_limit':          Percent(at=0x074b, step=9),
            'alarm_level':          SignedByte(at=0x074d, step=9),
        }),
        'pump_alarms':          Array(items=4, scheme={
            'source':               DataSource(at=0x0769, step=4),
            'disabled':             Boolean(at=0x076b, step=4),
            'alarm_level':          SignedByte(at=0x076c, step=4),
        }),
        'fill_level_alarms':    Array(items=4, scheme={
            'source':               DataSource(at=0x0779, step=9),
            'disabled':             Boolean(at=0x077b, step=9),
            'warn_limit':           Percent(at=0x077c, step=9),
            'warn_level':           UnsignedByte(at=0x077e, step=9),
            'alarm_limit':          Percent(at=0x077f, step=9),
            'alarm_level':          SignedByte(at=0x0781, step=9),
        }),
        'timers':               Array(items=32, scheme={
            'sunday':               Boolean(mask=0x01, at=0x07c1, step=7),
            'monday':               Boolean(mask=0x02, at=0x07c1, step=7),
            'tuesday':              Boolean(mask=0x04, at=0x07c1, step=7),
            'wednesday':            Boolean(mask=0x08, at=0x07c1, step=7),
            'thursday':             Boolean(mask=0x10, at=0x07c1, step=7),
            'friday':               Boolean(mask=0x20, at=0x07c1, step=7),
            'saturday':             Boolean(mask=0x40, at=0x07c1, step=7),
            'time':                 Uptime(at=0x07c2, step=7),  # TODO: hour/minute/second instead
            'action':               Action(at=0x07c6, step=7),
        }),
        'ir_function':          Group(scheme={
            'aquaero':              Boolean(mask=0x01, at=0x08a1),
            'pc_mouse':             Boolean(mask=0x02, at=0x08a1),
            'pc_keyboard':          Boolean(mask=0x04, at=0x08a1),
            'forward_unknown':      Boolean(mask=0x08, at=0x08a1),
            'layout':               UnsignedByte(at=0x08a2),
        }),
        'ir_commands':          Array(items=16, scheme={
            'enabled':              Boolean(at=0x08a3, step=12),
            'action':               Action(at=0x08a5, step=12),
            'refresh_rate':         UnsignedWord(at=0x08a7, step=12),
            'signal1':              UnsignedWord(at=0x08a9, step=12),
            'signal2':              UnsignedWord(at=0x08ab, step=12),
            'signal3':              UnsignedWord(at=0x08ad, step=12),
        }),
        'ir_pc_switch':         Group(scheme={
            'enabled':              Boolean(at=0x0964),
            'refresh_rate':         UnsignedWord(at=0x0967),
            'signal1':              UnsignedWord(at=0x0969),
            'signal2':              UnsignedWord(at=0x096b),
            'signal3':              UnsignedWord(at=0x096d),
            'action_on':            Action(at=0x096f),
            'action_off':           Action(at=0x0971),
        }),
        'allow_output_override': Boolean(at=0x0973),
    })

    string_keys = (
        'F1', 'F2', 'F3', 'F4', 'exit', 'Menu', 'back', 'cancel', 'learn',
        'dummy 1', 'dummy 2', 'dummy 3', 'dummy 4', 'dummy 5', 'dummy 6', 'dummy 7',
        'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'Sensor 7', 'Sensor 8',
        'poweradjust 1', 'poweradjust 2', 'poweradjust 3', 'poweradjust 4',
        'poweradjust 5', 'poweradjust 6', 'poweradjust 7', 'poweradjust 8',
        'Software sensor 1', 'Software sensor 2', 'Software sensor 3', 'Software sensor 4',
        'Software sensor 5', 'Software sensor 6', 'Software sensor 7', 'Software sensor 8',
        'Virtual temperature 1', 'Virtual temperature 2', 'Virtual temperature 3', 'Virtual temperature 4',
        'mps 1 external', 'mps 1 internal', 'mps 2 external', 'mps 2 internal',
        'mps 3 external', 'mps 3 internal', 'mps 4 external', 'mps 4 internal',
        'aquastream 1', 'aquastream 2', 'Sensor 39', 'Sensor 40', 'Sensor 41', 'Sensor 42',
        'Sensor 43', 'Sensor 44',
        'Fan amplifier 1', 'Fan amplifier 2', 'Fan amplifier 3', 'Fan amplifier 4',
        'Fan amplifier 5', 'Fan amplifier 6', 'Fan amplifier 7', 'Fan amplifier 8',
        'Fan amplifier 9', 'Fan amplifier 10', 'Fan amplifier 11', 'Fan amplifier 12',
        'aquaero CPU', 'Sensor 58', 'Sensor 59', 'Sensor 60', 'Sensor 61', 'Sensor 62',
        'Sensor 63', 'Sensor 64',
        'Fan 1', 'Fan 2', 'Fan 3', 'Fan 4', 'Fan 5', 'Fan 6', 'Fan 7', 'Fan 8',
        'Fan 9', 'Fan 10', 'Fan 11', 'Fan 12',
        'Flow 1', 'Flow 2', 'Flow 3', 'Flow 4', 'Flow 5', 'Flow 6', 'Flow 7', 'Flow 8',
        'Flow 9', 'Flow 10', 'Flow 11', 'Flow 12', 'Flow 13', 'Flow 14',
        'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
        'aquastream XT 1', 'aquastream XT 2',
        'multiswitch 1', 'multiswitch 2',
        'Set point contr. 1', 'Set point contr. 2', 'Set point contr. 3', 'Set point contr. 4',
        'Set point contr. 5', 'Set point contr. 6', 'Set point contr. 7', 'Set point contr. 8',
        'Curve controller 1', 'Curve controller 2', 'Curve controller 3', 'Curve controller 4',
        'Two point contr. 1', 'Two point contr. 2', 'Two point contr. 3', 'Two point contr. 4',
        'Two point contr. 5', 'Two point contr. 6', 'Two point contr. 7', 'Two point contr. 8',
        'Two point contr. 9', 'Two point contr. 10', 'Two point contr. 11', 'Two point contr. 12',
        'Two point contr. 13', 'Two point contr. 14', 'Two point contr. 15', 'Two point contr. 16',
        'Preset value 1', 'Preset value 2', 'Preset value 3', 'Preset value 4',
        'Preset value 5', 'Preset value 6', 'Preset value 7', 'Preset value 8',
        'Power output 1', 'Power output 2',
        'Normal operation', 'Warning', 'Alarm', 'Alarm/Warning 3',
        'Alarm/Warning 4', 'Alarm/Warning 5', 'Alarm/Warning 6', 'Alarm/Warning 7',
        'aquaero 5',
        'Fill level 1', 'Fill level 2', 'Fill level 3', 'Fill level 4',
        'Pressure 1', 'Pressure 2', 'Pressure 3', 'Pressure 4',
        'Humidity 1', 'Humidity 2', 'Humidity 3', 'Humidity 4',
        'Water quality 1', 'Water quality 2', 'Water quality 3', 'Water quality 4',
        'D5 pump 1', 'D5 pump 2', 'D5 pump 3', 'D5 pump 4',
    )

    def unpack_status(self, data):
        return AquaSerializer1036.status_scheme.get(data)

    def unpack_settings(self, data):
        return AquaSerializer1036.settings_scheme.get(data)

    def unpack_strings(self, data):
        result = []
        while data:
            result.append(data[0:22].tobytes().decode('iso-8859-15').rstrip('\x00'))
            data = data[22:]
        return dict(zip(self.string_keys, result))

