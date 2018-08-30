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

"""Start the Pyquaero HTTP server."""

import argparse

from pyquaero.server import PyquaeroServer

def main():
    parser = argparse.ArgumentParser(description='Run the Pyquaero HTTP web service')
    parser.add_argument('-u', '--unit', default=0, type=int, help='Aquaero unit number')
    parser.add_argument('-p', '--port', default=9500, type=int, help='HTTP port the server is listening at')
    parser.add_argument('-H', '--host', default='', help='HTTP host the server is bound to')
    parser.add_argument('-T', '--notime', default=False, type=bool, help='Disable frequent Aquaero clock updates')
    args = parser.parse_args()

    httpd = PyquaeroServer((args.host, args.port), args.unit, updatetime=not args.notime)
    try:
        print('Now listening on port %d' % args.port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
