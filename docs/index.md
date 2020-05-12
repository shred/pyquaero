# Setup

This is a Python library and web service for accessing [Aquaero](https://aquacomputer.de/aquaero-5.html) fan and pump controllers by Aqua Computer GmbH & Co. KG.

_pyquaero_ is a community open source project. It is not endorsed by or affiliated with Aqua Computer.

!!! attention "EXPERIMENTAL SOFTWARE! USE AT YOUR OWN RISK!"

    The _pyquaero_ main developer is running this software for several years now, without any negative side effects. However, it is a highly experimental software, and it is based on reverse engineering only.

    * This software might damage your Aquaero device in a way that it must be repaired or replaced.
    * The use of this software could lead to failure of cooling fans or aqua pumps, which might cause permanent damage to heat sensitive components of your system.
    * Using this software might void your warranty.

    Neither the _pyquaero_ developers nor the manufacturer can be held liable for any damage caused by this software.

    It is strongly recommended to use only the official software!

## Supported Firmware Versions

Before you install _pyquaero_, [check here](firmware) if your Aquaero firmware is supported.

## Installation

```sh
pip install pyquaero
```

## USB Setup

Accessing the USB port might need root permission. However it is not recommended to use _pyquaero_ with root rights. Depending on the operating system, some extra steps might be necessary to give users permission to access the USB port.

### Fedora, RedHat, CentOS

Execute this sequence to set up an `aquaero` group, change the Aquaero USB permissions and add the user `$user` to this group:

```sh
cat > /etc/udev/rules.d/40-aquaero.rules << __EOF__
ATTRS{idVendor}=="0c70",ATTRS{idProduct}=="f001",MODE="0660",GROUP="aquaero"
__EOF__
groupadd -r aquaero
usermod -aG aquaero $user
```

The `$user` is now allowed to access the Aquaero USB device.

## Open Source

_pyquaero_ is open source software. The source code is available [at GitHub](https://github.com/shred/pyquaero), and is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
