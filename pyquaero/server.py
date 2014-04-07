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

from http.server import BaseHTTPRequestHandler
import re
from socketserver import TCPServer
from threading import Timer

from pyquaero.core import Aquaero
from pyquaero.struct.serializer import from_json, to_json


class PyquaeroTimeUpdater():
    """A timer that frequently updates the Aquaero real time clock.

    By default, the clock is updated once a day.
    """

    def __init__(self, device, frequency=(24 * 60 * 60.0)):
        self.device = device
        self.frequency = frequency

    def start(self):
        """Start the update timer."""
        self.shutdown = False
        self._update_time()

    def stop(self):
        """Stop the update timer."""
        self.shutdown = True

    def _update_time(self):
        """Update the Aquaero real time clock and then wait for the next turn."""
        self.device.set_time()
        if not self.shutdown:
            timer = Timer(self.frequency, lambda: self._update_time())
            timer.daemon = True
            timer.start()


class PyquaeroHandler(BaseHTTPRequestHandler):
    """Handle HTTP requests.

    Check if there is a matching command, and then execute it.
    """

    def do_HEAD(self):
        """Respond to a HEAD request."""
        if not self.server.is_defined(self.path):
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_default_header()
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        if not self.server.is_defined(self.path):
            self.send_response(404)
            self.end_headers()
            return

        try:
            result = self.server.invoke(self.path)
            result = to_json(result).encode('utf-8')
        except Exception as ex:
            self.send_response(500, 'Error: ' + str(ex))
            self.end_headers()
            return

        self.send_response(200)
        self.send_default_header()
        self.send_header("Content-Length", len(result))
        self.end_headers()
        self.wfile.write(result)

    def do_POST(self):
        """Respond to a POST request."""
        if not self.server.is_defined(self.path):
            self.send_response(404)
            self.end_headers()
            return

        try:
            length = int(self.headers['Content-Length'])

            charset = 'iso-8859-1'
            contenttype = self.headers['Content-Type']
            match = re.match(r'.*?charset=([a-zA-Z0-9-]+)', contenttype)
            if match:
                charset = match.group(1)

            data = from_json(self.rfile.read(length).decode(charset))
            result = self.server.invoke(self.path, data)
            result = to_json(result).encode('utf-8')
        except Exception as ex:
            self.send_response(500, 'Error: ' + str(ex))
            self.end_headers()
            return

    def send_default_header(self):
        """Send a default header for a valid response."""
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Expires", "Sat, 01 Jan 2000 00:00:00 GMT")


class PyquaeroServer(TCPServer):
    """Connect to a Aquaero and provide a HTTP service for controlling it."""

    def __init__(self, address, unit=0, updatetime=True):
        TCPServer.__init__(self, address, PyquaeroHandler)
        self.aquaero = Aquaero(unit)
        if updatetime:
            self.time_updater = PyquaeroTimeUpdater(self.aquaero)
            self.time_updater.start()

    def server_close(self):
        if self.time_updater:
            self.time_updater.stop()
        TCPServer.server_close(self)
        self.aquaero.close()

    def is_defined(self, command):
        """Check if a command is defined."""
        return command in PyquaeroServer.commands

    def invoke(self, command, data = None):
        """Invoke a command."""
        return PyquaeroServer.commands[command](self, data)

    def handle_status(self, data):
        """Handle status command."""
        return self.aquaero.get_status()

    def handle_settings(self, data):
        """Handle settings command."""
        return self.aquaero.get_settings()

    def handle_strings(self, data):
        """Handle strings command."""
        return self.aquaero.get_strings()

    commands = {
        '/status': handle_status,
        '/settings': handle_settings,
        '/strings': handle_strings,
    }

