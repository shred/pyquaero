# Tools

_pyquaero_ comes with two Aquaero related tools.

## Setting the Clock

`pyqsettime` is a simple example tool that sets the real time clock of your Aquaero to your system's time.

`pyqsettime --help` shows the usage. Without arguments, it will set the clock of your first Aquaero device.

Note that `pyqsettime` cannot be used while `pydq` is running on the Aquaero device. However, `pydq` already takes care of setting the real time clock and keeping it up to date.

## Pyquaero Server

Pyquaero provides a HTTP web service that communicates via simple commands and JSON. It is called `pyqd`.

`pyqd --help` shows its usage.

If you just start `pyqd`, it connects to the first Aquaero device found, and listens on port 9500 for HTTP requests. It also takes care of keeping the Aquaero real time clock up to date.

These end points are currently implemented:

- `status` - Return the current status of the Aquaero device as JSON (e.g. temperatures and fan speeds).
- `settings` - Return the current settings of the Aquaero device as JSON.
- `strings`- Return the current customizable strings of the Aquaero device as JSON.

Example: [http://localhost:9500/status](http://localhost:9500/status) returns the current state of your Aquaero as JSON data.
