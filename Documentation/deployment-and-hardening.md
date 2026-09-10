<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Deployment, Optimization and Security Hardening

## Source and evidence standard

This account expands phases 1–6 of the user's original Router Configuration & Test Project Workflow. Configuration and usability details attributed to the notes are part of the project record; they are not substitutes for independent measurements. Existing screenshots and XML corroborate the assessment and segmentation results where linked. The original DOCX remains unchanged in the local ignored Documentation/private directory. Its unfinished prompts were not treated as instructions to run new tests.

## 1. Network deployment

### Router installation and configuration

The project began as a home infrastructure upgrade from a 500 Mbps Internet plan toward a 1 Gbps service target, coupled with improved wireless coverage. The user reports deploying a Google Nest router connected by Ethernet to the Quantum Fiber ISP device. Two additional Nest units provided wireless mesh coverage.

The Google Home application was configured with the homeowner's administrative account to establish and manage the network. Initial wireless setup used a new SSID and WPA2-PSK. The service target and cable choice describe the deployment intent; they do not demonstrate a measured throughput above 1 Gbps or verify negotiated Ethernet speed.

### Mesh topology deployment

| Location | Role | Placement rationale from the notes |
|---|---|---|
| Office | Primary router beside the ISP connection | Prioritize office connectivity and proximity to the wired uplink |
| Kitchen/living room | Wireless mesh node | Cover frequently used common areas with fewer intervening obstacles |
| Far bedroom | Wireless mesh node | Extend coverage to the opposite end of the house and nearby outdoor IoT devices |

The nodes were powered, joined and tested through Google Home. The [mesh health screenshot](../evidence/01-deployment/05-mesh-point-health.png) shows both additional points rated Great connection. This corroborates the notes at the time of capture; there is no supplied RF survey, floor plan, node-distance measurement or latency series from which to quantify coverage improvement. The notes describe wireless inter-node connections, not wired backhaul.

### Wireless configuration

The configuration work covered SSID/PSK selection, LAN address and subnet, DHCP pool and reservations, device/router naming, Guest networking, and review of NAT/bridge and UPnP settings. The [LAN settings](../evidence/01-deployment/03-main-lan-configuration.png) show router 192.0.2.1, mask 255.255.255.0 and DHCP pool 192.0.2.20–192.0.2.250. [Device modes](../evidence/01-deployment/04-mesh-device-modes.png) show Office Wifi in NAT (standard) mode and both additional nodes in Bridge mode; the app says these modes were automatically set. Specific reservations and the upstream ISP device mode remain undocumented.

### Device connectivity

The user connected household devices using the wireless password and checked Internet access, device speeds and local interaction, including phone-to-TV communication. Later notes describe WPA2/WPA3 mixed-mode operation to improve wireless security while maintaining compatibility for older devices. These are user-reported functional checks rather than captured association or throughput measurements. Device discovery and inventory later supplied a more systematic view of the environment.

## 2. Troubleshooting and optimization

### Connectivity troubleshooting

The notes describe a layered troubleshooting sequence during an Internet outage. The user first treated the issue as a possible laptop problem by restarting the wireless driver, then tested from a phone and confirmed that multiple client devices lacked connectivity. The router and ISP device were power cycled, direct Ethernet connectivity to the ISP device was checked from a laptop, and `ipconfig /renew` was run from Windows. The renewal response indicated that the DHCP server was unreachable or not responding, shifting the investigation away from a single endpoint and toward upstream modem/ISP behavior. A hard reset left the ISP device unable to reconnect for an extended period, and service was restored after modem firmware remediation.

These steps document practical fault isolation and escalation from endpoint checks to network-edge testing. The project treats the result as consistent with upstream DHCP or modem firmware failure; no ISP ticket, modem log or packet trace is supplied that would independently prove the root cause.

### Mesh and node placement

Placement was chosen around the office, common spaces and far bedroom to balance the household's usage patterns with coverage needs. The reported mesh ratings and application checks informed placement. There is no controlled before/after signal survey establishing an optimal physical layout, so the design is described as chosen for the household rather than mathematically optimized.

### Wi-Fi performance testing

Google Home tests were used to inspect performance over time. The [Internet speed result](../evidence/01-deployment/06-network-speed-validation.png) records 975 Mbps download and 966 Mbps upload for September 9. The [later visible history](../evidence/01-deployment/07-network-performance-history.png) shows ten results spanning August 29–September 9, ranging from 788–975 Mbps download and 819–989 Mbps upload. The [earlier visible history](../evidence/01-deployment/08-speed-history-improvement.png) includes lower August 18 and August 20 results followed by repeated higher August 21 measurements. The year is not displayed. These are app-reported Internet speed measurements; they do not establish phone Wi-Fi throughput in every room. No controlled pre-upgrade baseline supports a precise percentage improvement claim.

