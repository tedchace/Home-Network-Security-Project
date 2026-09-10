<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Home Network Project Security Report

## Security Report Overview

This report was automatically generated from Nmap XML reconnaissance data collected before and after network segmentation. The Python script compares discovered hosts and open network services to document observed changes in the Main LAN attack surface.

## Pre-Segmentation State

- Hosts observed: 12
- Open services observed: 39

## Post-Segmentation State

- Hosts observed: 10
- Open services observed: 34

## Network State Changes

### Hosts No Longer Observed from the Main LAN

- 192.0.2.27 - pool-controller.example.invalid
- 192.0.2.74 - laptop.example.invalid
- 192.0.2.22 - garage-controller.example.invalid

### Newly Observed Hosts

- 192.0.2.82 - Unknown

## Service Exposure Changes

### workstation.example.invalid

- current IP address: 192.0.2.83
- Services no longer observed:
  - 5432/tcp - postgresql

## Segmentation Assessment

The post-segmentation Main LAN scan showed changes in observed hosts compared to the results from the pre-segmentation Main LAN scan. The Pool Controller and  Garage Door Opener, which were previously observed on the Main LAN, were no longer observed in the post-segmentation Main LAN scan. This result is consistent with the intended migration of these IoT devices to the segmented Guest Network.

## Additional Notes

A host or service not appearing in a later network scan does not by itself prove that the asset or service was removed or successfully segmented. Devices may be offline, asleep, dynamically addressed, filtered, or otherwise unavailable during collection. Guest Network discovery, network configuration, device inventory, and isolation testing can provide additional evidence when validating segmentation. Automated comparison results should therefore be interpreted alongside these supporting data sources.