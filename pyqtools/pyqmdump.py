#!/usr/bin/env python3
#
# pyquaero - a Python library for Aquaero fan controllers
#
# Copyright (C) 2019 Richard "Shred" Körber
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

"""Dumps the Aquaero memory for reverse engineering purposes."""

import argparse
import sys
import usb

import pyquaero.backend

def dump(unit, flash=True):
    aq = pyquaero.backend.Backend(unit)
    firmware = aq.get_firmware()
    structure = aq.get_structure()

    print('Firmware Version: %d' % (firmware))
    print('Structure Version: %d' % (structure))

    print('Reading status...')
    status = aq.read_status(2048)
    status_fn = 'status-%d-%d.bin' % (firmware, structure)
    with open(status_fn, 'wb') as out:
        out.write(status)
    print('  Success! Dumped %d bytes into %s' % (len(status), status_fn))
    print()

    print('Reading settings...')
    settings = aq.read_settings(4096)
    settings_fn = 'settings-%d-%d.bin' % (firmware, structure)
    with open(settings_fn, 'wb') as out:
        out.write(settings)
    print('  Success! Dumped %d bytes into %s' % (len(settings), settings_fn))
    print()

    if flash:
        flash_end = 0x100000
        print('Reading flash memory... (this may take a while)')
        dump = b''
        for address in range(0x00000, flash_end, 0x01000):
            print('  %05X %3d%%' % (address, ((int) (address * 100 / flash_end))), end='\r')
            dump += aq.read_strings(address)
        flash_fn = 'flash-%d-%d.bin' % (firmware, structure)
        with open(flash_fn, 'wb') as out:
            out.write(dump)
        print('  Success! Dumped %d bytes into %s' % (len(dump), flash_fn))
        print('  It is recommended to power off your Aquaero device for a few seconds now.')
        print()

    print('Dump is completed!')

    aq.close()


def main():
    parser = argparse.ArgumentParser(description='Dumps the status, settings, and flash memory of an Aquaero device for analytical purposes')
    parser.add_argument('-u', '--unit', default=0, type=int, help='Aquaero unit number')
    parser.add_argument('--flash', action='store_true', help='Also dump the contents of the flash memory (potentially risky, Aquaero reboot is recommended after that)')
    parser.add_argument('--i-mean-it', dest='imeanit', action='store_true', help='Confirm that you know what you are doing')
    args = parser.parse_args()

    if not args.imeanit:
        parser.print_help()
        print()
        print('''pyqmdump is meant for reverse engineering purposes only.

It connects to your Aquaero device, irregarding of the firmware version.
This is potentially risky, as it is not known how the Aquaero device is
reacting on the commands sent by this tool.

WARNING:
 - Your Aquaero device may crash or behave erratic. Fans and pumps might
   stop at any time. Do not use this tool while your Aquaero device is
   in use (e.g. actually cooling a computer).
 - After use, it is recommended to restart your Aquaero device by
   disconnecting it from power for a few seconds.
 - Use it at your own risk.

If you really know what you are doing, set the --i-mean-it option.''')
        sys.exit(1)

    try:
        dump(args.unit, args.flash)
    except KeyboardInterrupt:
        print()
        print()
        print('Dump was aborted! To avoid malfunction, restart your Aquaero device.')
    except usb.USBError as err:
        print()
        print()
        print('Failed to connect to the Aquaero.\nReason: %s\nReconnect the Aquaero device and try again.' % err)
