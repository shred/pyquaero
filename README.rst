pyquaero
========

A library and web service for accessing Aquaero fan controllers by Aqua Computer GmbH & Co. KG, written in Python.

WARNING
-------

(Deutsch im nächsten Absatz - German below)

**USE PYQUAERO AT YOUR OWN RISK!**

As there is no official documentation, pyquaero is highly experimental and based on reverse engineering.

**Using pyquaero may damage your Aquaero in a way that it must be repaired or replaced. Your warranty is very likely void when using pyquaero.**

Using pyquaero could lead to failure of cooling fans and aqua pumps, and thus may cause permanent damage to heat sensitive components (like CPUs).

Neither the pyquaero developers nor Aqua Computer are responsible for any damage caused by this software. We strongly recommend to use the official software only! Again: pyquaero is highly experimental.

pyquaero is a community open source project and is not endorsed by or affiliated with Aqua Computer.

WARNUNG
-------

**DU VERWENDEST PYQUAERO AUF DEIN EIGENES RISIKO!**

Da es keine offizielle Dokumentation gibt, basiert pyquaero auf reverse engineering und ist in hohem Maße experimentell.

**Durch die Verwendung von pyquaero kann dein Aquaero so stark beschädigt werden, dass es repariert oder ausgetauscht werden muss. Deine Garantie verfällt sehr wahrscheinlich bei der Verwendung von pyquaero.**

Durch pyquaero können Lüfter und Wasserpumpen ausfallen, wodurch hitzeempfindliche Komponenten (z. B. CPUs) dauerhaft beschädigt werden können.

Weder die pyquaero-Entwickler noch Aqua Computer sind für jegliche Schäden verantwortlich, die durch den Einsatz dieser Software entstehen. Wir empfehlen ausdrücklich nur den Einsatz der offiziellen Software! Noch einmal: pyquaero ist hochexperimentell.

pyquaero ist ein freies Open Source-Projekt und steht in keinem Bezug zu Aqua Computer.

USB Setup
---------

It is not recommended to use Pyquaero or ``pyqd.py`` with root rights.

Execute this sequence to set up an "aquaero" group, change the Aquaero USB permissions and add the user ``$user`` to this group::

    cat > /etc/udev/rules.d/40-aquaero.rules << __EOF__
    ATTRS{idVendor}=="0c70",ATTRS{idProduct}=="f001",MODE="0660",GROUP="aquaero"
    __EOF__
    groupadd -r aquaero
    usermod -aG aquaero $user

The ``$user`` is now able to access the Aquaero USB device.

Usage
-----

**Note** that Pyquaero currently only supports Aquaero 5 and 6 with firmware version 1036.

To use Pyquaero as a library in your own project, you usually import ``pyquaero.core`` and create an instance of ``Aquaero``. Multiple Aquaero devices are supported. If the unit number is omitted, the first device is used. Example::

    import pyquaero.core
    with pyquaero.core.Aquaero() as aq:
        aq.set_time()

The other modules contain low level access classes which are not very useful for other projects unless you want to use features of Aquaero that are not supported by this library.

Server Usage
------------

Pyquaero provides a HTTP web service that communicates via simple commands and JSON. It is called ``pyqd.py``.

``pyqd.py --help`` shows its usage.

If you just start ``pyqd.py``, it connects to the first Aquaero device found, and listens on port 9500 for HTTP requests by default. It also takes care of keeping the Aquaero real time clock up to date.

These commands are currently implemented:

status
  Return the current status of the Aquaero device as JSON.

settings
  Return the current settings of the Aquaero device as JSON.

strings
  Return the current customizable strings of the Aquaero device as JSON.

Example: http://localhost:9500/status returns the current status of your Aquaero as JSON data.

Setting the Clock
-----------------

``pyqsettime.py`` is a simple example tool that sets the real time clock of your Aquaero to your system's time.

``pyqsettime.py --help`` shows the usage. Without arguments, it will set the clock of your first Aquaero device.

Note that ``pyqsettime.py`` cannot be used while ``pydq.py`` is running on the Aquaero device. However, ``pydq.py`` usually takes care of setting the real time clock and keeping it up to date, so there is no need to run ``pyqsettime.py`` anyways.

Development
-----------

The project is hosted at `GitHub <https://github.com/shred/pyquaero>`_

Pyquaero is developed in Python 3. It is my first Python project, so please be patient if things are not very pythonesque yet. Your feedback and patches are very welcome.

Pyquaero is currently in alpha state. The API and the web services may undergo major changes without prior notice.

The Future
----------

These features are planned for future releases:

* Web service commands for changing the configuration via JSON.
* Support for other firmware versions.
* Munin support.
* A configuration tool.

Acknowledgements
----------------

* JinTu for `aerotools-ng <https://github.com/JinTu/aerotools-ng>`_. Without his work, Pyquaero would not exist.
* The people of `Aqua Computer Forum <http://forum.aquacomputer.de>`_ for helping, reverse engineering and feedback.
