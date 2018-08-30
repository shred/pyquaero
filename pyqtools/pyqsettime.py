#!/usr/bin/env python3
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

"""A simple example that sets the Aquaero clock."""

import argparse

import pyquaero.core

def main():
    parser = argparse.ArgumentParser(description='Set the clock of an Aquaero device')
    parser.add_argument('-u', '--unit', default=0, type=int, help='Aquaero unit number')
    args = parser.parse_args()

    with pyquaero.core.Aquaero(args.unit) as aq:
        print('Setting clock of Aquaero unit %d' % args.unit)
        aq.set_time()
