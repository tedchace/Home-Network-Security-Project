<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Deployment and optimization evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

Original Google Home screenshots supplied by the user, published as redacted derivatives. The [workflow account](../../documentation/deployment-and-hardening.md) supplies installation and placement context. The original filename plan (private; not published) is retained.

| ID | Screenshot | Observation |
|---|---|---|
| D01 | [Home overview](01-google-home-network-overview.png) | Office and two Nest Wifi Pro tiles; network test shortcut |
| D02 | [Wi-Fi status](02-mesh-status-overview.png) | Three points online, 10-device snapshot; instantaneous usage is not a speed-test result |
| D03 | [Main LAN](03-main-lan-configuration.png) | 192.0.2.1, 255.255.255.0; DHCP 192.0.2.20–192.0.2.250 |
| D04 | [Device modes](04-mesh-device-modes.png) | Office NAT standard; two nodes Bridge; app says automatically set |
| D05 | [Point health](05-mesh-point-health.png) | Both additional points rated Great connection |
| D06 | [Internet speed](06-network-speed-validation.png) | September 9: 975 Mbps download, 966 Mbps upload |
| D07 | Speed history (private screenshot; transcription below) | Ten visible results, transcribed below |
| D08 | [Earlier speed history](07-speed-history-improvement.png) | August 18 and 20 lower results followed by repeated higher August 21 results |

| Displayed date | Download Mbps | Upload Mbps |
|---|---:|---:|
| Yesterday (September 9 in D06) | 975 | 966 |
| September 8 | 954 | 974 |
| September 6 | 815 | 976 |
| September 5 | 939 | 977 |
| September 4 | 917 | 975 |
| September 3 | 919 | 969 |
| September 1 | 956 | 950 |
| September 1 | 788 | 819 |
| August 31 | 956 | 982 |
| August 29 | 942 | 989 |

Earlier history in D08 shows two lower visible tests before the later high-throughput cluster:

| Displayed date | Download Mbps | Upload Mbps |
|---|---:|---:|
| August 18 | 435 | 246 |
| August 20 | 539 | 242 |
| August 21 | 836 | 736 |
| August 21 | 827 | 907 |
| August 21 | 924 | 973 |
| August 21 | 985 | 959 |
| August 21 | 778 | 796 |
| August 21 | 831 | 838 |
| August 21 | 941 | 975 |
| August 21 | 844 | 906 |
| August 21 | 984 | 985 |

The year is not displayed. These app-reported Internet tests are not per-room client Wi-Fi measurements or continuous uptime monitoring. No numerical pre-upgrade baseline establishes a percentage improvement. Mode settings do not establish upstream ISP bridge mode or absence of double NAT. The device count is a separate snapshot from Nmap discovery.

[Source hashes](source-map.csv) document the public derivatives. Public derivatives have been sanitized; original evidence is retained privately.
