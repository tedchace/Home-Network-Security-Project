<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Findings

## Evidence standard

This assessment is grounded in 11 indexed [Nmap images](../evidence/04-nmap/README.md) and eight [Wireshark images](../evidence/05-wireshark/README.md), plus [Splunk screenshots and a dashboard export](../evidence/06-splunk/README.md). Observed exposure is not a confirmed exploitable vulnerability. Service labels and fingerprints are observations, not proof of a vulnerable product version, successful authentication, or compromise.

| Finding | Observed evidence | Security relevance and limits |
|---|---|---|
| IoT systems shared the Main LAN | [N01](../evidence/04-nmap/01-initial-main-lan-discovery.png) shows Garage Door Controller at 192.0.2.22 and Pool Controller at 192.0.2.27 alongside user endpoints. | Supports reviewing trust-zone placement; membership alone does not establish unrestricted communication between every pair of devices. |
| Pool Controller Telnet-compatible exposure | [N04](../evidence/04-nmap/04-pool-controller-tcp23-telnet-exposure.png) shows TCP/23 open, labeled telnet, with an unrecognized response fingerprint containing Nucleus Shell text. TCP/8080 is filtered. | A reachable legacy remote-access service warrants review. This does not prove unauthenticated shell access, successful login, a CVE, or Internet exposure. The filtered 8080 result is not an open HTTP proxy finding. |
| Garage Door Controller HTTP metadata exposure | [N06](../evidence/04-nmap/06-garage-door-http-exposure.png) shows TCP/80 open and an HTTP 200 JSON response with device and network metadata. | Local information exposure is demonstrated for the scan probes. Remote actuation, authentication bypass, and Internet accessibility were not established. |
| Windows endpoint services | [N02](../evidence/04-nmap/02-windows-endpoint-service-enumeration.png) shows 135, 139, 445, 902, and 912 open on 192.0.2.40; [N03](../evidence/04-nmap/03-vmware-netstat-tasklist-corroboration.png) corroborates VMware ownership of 902/912. | Review required services and host firewall scope. Nmap's VMware description mentions VNC/SOAP; this does not establish a separate VNC server or VNC vulnerability. No SMB exploitability or authentication weakness is established. |
| Printer services (supporting inventory) | [N05](../evidence/04-nmap/05-printer-service-enumeration.png) shows TCP 80, 443, 515, 631, 9100, 9876, 9877 open on 192.0.2.24. | Supports service inventory and exposure review. Nmap's jetdirect? and Clam AV labels are not independently verified product identifications; do not infer antivirus deployment or vulnerabilities from them. |

## Segmentation observations

[N08](../evidence/04-nmap/08-post-segmentation-main-lan-discovery.png) does not display the original IoT entries on Main; [N09](../evidence/04-nmap/09-post-segmentation-guest-iot-discovery.png) displays matching device hostnames on Guest: Garage Door Opener 198.51.100.21 and Pool Controller 198.51.100.22. Together with the reported migration, this supports relocation of the selected devices. Confirm identity with router inventory/MAC records when integrating fuller evidence; IP changes alone do not prove identity.

[N10](../evidence/04-nmap/10-main-to-guest-tcp23-filtered.png) records a Main-to-Guest TCP/23 result of `filtered`. This supports restricted reachability on that tested path at that time, not universal or bidirectional isolation. See [remediation and validation](../documentation/remediation-validation.md).

## Comparison interpretation

[N11](../evidence/04-nmap/11-pre-post-network-comparison.png) reports three hosts no longer observed on Main: the former Pool Controller and Garage Door Controller addresses and laptop 192.0.2.74. Only the two IoT devices have corroborating Guest discovery here. The laptop's absence is unexplained and is not counted as a segmentation success. The newly observed 192.0.2.82 is not automatically a new physical device. TCP/5432 disappearing from the correlated workstation is an observed service change, not proof that software was removed or a vulnerability fixed.

The comparison screenshot is derived evidence. Its supplied XML and Python identity-matching logic have now been reviewed and the metrics reproduced; see the reconciliation below. This does not establish the cause of every change.

## Wireshark observations

| Observation | Evidence | Interpretation |
|---|---|---|
| Client/router DNS resolution | [W01](../evidence/05-wireshark/01-dns-resolution-analysis.png) | 192.0.2.83 receives A/AAAA answers for example.com from 192.0.2.1. The gateway PTR returns No such name. This does not validate upstream Cloudflare use, malware blocking, or DNSSEC. |
| Capture protocol distribution | [W02](../evidence/05-wireshark/02-protocol-hierarchy-baseline.png) | 846 frames, including 249 ARP frames (29.4%). This is a sample of observed traffic, not a whole-network health assessment; protocol hierarchy percentages overlap. |
| Repeated controller broadcasts | [W03](../evidence/05-wireshark/03-pool-controller-broadcast-endpoints.png), [W04](../evidence/05-wireshark/04-pool-controller-broadcast-conversation.png), [W05](../evidence/05-wireshark/05-pre-segmentation-icmp-request-reply.png) | Filtered endpoint/conversation statistics and repeated ARP requests support the observation. The controller MAC 02:00:00:00:00:01 maps to 192.0.2.27 in W05. No ARP poisoning, malicious intent, fault, or performance impact is established. Counts from separate views are not combined. |
| Pre-segmentation ICMP reachability | [W05](../evidence/05-wireshark/05-pre-segmentation-icmp-request-reply.png) | Four visible request/reply pairs between 192.0.2.83 and 192.0.2.27 confirm bidirectional ICMP for those exchanges. |
| TCP/23 response with incomplete handshake | [W06](../evidence/05-wireshark/06-pre-segmentation-tcp23-incomplete-handshake.png) | SYN/ACK responses and retransmissions show responsiveness; no final ACK or application data is displayed in this capture. |
| Telnet negotiation corroborates Nmap | [W07](../evidence/05-wireshark/07-pre-segmentation-tcp23-telnet-negotiation.png) | A separate exchange shows SYN/SYN-ACK/ACK and data decoded as TELNET, including option negotiation. This strengthens protocol identification without proving authentication, command execution, or exploitation. Zero-window annotations alone do not establish a vulnerability. |
| Post-segmentation ICMP replies not observed | [W08](../evidence/05-wireshark/08-post-segmentation-main-to-guest-icmp.png) | 192.0.2.92 sends four requests to each of 198.51.100.21 and 198.51.100.22, all marked no response found. Consistent with the intended restriction; capture limitations and alternate causes remain. |

