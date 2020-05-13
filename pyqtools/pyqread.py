#!/usr/bin/env python3
#
# pyquaero - a Python library for Aquaero fan controllers
#
# Copyright (C) 2020 Richard "Shred" Körber
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

"""A command line tool for reading the current status, settings, or strings."""

import argparse
import datetime

import pyquaero.core
from pyquaero.struct.serializer import to_json

def printFlat(value, key=''):
    if value is None:
        pass
    elif isinstance(value, list):
        index = 0
        for av in value:
            printFlat(av, '%s[%d]' % (key, index))
            index += 1
    elif isinstance(value, dict):
        for dictKey in sorted(value.keys()):
            printFlat(value[dictKey], key=dictKey if not len(key) else key + '.' + dictKey)
    elif isinstance(value, datetime.datetime):
        print('%s = %s' % (key, value.isoformat()))
    elif isinstance(value, datetime.timedelta):
        print('%s = %d' % (key, value.total_seconds()))
    else:
        print('%s = %s' % (key, str(value)))


def main():
    parser = argparse.ArgumentParser(description='Read the Aquaero status, settings, or strings')
    parser.add_argument('-u', '--unit', default=0, type=int, help='Aquaero unit number')
    parser.add_argument('-t', '--type', default="status", choices=['status', 'settings', 'strings'], help='Data type to read, default is "status"')
    parser.add_argument('-f', '--format', default="json", choices=['json', 'compact', 'flat'], help='Output format, default is "json"')
    args = parser.parse_args()

    data = {}
    with pyquaero.core.Aquaero(args.unit) as aq:
        if 'status' == args.type:
            data = aq.get_status()
        elif 'settings' == args.type:
            data = aq.get_settings()
        elif 'strings' == args.type:
            data = aq.get_strings()

    if 'json' == args.format:
        print(to_json(data, indent=2))
    elif 'compact' == args.format:
        print(to_json(data))
    elif 'flat' == args.format:
        printFlat(data)
