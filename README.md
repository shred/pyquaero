# pyquaero

This is a Python library and web service for accessing [Aquaero](https://aquacomputer.de/aquaero-5.html) fan and pump controllers by Aqua Computer GmbH & Co. KG.

_pyquaero_ is a community open source project. It is not endorsed by or affiliated with Aqua Computer.

_pyquaero_ supports Aquaero devices with **firmware version 2100 or 1036**. Other firmware versions may work as well, after some tweaking.

## USE THIS SOFTWARE AT YOUR OWN RISK!

The _pyquaero_ main developer is running this software for several years now, without any negative side effects. However, it is a highly experimental software, and it is based on reverse engineering only.

* This software might damage your Aquaero device in a way that it must be repaired or replaced.
* The use of this software could lead to failure of cooling fans or aqua pumps, which might cause permanent damage to heat sensitive components of your system.
* Using this software might void your warranty.

Neither the _pyquaero_ developers nor Aqua Computer GmbH & Co. KG can be held liable for any damage caused by this software.

It is strongly recommended to use only the official software!

## Installation

```sh
pip install pyquaero
```

See the [documentation](https://shredzone.org/docs/pyquaero/index.html) for how the library and tools are used.

## Contribute

* Fork the [Source code at GitHub](https://github.com/shred/pyquaero). Feel free to send pull requests.
* Found a bug? [File a bug report!](https://github.com/shred/pyquaero/issues)

## License

_pyquaero_ is open source software. The source code is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).

## Acknowledgements

* [Aqua Computer GmbH & Co. KG](https://www.aquacomputer.de) for donating an Aquaero LT for development purposes.
* JinTu for [aerotools-ng](https://github.com/JinTu/aerotools-ng). Without his work, pyquaero would not exist.
* The members of the [Aqua Computer Forum](https://forum.aquacomputer.de) for helping, reverse engineering and feedback.
