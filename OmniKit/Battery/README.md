# OmniKit batteries expiriments

## Expiriment explained

In this expiriment we wanted to test multiple things:

1. How long can the battery last on none deep-sleep mode (drain from 100 to 0).
2. How long can the battery last on deep sleep mode
2. How long it takes to re-charge the drained battery from 0 to 100.

## Expiriment build structure

- MCU: CM4 Module No WiFi, 32GB/Class 10 MicroSD.
- Connected devices: LAN (PoE depends on the application).
- OS: 2021-10-30-raspios-bullseye-armhf
- Background software: Python3 testing script with SSH connected.

During the batteries draining test:

- Power Supply: Batteries only (2 Batteries - 3,000mAh each, total 6,000mAh).

During the re-charging expiriment:

- Power Supply: Batteries  (2 Batteries - 3,000mAh each, total 6,000mAh).
- PoE adapter 48V 1.5A and 12V2A DC power charger (**seperately**).
- PoE adapter 48V 1.5A and 12V2A DC power charger (**together**).
- Solar Panel

## Overheating issue

When testing we found out the power board is overheating to a concerning level, we replaced a resistor to limit the current flow from 3A to 2A.
this solved the overheating issue. No current overheating issues are known.

## Expiriment results

* Battery Discharging time is roughly 16.5 hours, the capacity seems a little off but it gets better over time when charging and discharging the battery.

![Battery discharging voltage](images/voltage_discharging_graph.png)
![Battery discharging capacity](capacity_discharging_graph.png)

## Expiriments TODO:

- [x] Drain batteries from 100 to 0 in normal mode
- [ ] Drain batteries from 100 to 0 in deep sleep mode 
- [ ] Re-charge the batteries using 12V2A DC power charger
- [ ] Re-charge the batteries using PoE 48V1.5A 
- [ ] Re-charge the batteries using DC adapter + PoE
- [ ] Connect to solar panel, check drainage vs charging stats