### Stability and performance validation

The workflow reports daily/weekly application checks of speeds, Internet usage and connectivity. This documents repeated operational observation, not an uptime SLA or an established packet-loss/latency baseline. The [deployment index](../evidence/01-deployment/README.md) now records the visible speed history and screenshots showing all three points online. Repeated successful tests support operational checks, but do not establish uninterrupted uptime.

## 3. Security hardening

### Router configuration review

The user reviewed LAN settings, DHCP reservations/pool, and ISP bridge/NAT considerations. The notes state that both the modem and router initially assigned private addresses, creating a double NAT condition, and that the modem was placed into bridge/invisible mode so the Nest router handled routing and DHCP. A final modem export is not supplied, so bridge mode remains documented rather than independently proven. The notes state no port-forwarding rules. [The later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png) shows WPA3 enabled, UPnP disabled, IPv6 disabled, Custom DNS selected, and the WAN settings menu available.

### DNS configuration and Cloudflare malware-blocking DNS

The notes report changing the router's default ISP-assigned DNS configuration to 1.1.1.2 and 1.0.0.2 for the intended malware-blocking DNS control. The [DNS settings screenshot](../evidence/02-hardening/01-cloudflare-security-dns.png) corroborates Custom DNS selected with 1.1.1.2 displayed. The secondary 1.0.0.2 address remains workflow-reported because it is not visible. No evidence establishes that the prior ISP resolvers were less reliable, so that comparative claim is not carried forward.

[Wireshark DNS evidence](../evidence/05-wireshark/01-dns-resolution-analysis.png) shows the client querying the router and receiving A/AAAA answers. It verifies that particular client/router exchange, not upstream resolver selection, blocking efficacy or DNSSEC validation. The router settings screenshot documents configuration selection; a controlled blocking test remains separate evidence. No new DNS tests were run during this update.

### Device inventory

The user recorded device purpose/IP, named devices and reserved addresses for selected important systems, including security equipment. Later Nmap results added hostnames, MAC/vendor hints and service observations. Inventory includes user endpoints, security devices, printer, TV, and the two household controllers. [Family Wi-Fi](../evidence/02-hardening/02-device-grouping.png) shows Printer (1), Security System (4), Smart TV (1), and Trusted Devices (11) groups, all with SafeSearch off and no schedules set. These are management groups, not VLANs or demonstrated isolation boundaries. Group membership totals and the overview's 10-device snapshot are not interchangeable with Nmap host counts. Names and vendor hints inform identification but are not conclusive by themselves; the two IoT migrations are corroborated by unchanged MAC addresses in XML.

### Reduction of unnecessary exposure

Controls recorded in the workflow include a longer/stronger wireless PSK, reported WPA2/WPA3 mixed-mode operation, restricted resource sharing, disabling UPnP, and moving selected IoT devices to Guest. The wireless screenshot shows the WPA3 confirmation prompt, and the later advanced settings screenshot shows WPA3 on and UPnP off at the time of capture. Negotiated client modes remain user-reported. The Guest move reduces the tested Main-to-IoT reachability while leaving the services available on Guest; it does not demonstrate that the services themselves were disabled.

## 4. Network segmentation

### Trusted Main network

Main uses 192.0.2.0/24 with gateway 192.0.2.1. The intended role is trusted personal devices and retained household infrastructure such as security equipment and the printer. This is selective segmentation, not a claim that every IoT device left Main.

### Guest and IoT network

Guest uses 198.51.100.0/24 with gateway 198.51.100.1. The design uses the router's Guest capability as the separation mechanism. [Guest settings](../evidence/02-hardening/03-guest-iot-network-configuration.png) show the Guest network enabled with a separate named SSID and masked password. The option to show its password on voice-assistant displays is checked. The shared-device list is below the visible area; enabled sharing exceptions cannot be determined. Guest subnet addressing comes from the scan evidence, not this settings screen. The workflow discusses optional sharing of selected Main resources through Google Home, but does not establish which exceptions were enabled. No custom VLAN or firewall-policy deployment is claimed from these notes.

### Garage and pool controller migration

