# Tools

_pyquaero_ comes with two Aquaero related tools.

## Reading the Status

`pyqread` is a tool that reads the status, settings, or customizable strings from an Aquaero device. The output is printed to `stdout`.

`pyqread --help` shows the usage. Without arguments, it prints the current status as pretty-printed JSON.

These `--type` options are available:

- `status` - Print the current status of the Aquaero device (e.g. temperatures and fan speeds). This is the default.
- `settings` - Print the current settings of the Aquaero device.
- `strings` - Print the current customizable strings of the Aquaero device.

These `--format` options are available:

- `json` - The output is formatted as pretty-printed, human readable JSON. This is the default.
- `compact` - The output is formatted as compact, single-line JSON. Useful for post-processing the output with other tools.
- `flat` - The output is a flat set of key-value pairs, separated by `=`. Useful for post-processing with line-based tools (like grep). You can safely split key and values at the first `=` of the line, as the key will never contain that character. Note that, unlike in JSON, all `null` values are skipped in this format.

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

## Memory Dump

`pyqmdump` is a tool that is mainly used for reverse engineering. It saves a binary dump of the current status and the settings, and optionally also saves a dump of the flash memory. The dumps are saved to the current working directory.

This tool ignores the firmware and structure version. Invoking the tool may be harmful to the Aquaero device, because it is unclear how unknown firmware versions react on the USB commands send to it. For security reasons, it won't start unless the `--i-mean-it` parameter is set on the command line, so you cannot run it by accident.

!!! important
    Only invoke `pyqmdump` if your Aquaero does not currently serve any vital purposes (like actually cooling a computer). The Aquaero may crash or behave erratic when running this tool. Connected fans and pumps might stop, or rotate too slow.

    After dumping the flash memory, it is strongly recommended to reset the Aquaero by disconnecting it from power for a few seconds.
