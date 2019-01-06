# Firmware

## Supported Firmware Versions

These are the Aquaero firmware versions currently supported by _pyquaero_:

<div class="firmware">
<table>
<thead>
<tr>
  <th>Version (Structure)</th>
  <th>Read Status</th>
  <th>Read Settings</th>
  <th>Change Settings</th>
  <th>Read Strings</th>
  <th>Change Strings</th>
  <th>Set Time</th>
</tr>
</thead>
<tbody>
<tr>
  <td>2101 (1200)</td>
  <td class="fw-ok">OK</td>
  <td class="fw-part">Partial</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
</tr>
<tr>
  <td>2100 (1200)</td>
  <td class="fw-ok">OK</td>
  <td class="fw-part">Partial</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
</tr>
<tr>
  <td>1036 (1013)</td>
  <td class="fw-ok">OK</td>
  <td class="fw-ok">OK</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
  <td class="fw-no">No</td>
  <td class="fw-ok">OK</td>
</tr>
</tbody>
</table>
</div>

<span class="fw-ok">OK</span>: Feature is (almost) fully supported. Some rarely used parts may be missing, though.<br>
<span class="fw-part">Partial</span>: Feature is essentially supported, but some important parts are still missing. <br>
<span class="fw-no">No</span>: Feature is not supported at all.

!!! important
    Some existing features may disappear after a firmware update. If you require a special feature, make sure it is still available after the firmware has been updated, _before_ performing the update. It is **not** possible to downgrade to an older firmware version again, so do not update if in doubt.

## Other Firmware Versions

Your firmware version is not listed above?

If the structure version (the number given in brackets) still matches, other firmware versions may be supported as well, but are then untested.

If the structure version is unknown, _pyquaero_ refuses to connect to the Aquaero device. More or less extensive changes to the source code are then needed to make this firmware version work.

If you was able to add support for another firmware or structure version, please send in a pull request!

## Latest Firmware

[Aqua Computer GmbH & Co. KG](https://www.aquacomputer.de) has donated an Aquaero LT for development purposes to this project. It allows me to reverse engineer the latest Aquaero firmware, and eventually support it in _pyquaero_.

Although this is good news, there are some caveats:

* It may take a while until the latest firmware is supported by _pyquaero_. If you rely on a working _pyquaero_, do not update the firmware of your Aquaero until it is supported.
* There is no guarantee that a firmware version will be supported by _pyquaero_. It still bases on reverse engineering, which may turn out to be impossible.
* Even though Aqua Computer donated an Aquaero device to this project, it does not mean that they officially support or endorse it. You are still using _pyquaero_ at your own risk!
