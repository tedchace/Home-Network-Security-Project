<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Remediation and Validation

## Control implemented

Project context reports migration of the Garage Controller and Pool Controller from Main (192.0.2.0/24) to Guest/IoT (198.51.100.0/24). The goal was to reduce direct exposure to trusted endpoints while retaining needed device functionality. These screenshots support network-placement and targeted reachability observations; they do not document disabling the services or validate cloud functionality.

| Validation step | Evidence | Result and boundary |
|---|---|---|
| Establish original exposure | [N01](../evidence/04-nmap/01-initial-main-lan-discovery.png), [N04](../evidence/04-nmap/04-pool-controller-tcp23-telnet-exposure.png), [N06](../evidence/04-nmap/06-garage-door-http-exposure.png) | Main discovery includes both IoT devices; Pool Controller TCP/23 and Garage Controller TCP/80 are open in selected service scans. |
| Establish Guest baseline | [N07](../evidence/04-nmap/07-guest-network-initial-discovery.png) | Guest topology displays gateway and workstation only; this is not proof of complete Guest inventory. |
| Recheck Main | [N08](../evidence/04-nmap/08-post-segmentation-main-lan-discovery.png) | Original IoT entries are not displayed. Absence alone is insufficient to prove isolation. |
| Locate devices on Guest | [N09](../evidence/04-nmap/09-post-segmentation-guest-iot-discovery.png) | Matching Garage Controller and Pool Controller hostnames appear at 198.51.100.21 and .22; supports the reported migration. |
| Test Main-to-Guest TCP/23 | [N10](../evidence/04-nmap/10-main-to-guest-tcp23-filtered.png) | At 2026-09-04 14:42 EDT, `nmap -Pn -p 23 198.51.100.22` returns `23/tcp filtered telnet`. Screenshot shows Main Wi-Fi address 192.0.2.88 and gateway 192.0.2.1. |
| Compare network states | [N11](../evidence/04-nmap/11-pre-post-network-comparison.png) | Derived output identifies missing IoT entries plus unrelated host/service differences. It does not establish the cause of every difference. |

## Interpretation of the targeted test

The scanner could not determine an open/closed state for TCP/23 on the tested path. This is consistent with filtering and supports the intended restriction, but it does not identify the enforcing device or rule. The screenshot includes another adapter, and no route table or packet trace; the Wi-Fi configuration supports Main attachment without independently proving the exact egress interface.

The `-Pn` option skips host discovery and treats the target as available for scanning. Consequently, the printed “Host is up” is not independent evidence that the controller responded. The `telnet` label in this port-only scan is not fresh application-level confirmation. This is a change in observed reachability, not proof that Telnet was disabled on the controller.

## Remaining validation boundaries

- No claim of Guest-to-Main isolation, all-port isolation, IPv6 isolation, or isolation between Guest clients follows from this one TCP test.
- Guest XML now confirms the controller's TCP/23 service remains open in the Guest scan; the Main-to-Guest filtered result is a separate path observation.
- Garage Controller HTTP restriction across the boundary was not directly tested in the supplied targeted screenshot.
- The workflow notes report successful cloud-app functionality after migration; direct configuration and application-test evidence remain separate from the scan results.
- Laptop absence and workstation TCP/5432 disappearance remain unexplained scan differences.

## Packet-level validation

| Test | Evidence | Observed result | Supported conclusion |
|---|---|---|---|
| Pre-segmentation pool ICMP | [W05](../evidence/05-wireshark/05-pre-segmentation-icmp-request-reply.png) | 192.0.2.83 → 192.0.2.27 echo requests have matching reverse replies (158/163, 166/167, 171/172, 180/181). | Bidirectional ICMP existed for these exchanges. |
| Pre-segmentation pool TCP/23 probe | [W06](../evidence/05-wireshark/06-pre-segmentation-tcp23-incomplete-handshake.png) | SYN, SYN/ACK, and SYN/ACK retransmissions; no final ACK/data shown. | TCP/23 responded; this particular view does not establish a complete session. |
| Separate pre-segmentation TCP/23 exchange | [W07](../evidence/05-wireshark/07-pre-segmentation-tcp23-telnet-negotiation.png) | 192.0.2.83:52766 ↔ 192.0.2.27:23 handshake (2769/2771/2772), then Telnet negotiation/data. | Packet-level corroboration of the Nmap service exposure, without proof of login or shell access. |
| Post-segmentation ICMP to Guest IoT | [W08](../evidence/05-wireshark/08-post-segmentation-main-to-guest-icmp.png) | 192.0.2.92 sends four echo requests each to 198.51.100.21 and 198.51.100.22; no replies displayed, all requests marked no response found. | No ICMP replies observed for these requests in the supplied capture view. |

