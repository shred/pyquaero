# Setup

This is a Python library and web service for accessing [Aquaero](https://aquacomputer.de/aquaero-5.html) fan controllers by Aqua Computer GmbH & Co. KG.

_pyquaero_ is a community open source project. It is not endorsed by or affiliated with Aqua Computer.

**NOTE:** At the moment, _pyquaero_ only supports Aquaero 5 and 6 with the now outdated **firmware version 1036**. Later firmware versions may work, but are untested.

!!! attention "EXPERIMENTAL SOFTWARE! USE AT YOUR OWN RISK!"

    The _pyquaero_ main developer is running this software for several years now, without any negative side effects. However, it is a highly experimental software, and it is based on reverse engineering only.

    * This software might damage your Aquaero device in a way that it must be repaired or replaced.
    * The use of this software could lead to failure of cooling fans or aqua pumps, which might cause permanent damage to heat sensitive components of your computer.
    * Using this software might void your warranty.

    Neither the _pyquaero_ developers nor Aqua Computer can be held liable for any damage caused by this software. We strongly recommend to use only the official software!

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

## Later Firmwares

_pyquaero_ only supports the now outdated firmware version 1036.

The reason is that I, as the developer of _pyquaero_, only own a single Aquaero, which is actually in use.

As there is no official documentation, _pyquaero_ bases on reverse engineering of the data transferred via USB. Updating the firmware of my Aquaero could mean that _pyquaero_ stops working, and I could be unable to make it work again. As I need my Aquaero, I cannot afford to risk that. For that reason, _pyquaero_ is stuck to firmware version 1036.

If you need support of the latest firmware, I would be happy about a donation so I can buy a second Aquaero for experiments only. However I cannot guarantee that there will be a release that supports the latest firmware, if technical reasons prevent it.

## Open Source

_pyquaero_ is open source software. The source code is available [at GitHub](https://github.com/shred/pyquaero), and is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
