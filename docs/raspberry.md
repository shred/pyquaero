# Raspberry Pi

_pyquaero_ is tested and runs on Raspberry Pi with either [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) or [Fedora 27 or higher](https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi).

!!! important
    Make sure the Raspberry Pi's power supply is generously dimensioned. If the Aquaero power supply fails, the Aquaero draws its 5V power from the USB port of the Raspberry. If the power supply is too weak, the Raspberry Pi may become unstable.

## Compatibility

* The _Raspberry Pi 1_ has stability issues with the USB port, maybe due to hardware or driver problems. Once in a while, the USB connection to the Aquaero is lost, and must be re-established by restarting the `pyqd` service or by a reboot.

* I don't know about the state of _Rasperry Pi 2_. Your feedback is welcome.

* The _Raspberry Pi 3_ has no USB issues. `pyqd` is running stable.
