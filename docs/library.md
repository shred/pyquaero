# Library

To use Pyquaero as a library in your own project, you usually import `pyquaero.core` and create an instance of `Aquaero`. Multiple Aquaero devices are supported. If the unit number is omitted, the first device is used. Example:

```python
import pyquaero.core

with pyquaero.core.Aquaero() as aq:
    aq.set_time()
```

`Aquaero` offers four methods:

* `get_settings` - Read the current settings of the Aquaero.
* `get_status` - Read the current status, e.g. fan speeds and temperatures.
* `get_strings` - Read message strings.
* `set_time` - Set the Aquaero time.

!!! note
    Currently it is only possible to read the state of the Aquaero device, and set the current time. It is not possible to change the settings.

The other modules of this project contain low level access classes which are not very useful for other projects unless you want to use features of Aquaero that are not supported by this library.
