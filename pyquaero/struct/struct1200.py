#
# pyquaero - a Python library for Aquaero fan controllers
#
# Copyright (C) 2018 Richard "Shred" Körber
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
    def fetch(self, data, pos):
        val = struct.unpack('>h', data[pos : pos + 2])[0]
        return "?%d?" % val if val >= 0 else None


class Action(AquaType):
    """A word containing an action."""
    actions = {
        - 1: None,
        0: 'speed signal generator off',
        1: 'speed signal generator on',
        2: 'alarm buzzer on',
        3: 'alarm buzzer off',
        4: 'alarm buzzer cycle on-off',
        5: 'alarm buzzer single tone',
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
    def fetch(self, data, pos):
        val = struct.unpack('>b', data[pos : pos + 1])[0]
        return "?%d?" % val if val >= 0 else None


class AquaSerializer1200(AquaSerializer):
    """An AquaSerializer for structure version 1200."""

    status_scheme = Group(scheme={
        'time':                 Time(at=0x0001),
        'structure_version':    UnsignedWord(at=0x0005),
        'serial_major':         UnsignedWord(at=0x0007),
        'serial_minor':         UnsignedWord(at=0x0009),
        'firmware_version':     UnsignedWord(at=0x000b),
        'bootloader_version':   UnsignedWord(at=0x000d),
        'hardware_version':     UnsignedWord(at=0x000f),
        'uptime':               Uptime(at=0x0011),
        'total_uptime':         Uptime(at=0x0015),
        'tacho':                UnsignedWord(at=0x0165),
        'temperatures':         Group(scheme={
            'sensor':               Array(items=8, scheme={
                 'temp':                Temperature(at=0x0065, step=2),
                                    }),
            'poweradjust':          Array(items=8, scheme={
                 'temp':                Temperature(at=0x0075, step=2),
                                    }),
            'software':             Array(items=8, scheme={
                 'temp':                Temperature(at=0x0085, step=2),
                                    }),
            'virtual':              Array(items=4, scheme={
                 'temp':                Temperature(at=0x0095, step=2),
                                    }),
            'mps':                  Array(items=4, scheme={
                 'external':            Temperature(at=0x009d, step=4),
                 'internal':            Temperature(at=0x009f, step=4),
                                    }),
            'aquastream':           Array(items=4, scheme={
                 'temp':                Temperature(at=0x00ad, step=2),
                                    }),
            'calitemp':             Array(items=4, scheme={
                 'temp':                Temperature(at=0x00b5, step=2),
                                    }),
            'fan_vrm':              Array(items=12, scheme={
                 'temp':                Temperature(at=0x00bd, step=2),
                                    }),
            'other':                Array(items=4, scheme={
                 'temp':                Temperature(at=0x00d5, step=2),
                                    }),
            'vision':               Array(items=4, scheme={
                 'temp':                Temperature(at=0x00dd, step=2),
                                    }),
                                }),
        'fans':                 Array(items=12, scheme={
            'speed':                UnsignedWord(at=0x0167, step=12, optional=True),
            'power':                Percent(at=0x0169, step=12),
            'voltage':              Fraction(divisor=100.0, at=0x016b, step=12),
            'current':              Fraction(divisor=1000.0, at=0x016d, step=12),
            'performance':          Fraction(divisor=100.0, at=0x016f, step=12),
            'torque':               SignedWord(at=0x0171, step=12),
                                }),
        'flow_meters':          Array(items=14, scheme={
            'rate':                 Fraction(divisor=10.0, at=0x00f9, step=2, optional=True),
                                }),
        'levels':               Array(items=4, scheme={
            'level':                Level(at=0x0145, step=2),
                                }),
        'pressures':            Array(items=4, scheme={
            'pressure':             SignedWord(at=0x015d, step=2, optional=True),
                                }),
        'powerconsumption':     Array(items=4, scheme={
            'flow':                 UnsignedFraction(divisor=10.0, at=0x0115, step=12, optional=True),
            'sensor1':              Temperature(at=0x0117, step=12),
            'sensor2':              Temperature(at=0x0119, step=12),
            'deltaT':               Fraction(divisor=100.0, at=0x011b, step=12),
            'power':                SignedWord(at=0x011d, step=12),
            'resistance':           SignedWord(at=0x011f, step=12, optional=True),
                                }),
        'aquastream':           Array(items=6, scheme={
            'status':               Mapped(at=0x01f7, step=8, values={
                                        1: 'available',
                                        2: 'alarm',
                                        3: 'alarm',
                                    }),
            'mode':                 Mapped(at=0x01f8, step=8, values={
                                        0: 'automatic',
                                        1: 'manual',
                                        2: 'data source',
                                        3: 'level sense',
                                        - 1: 'offline',
                                    }),
            'speed':                UnsignedWord(at=0x01f9, step=8, optional=True),
            'voltage':              UnsignedFraction(divisor=100.0, at=0x01fb, step=8, optional=True),
            'current':              UnsignedFraction(divisor=1000.0, at=0x01fd, step=8, optional=True),
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
            'sensor':               Array(items=8, scheme={
                 'offset':              Percent(at=0x00dc, step=2),
                                    }),
            'poweradjust':          Array(items=8, scheme={
                 'offset':              Percent(at=0x00ec, step=2),
                                    }),
            'software':             Array(items=8, scheme={
                 'offset':              Percent(at=0x00fc, step=2),
                                    }),
            'virtual':              Array(items=4, scheme={
                 'offset':              Percent(at=0x010c, step=2),
                                    }),
            'mps':                  Array(items=4, scheme={
                 'external':            Percent(at=0x0114, step=4),
                 'internal':            Percent(at=0x0116, step=4),
                                    }),
            'aquastream':           Array(items=4, scheme={
                 'offset':              Percent(at=0x0124, step=2),
                                    }),
            'calitemp':             Array(items=4, scheme={
                 'offset':              Percent(at=0x012c, step=2),
                                    }),
            'fan_vrm':              Array(items=12, scheme={
                 'offset':              Percent(at=0x0134, step=2),
                                    }),
            'other':                Array(items=7, scheme={
                 'offset':              Percent(at=0x014c, step=2),
                                    }),
                                }),
        'virtual_sensors':      Array(items=4, scheme={
            'source1':              DataSource(at=0x015b, step=7),
            'source2':              DataSource(at=0x015d, step=7),
            'source3':              DataSource(at=0x0160, step=7),
            'mode':                 Mapped(at=0x0162, step=7, values={
                                        - 1: 'disabled',
                                        0: 'max',
                                        1: 'min',
                                        2: 'average',
                                        3: 'difference',
                                        4: 'absolute',
                                    }),
        }),
        'software_sensors':     Array(items=8, scheme={
            'state':                UnsignedByte(at=0x0177, step=5),
            'fallback':             UnsignedWord(at=0x0178, step=5),
            'timeout':              UnsignedWord(at=0x017a, step=5),
        }),
        'flow_sensors':         Array(items=14, scheme={
            'calibration':          SignedWord(at=0x019f, step=6),
            'lower_limit':          UnsignedWord(at=0x01a1, step=6),
            'upper_limit':          UnsignedWord(at=0x01a3, step=6),
        }),
        'power_sensors':        Array(items=4, scheme={
            'flow_source':          DataSource(at=0x01f3, step=6),
            'temp_source1':         DataSource(at=0x01f5, step=6),
            'temp_source2':         DataSource(at=0x01f7, step=6),
        }),
        'fans':                 Array(items=12, scheme={
            'min_speed':            UnsignedWord(at=0x020c, step=20),
            'max_speed':            UnsignedWord(at=0x020e, step=20),
            'min_power':            Percent(at=0x0210, step=20),
            'max_power':            Percent(at=0x0212, step=20),
            'boost_power':          Percent(at=0x0214, step=20),
            'boost_duration':       UnsignedWord(at=0x0216, step=20),
            'pulses':               UnsignedWord(at=0x0218, step=20),
            'regulation':           Mapped(at=0x021b, mask=0x01, values={
                                        0: 'power',
                                        1: 'speed',
                                    }),
            'hold_minimum':         Boolean(at=0x021a, mask=0x01),
            'enable_fuse':          Boolean(at=0x021a, mask=0x02),
            'enable_boost':         Boolean(at=0x021a, mask=0x04),
            'source':               DataSource(at=0x021c, step=20),
            'fuse':                 UnsignedWord(at=0x021e, step=20),
        }),
        'controllers':          Group(scheme={
            'twopoint':             Array(items=16, scheme={
                'source':               DataSource(at=0x04fc, step=6),
                'upper':                Percent(at=0x04fe, step=6),
                'lower':                Percent(at=0x0500, step=6),
            }),
            'presetvalue':          Array(items=32, scheme={
                'value':                Percent(at=0x055c, step=2),
            }),
        }),
        'timers':               Array(items=16, scheme={
            'sunday':               Boolean(mask=0x01, at=0x090a, step=7),
            'monday':               Boolean(mask=0x02, at=0x090a, step=7),
            'tuesday':              Boolean(mask=0x04, at=0x090a, step=7),
            'wednesday':            Boolean(mask=0x08, at=0x090a, step=7),
            'thursday':             Boolean(mask=0x10, at=0x090a, step=7),
            'friday':               Boolean(mask=0x20, at=0x090a, step=7),
            'saturday':             Boolean(mask=0x40, at=0x090a, step=7),
            'time':                 Uptime(at=0x090b, step=7),  # TODO: hour/minute/second instead
            'action':               Action(at=0x090f, step=7),
        }),
        'ir_function':          Group(scheme={
            'aquaero':              Boolean(mask=0x01, at=0x097a),
            'pc_mouse':             Boolean(mask=0x02, at=0x097a),
            'pc_keyboard':          Boolean(mask=0x04, at=0x097a),
            'forward_unknown':      Boolean(mask=0x08, at=0x097a),
            'layout':               UnsignedByte(at=0x097b),
        }),
        'ir_commands':          Array(items=16, scheme={
            'enabled':              Boolean(at=0x097c, step=12),
            'action':               Action(at=0x097e, step=12),
            'refresh_rate':         UnsignedWord(at=0x0980, step=12),
            'signal1':              UnsignedWord(at=0x0982, step=12),
            'signal2':              UnsignedWord(at=0x0984, step=12),
            'signal3':              UnsignedWord(at=0x0986, step=12),
        }),
        'ir_pc_switch':         Group(scheme={
            'enabled':              Boolean(at=0x0a3d),
            'refresh_rate':         UnsignedWord(at=0x0a40),
            'signal1':              UnsignedWord(at=0x0a42),
            'signal2':              UnsignedWord(at=0x0a44),
            'signal3':              UnsignedWord(at=0x0a46),
            'action_on':            Action(at=0x0a48),
            'action_off':           Action(at=0x0a4a),
        }),
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
        'aquastream 1a', 'aquastream 1b', 'aquastream 2a', 'aquastream 2b',
        'calitemp 1', 'calitemp 2', 'calitemp 3', 'calitemp 4',
        'Fan amplifier 1', 'Fan amplifier 2', 'Fan amplifier 3', 'Fan amplifier 4',
        'Fan amplifier 5', 'Fan amplifier 6', 'Fan amplifier 7', 'Fan amplifier 8',
        'Fan amplifier 9', 'Fan amplifier 10', 'Fan amplifier 11', 'Fan amplifier 12',
        'Sensor 57', 'Sensor 58', 'Sensor 59', 'Sensor 60',
        'vision 1', 'vision 2', 'vision 3', 'vision 4',
        'Fan 1', 'Fan 2', 'Fan 3', 'Fan 4', 'Fan 5', 'Fan 6', 'Fan 7', 'Fan 8',
        'Fan 9', 'Fan 10', 'Fan 11', 'Fan 12',
        'Flow 1', 'Flow 2', 'Flow 3', 'Flow 4', 'Flow 5', 'Flow 6', 'Flow 7', 'Flow 8',
        'Flow 9', 'Flow 10', 'Flow 11', 'Flow 12', 'Flow 13', 'Flow 14',
        'Profile 1', 'Profile 2', 'Profile 3', 'Profile 4',
        'Set point contr. 1', 'Set point contr. 2', 'Set point contr. 3', 'Set point contr. 4',
        'Set point contr. 5', 'Set point contr. 6', 'Set point contr. 7', 'Set point contr. 8',
        'Curve controller 1', 'Curve controller 2', 'Curve controller 3', 'Curve controller 4',
        'Two point contr. 1', 'Two point contr. 2', 'Two point contr. 3', 'Two point contr. 4',
        'Two point contr. 5', 'Two point contr. 6', 'Two point contr. 7', 'Two point contr. 8',
        'Two point contr. 9', 'Two point contr. 10', 'Two point contr. 11', 'Two point contr. 12',
        'Two point contr. 13', 'Two point contr. 14', 'Two point contr. 15', 'Two point contr. 16',
        'Preset fan', 'Preset relay',
        'Power outputs',
        'Preset value 4', 'Preset value 5', 'Preset value 6', 'Preset value 7',
        'Preset value 8', 'Preset value 9', 'Preset value 10', 'Preset value 11',
        'Preset value 12', 'Preset value 13', 'Preset value 14', 'Preset value 15',
        'Preset value 16', 'Preset value 17', 'Preset value 18', 'Preset value 19',
        'Preset value 20', 'Preset value 21', 'Preset value 22', 'Preset value 23',
        'Preset value 24', 'Preset value 25', 'Preset value 26', 'Preset value 27',
        'Preset value 28', 'Preset value 29', 'Preset value 30', 'Preset value 31',
        'Preset value 32',
        'Normal operation',
        'Warning', 'Alarm', 'Emergency shutdown',
        'Alarm/Warning 4', 'Alarm/Warning 5', 'Alarm/Warning 6', 'Alarm/Warning 7',
        'Fill level 1', 'Fill level 2', 'Fill level 3', 'Fill level 4',
        'Pressure 1', 'Pressure 2', 'Pressure 3', 'Pressure 4',
        'Humidity 1', 'Humidity 2', 'Humidity 3', 'Humidity 4',
        'Water quality 1', 'Water quality 2', 'Water quality 3', 'Water quality 4',
        'Timer 1', 'Timer 2', 'Timer 3', 'Timer 4', 'Timer 5', 'Timer 6', 'Timer 7', 'Timer 8',
        'Timer 9', 'Timer 10', 'Timer 11', 'Timer 12', 'Timer 13', 'Timer 14', 'Timer 15', 'Timer 16',
        'Power consumption 1', 'Power consumption 2', 'Power consumption 3', 'Power consumption 4',
        'RGB controller 1', 'RGB controller 2', 'RGB controller 3', 'RGB controller 4',
        'Red LED', 'Green LED', 'Blue LED', 'Relay',
        'Power output 1', 'Power output 2',
        'farbwerk(1) 1-R', 'farbwerk(1) 1-G', 'farbwerk(1) 1-B',
        'farbwerk(1) 2-R', 'farbwerk(1) 2-G', 'farbwerk(1) 2-B',
        'farbwerk(1) 3-R', 'farbwerk(1) 3-G', 'farbwerk(1) 3-B',
        'farbwerk(1) 4-R', 'farbwerk(1) 4-G', 'farbwerk(1) 4-B',
        'farbwerk(2) 1-R', 'farbwerk(2) 1-G', 'farbwerk(2) 1-B',
        'farbwerk(2) 2-R', 'farbwerk(2) 2-G', 'farbwerk(2) 2-B',
        'farbwerk(2) 3-R', 'farbwerk(2) 3-G', 'farbwerk(2) 3-B',
        'farbwerk(2) 4-R', 'farbwerk(2) 4-G', 'farbwerk(2) 4-B',
        'aquastream 1', 'aquastream 2',
        'D5 pump 1', 'D5 pump 2', 'D5 pump 3', 'D5 pump 4',
        'Pump 1', 'Pump 2',
        'output 1', 'output 2', 'output 3', 'output 4', 'output 5', 'output 6',
        'output 7', 'output 8', 'output 9', 'output 10', 'output 11', 'output 12',
        'output 13', 'output 14', 'output 15', 'output 16', 'output 17', 'output 18',
        'output 19', 'output 20', 'output 21', 'output 22', 'output 23', 'output 24',
        'output 25', 'output 26', 'output 27',
    )

    def read_status(self, backend):
        return backend.read_status(903, max_age=0.5)

    def unpack_status(self, data):
        return AquaSerializer1200.status_scheme.get(data)

    def read_settings(self, backend):
        return backend.read_settings(2707)

    def unpack_settings(self, data):
        return AquaSerializer1200.settings_scheme.get(data)

    def read_strings(self, backend):
        strings = backend.read_strings(0x00094000)
        strings += backend.read_strings(0x00095000)
        return strings

    def unpack_strings(self, data):
        result = []
        while data:
            result.append(data[0:24].tobytes().decode('iso-8859-15').rstrip('\x00'))
            data = data[24:]
        return dict(zip(self.string_keys, result))


class AquaSerializer1200Fw2007(AquaSerializer1200):
    """An AquaSerializer for structure version 1200 and firmwares starting 2007."""

    def read_status(self, backend):
        return backend.read_status(871, max_age=0.5)