| Device | Original Main address | Guest address | Evidence and operational outcome |
|---|---|---|---|
| Garage Controller | 192.0.2.22 | 198.51.100.21 | Matching MAC in XML; HTTP TCP/80 remains open on Guest; phone-app cloud control reported functional |
| Pool Controller | 192.0.2.27 | 198.51.100.22 | Matching MAC in XML; Telnet-compatible TCP/23 remains open on Guest; phone-app cloud control reported functional |

The notes describe moving each controller through its phone application and checking Guest connectivity and cloud usability afterward. [XML verification](python-xml-validation.md) independently corroborates identities and network placement; app usability remains an attributed test result.

### Isolation validation

[Nmap](../evidence/04-nmap/10-main-to-guest-tcp23-filtered.png) records Main-to-Guest TCP/23 filtered. [Wireshark](../evidence/05-wireshark/08-post-segmentation-main-to-guest-icmp.png) records requests to both Guest devices without observed ICMP replies. The pool controller had replied to Main ICMP before migration. These tests support the tested direction/protocols; they do not establish Guest-to-Main isolation, complete IPv6 coverage, all-port isolation or absence of sharing exceptions. [Validation](remediation-validation.md) records the exact limits.

## 5. Wireless security assessment

### Authorized Wifite testing

The user reports using bootable Kali Linux to assess their own wireless network. [Wifite evidence](../evidence/03-wifite/README.md) shows discovery of the selected home target, handshake capture and tool validation, followed by failure of the initial dictionary. Aircrack-ng then reports successful recovery using a five-entry custom wordlist containing the matching candidate. This is controlled offline dictionary verification; the workflow's broad brute-force wording is narrowed to the observed method.

### Evaluation and hardening

The result demonstrates that a matching password candidate can validate against that capture; it does not show a general cryptographic break. Subsequent network entry and a stronger PSK are reported by the user. The WPA3 confirmation screenshot documents initiating the configuration change, and the later advanced settings screenshot shows WPA3 enabled. There is no supplied post-change client negotiation or repeat-test evidence establishing mitigation effectiveness. [Wireless analysis](wireless-assessment.md) provides the detailed assessment.

## 6. Nmap network and attack-surface assessment

### Host discovery and asset correlation

The workflow describes checking local addressing with ipconfig /all, then using Zenmap host discovery against the identified subnet. [Initial Main discovery](../evidence/04-nmap/01-initial-main-lan-discovery.png) records the starting inventory. Hostnames and vendor labels helped map devices to household roles; vendor names are not evidence of contacting a manufacturer's website. Discovery is a snapshot and may miss unavailable or nonresponding assets.

### Port enumeration and service detection

Targeted service scans examined the assessment workstation, security devices, printer and IoT controllers. [The Nmap index](../evidence/04-nmap/README.md) connects each device scan to visible port states and service labels. TCP/23 on Pool Controller and TCP/80 on Garage Controller motivated exposure review; open ports alone do not establish exploitable vulnerabilities. The later Main XML scans use the same 1,000 TCP-port list and service detection, not exhaustive TCP/UDP testing.

### IoT exposure analysis

The controllers needed network access for their household functions. Moving them to Guest retained a path for their reported cloud operation while reducing direct reachability from trusted endpoints in the tested cases. The finding is unnecessary shared exposure and a scoped boundary improvement, not proof that either device was compromised.

### Endpoint validation

The workflow's unfinished endpoint-validation prompt is completed by the supplied [local process evidence](../evidence/04-nmap/03-vmware-netstat-tasklist-corroboration.png): netstat shows TCP/902 and TCP/912 listeners associated with PID 6388, and tasklist maps that PID to vmware-authd.exe. This corroborates the VMware service identification at that observation. It does not independently validate software patch state or prove a separate VNC vulnerability.

### Before and after segmentation testing

The [Python/XML reconciliation](python-xml-validation.md) verifies Main changes from 12 to 10 hosts and 39 to 34 open service records, with matching IoT MACs appearing on Guest. The missing laptop, missing PostgreSQL observation and newly seen host explain additional changes and are not automatically remediation successes. Guest XML has a /24 argument but a four-target run summary; complete Guest coverage is not asserted. Findings, packet tests and user-recorded operational checks are interpreted together.

## Continuation into monitoring and automation

Phases 1–6 establish the network, baseline and control changes. The existing [Wireshark](../evidence/05-wireshark/README.md), [Splunk](splunk-analysis.md), and [Python](python-xml-validation.md) documentation then adds packet-level analysis, service analytics, a recorded failed-login alert and reproducible source-data comparison. These later sections supplement the workflow's initially unfinished outline.
