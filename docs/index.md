# Setup

This is a Python library and web service for accessing [Aquaero](https://aquacomputer.de/aquaero-5.html) fan and pump controllers by Aqua Computer GmbH & Co. KG.

_pyquaero_ is a community open source project. It is not endorsed by or affiliated with Aqua Computer.

!!! attention "EXPERIMENTAL SOFTWARE! USE AT YOUR OWN RISK!"

    The _pyquaero_ main developer is running this software for several years now, without any negative side effects. However, it is a highly experimental software, and it is based on reverse engineering only.

    * This software might damage your Aquaero device in a way that it must be repaired or replaced.
    * The use of this software could lead to failure of cooling fans or aqua pumps, which might cause permanent damage to heat sensitive components of your system.
    * Using this software might void your warranty.

    Neither the _pyquaero_ developers nor Aqua Computer GmbH & Co. KG can be held liable for any damage caused by this software.

    It is strongly recommended to use only the official software!

## Supported Firmware Versions

* 2100: Current status can be read almost fully. Settings are incomplete and won't decode data source and page type. Customizable strings are complete. Internal clock can be set.
* 1036: Current status and settings can be read almost fully. Customizable strings are complete. Internal clock can be set.

Other firmware versions may work as well, but require some tweaking at the source code. If you was able to add support for other firmware versions, please send in a pull request!

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

## Support of the latest Firmware

[Aqua Computer GmbH & Co. KG](https://www.aquacomputer.de) has donated an Aquaero LT for development purposes to this project. It allows me to reverse engineer the latest Aquaero firmware, and eventually support it in _pyquaero_.

Although this is good news, there are some caveats:

* It may take a while until the latest firmware is supported by _pyquaero_. If you rely on a working _pyquaero_, do not update the firmware of your Aquaero until it is supported.
* There is no guarantee that a firmware version will be supported by _pyquaero_. It still bases on reverse engineering, which may turn out to be impossible.
* Even though Aqua Computer donated an Aquaero device to this project, it does not mean that they officially support or endorse it. You are still using _pyquaero_ at your own risk, as stated in the warning above!

## Open Source

_pyquaero_ is open source software. The source code is available [at GitHub](https://github.com/shred/pyquaero), and is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).