For the Pool Controller, the pre/post evidence shows replies on Main before migration and no replies observed when targeted on Guest afterward. For the Garage Controller, only the post-segmentation ICMP observation is supplied. Guest identity is correlated with Nmap discovery. The source addresses differ across the packet tests and the existing 192.0.2.88 TCP/23 test; these are separate observations with no absolute Wireshark capture times shown.

The ICMP result is consistent with the intended restriction and complements Nmap's filtered TCP/23 result. Neither establishes the precise enforcing rule or rules out device availability, routing, or capture visibility as alternative causes. The Guest-IP display filter can omit intermediate-router ICMP errors. These results do not establish reverse-direction, all-protocol, IPv6, or Guest-to-Guest isolation, nor prove the underlying services were disabled. No raw capture was analyzed during this update.

## Splunk validation and monitoring

[S14](../evidence/06-splunk/14-pre-post-comparison-and-missing-hosts.png) provides an explicitly labeled pre/post view: 39 → 34 open TCP service rows and 5 → 1 classified rows. Its missing-host table lists the pool controller, laptop .74 and the garage controller. Nmap/Wireshark support the scoped IoT migration outcome; Splunk's table does not establish why the laptop disappeared. The displayed percentage changes are not vulnerability-remediation rates. XML and panel queries remain necessary for independent count reconciliation.

[S15](../evidence/06-splunk/15-windows-failed-login-detection-logic.png) shows a failed-login threshold search, while [S16](../evidence/06-splunk/16-windows-failed-login-alert-trigger.png) shows a recorded scheduled alert trigger at 2026-09-03 14:00:01 EDT. This validates the presence of query results and a triggered alert, not malicious activity, notification delivery, or a complete investigation. The fixed-bucket semantics, account-field ambiguity and missing schedule details are recorded in [Splunk analysis](splunk-analysis.md).


## Python and network XML verification

[Verification results](python-xml-validation.md) reproduce the Main host/service counts and chosen classification, match both supplied CSVs, and corroborate migration by unchanged device MAC addresses in Guest XML. The Guest scan shows TCP/80 and TCP/23 remain open on the Garage Door Controller and Pool Controller respectively. Same-port lists and subnet scopes make the Main datasets comparable in scan configuration, but availability and timing still differ.

The Guest run summary reports four total targets despite /24 arguments, so exhaustive Guest coverage is not certified. [Workflow context](project-workflow.md) reports preserved cloud functionality, with the evidentiary distinction retained. Deployment screenshots are now integrated. Sanitization and post-hardening wireless validation remain outstanding.

## Wireless hardening validation

[F01](../evidence/03-wifite/01-wlan-discovery-handshake.png) records handshake capture and initial dictionary failure. [F02](../evidence/03-wifite/02-offline-dictionary-validation.png) records successful recovery using a small custom list containing the matching candidate. The user reports subsequent entry; a connection or resource-access test is not shown.

[F03](../evidence/03-wifite/03-wpa3-enablement-confirmation.png) shows Turn on WPA3? awaiting confirmation. The user reports completion and the workflow reports a stronger PSK with WPA2/WPA3. Applied settings, client negotiation and post-hardening testing remain unverified by these images. This should be presented as reported remediation with partial configuration evidence, not proven elimination of the original attack path. See [wireless analysis](wireless-assessment.md).

## Early configuration and usability checks

[The workflow-based account](deployment-and-hardening.md) records Google Home mesh ratings, recurring connectivity/speed checks, DNS reassignment, reservations and reported phone-app usability after both controller migrations. These are valid attributed project records; they do not independently demonstrate measured throughput gains, upstream DNS blocking, the upstream ISP mode or the full router sharing policy. Existing XML and packet evidence remain the basis for the narrower verified segmentation conclusions.

## Google Home configuration corroboration

[Deployment evidence](../evidence/01-deployment/README.md) now shows the Main DHCP range, NAT/bridge roles, all three points online, mesh health and app Internet-speed history. [Hardening evidence](../evidence/02-hardening/README.md) shows Custom DNS 1.1.1.2 and Guest enabled. These corroborate configuration and operational observations; the DNS upstream/blocking path and full isolation policy still require separate tests. The shared-device list is not visible. No new network settings or live tests were performed for this documentation update.