The ICMP post-test and Nmap filtered TCP/23 test concern different protocols and source addresses. Together with Guest discovery they support a scoped segmentation outcome; they do not establish all-port, reverse-direction, or Guest-client isolation. The Garage Door Controller has no pre-segmentation ICMP baseline in this image set, so its post-test should not be described as a demonstrated before/after ICMP change.

## Splunk observations

[S14](../evidence/06-splunk/14-pre-post-comparison-and-missing-hosts.png) explicitly displays 39 → 34 open TCP service rows and 5 → 1 classified service rows. These are displayed dataset changes (approximately 12.8% and 80%), not confirmed vulnerability reductions or changes attributable entirely to segmentation. The missing laptop remains unexplained; its baseline SMB/VNC rows must not be counted as remediated simply because they disappear.

[S06](../evidence/06-splunk/06-security-relevant-port-classification.png) adds baseline service observations for laptop 192.0.2.74: TCP/445, 5800 and 5900. These are distinct from the earlier VMware 902/912 observations on the other workstation. Service labels and classifications do not establish authentication weakness or exploitation. [S13](../evidence/06-splunk/13-post-segmentation-classified-service.png) shows one remaining classified row: workstation 192.0.2.83 TCP/445; unclassified services still require contextual review.

[S03](../evidence/06-splunk/03-asset-field-extraction.png) contains duplicate gateway rows, and [S04](../evidence/06-splunk/04-service-inventory-all-states.png) includes filtered ports. Neither asset row count nor total expanded port count should be reported as unique hosts/open services without validation.

[S15](../evidence/06-splunk/15-windows-failed-login-detection-logic.png) shows failed-login query results and [S16](../evidence/06-splunk/16-windows-failed-login-alert-trigger.png) records an enabled scheduled alert trigger. This supports detection implementation and a recorded lab trigger, not a confirmed attack. The two account rows may share underlying events and are not evidence of six unique failures. See [Splunk analysis](../documentation/splunk-analysis.md) for query semantics and limits.

## Other project findings awaiting evidence integration

Controlled wireless credential recovery and WPA2/WPA3 hardening are described in the user's workflow notes; wireless evidence is now integrated with the limits described in [wireless analysis](../documentation/wireless-assessment.md). [Python and XML results](../evidence/07-python/README.md) are verified for the supplied files.

## Python and XML reconciliation update

[Source-data verification](../documentation/python-xml-validation.md) now reproduces the 12/39 → 10/34 Main counts and 5 → 1 classification. Both provided inventories match regenerated CSV records, and the supplied report matches regenerated line content allowing ordering differences. The Guest XML matches the Garage Door Controller/Pool Controller MAC addresses across subnets and shows their TCP/80 and TCP/23 services still open on Guest. These checks do not validate unpublished Splunk panel queries or Windows event extraction.

The net five-service decline includes the missing laptop, missing workstation PostgreSQL service and newly observed host, not only IoT migration. [Workflow notes](../documentation/project-workflow.md) report cloud-app usability and WPA2/WPA3 hardening; these are attributed user observations rather than newly measured results.

## Wireless assessment evidence

[Wireless analysis](../documentation/wireless-assessment.md) documents successful handshake capture, a failed initial dictionary, and Aircrack-ng KEY FOUND with a five-entry custom list containing the correct candidate. This confirms controlled offline candidate recovery, not a cryptographic break or general brute-force feasibility. Subsequent network entry is reported by the user but not shown.

The initial WPA3 image shows an enablement confirmation dialog with UPnP enabled. The [later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png) corroborates applied WPA3 enablement and UPnP disablement. Stronger-PSK configuration remains user/workflow-reported; negotiated client security, active mappings, WAN exposure and post-change effectiveness are not established.

## Google Home configuration and operational evidence

[Deployment screenshots](../evidence/01-deployment/README.md) corroborate the three-point topology, office NAT mode, two bridge-mode nodes, Main /24 addressing and DHCP pool 192.0.2.20–192.0.2.250. The app shows both mesh nodes with Great connection and records 975/966 Mbps download/upload on September 9. Ten historical tests support repeated performance checks, without proving uninterrupted stability or a quantified improvement over the prior plan.

[Hardening screenshots](../evidence/02-hardening/README.md) show Custom DNS 1.1.1.2 and Guest enabled. DNS-blocking efficacy, the secondary resolver and Guest sharing exceptions are not demonstrated by these views. Family Wi-Fi groups represent management organization, not extra isolated segments. The Guest-password display option is checked; no password is visible in these Guest screenshots.
