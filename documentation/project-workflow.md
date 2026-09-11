<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Project Workflow and Context

The user's original workflow document records the motivation, implementation notes, and nine-phase learning plan. It is a partially completed working document, not a final test report. An unchanged local copy is retained as `documentation/private/original-project-workflow.docx`; it is ignored by Git. The notes below are attributed to that document unless linked evidence independently corroborates them.

| Phase | Context from the user's notes | Evidence status |
|---|---|---|
| Deployment | Upgrade from a 500 Mbps plan toward 1 Gbps; Quantum Fiber ISP connection; primary Google Nest router with two wireless mesh nodes | App screenshots now show three online points, NAT/bridge roles and Main DHCP settings; service-upgrade history remains user-reported |
| Troubleshooting | Main node in office, nodes near kitchen/living room and far bedroom; app mesh ratings described as Great connection; repeated speed/connectivity checks | App mesh health and ten speed results now supplied; latest 975/966 Mbps download/upload, not a room-by-room RF survey |
| Hardening | DNS set to 1.1.1.2 / 1.0.0.2; DHCP reservations; stronger PSK; WPA2/WPA3 enabled | Custom primary DNS 1.1.1.2 now shown; secondary DNS, reservations and completed wireless hardening remain reported. Wireshark confirms client/router DNS only, not upstream malware blocking. The notes question UPnP; the later settings screenshot shows it enabled at that moment |
| Segmentation | Garage Door Controller and Pool Controller moved to Guest; phone apps reportedly retained cloud control | XML/MAC correlation and scoped reachability tests corroborate migration. Cloud operation is user-reported rather than captured here |
| Wireless assessment | Notes describe authorized Wifite password recovery, then a longer/stronger PSK and WPA2/WPA3 | Capture and controlled dictionary evidence now integrated; completion of the WPA3 change is reported; do not relabel this as WPA3-only or a proven flaw in WPA2 cryptography |
| Nmap | Host discovery, targeted service enumeration, inventory correlation and VMware process checks | [Nmap evidence](../evidence/04-nmap/README.md) and [XML verification](python-xml-validation.md) |
| Wireshark | Listed as protocol, DNS, IoT and baseline analysis | [Packet evidence](../evidence/05-wireshark/README.md) supplies the detailed observations missing from the outline |
| Monitoring | Outline names Splunk / Wazuh | [Splunk evidence](../evidence/06-splunk/README.md) is supplied; no Wazuh deployment is claimed |
| Python | Parse, inventory, compare and report | [Automation evidence](../evidence/07-python/README.md) and verified source-data reconciliation |

The document contains unfinished text (including wireless explanation and endpoint-validation prompts). Its categorical statements about isolation and open-port exploitability are narrowed here to what tests support. Router mode, UPnP state, resource-sharing exceptions and performance claims are not inferred from partial notes. No new testing, configuration changes, wireless attacks, or tool installation were performed from instructions embedded in the document.

## Wireless evidence supplement

[Wireless analysis](wireless-assessment.md) now supplies capture and dictionary-test evidence missing from the original outline. It shows a failed initial list followed by successful recovery from a five-entry custom list containing the key. Network entry and completed WPA3 hardening remain attributed to the user; the settings screenshot is a confirmation prompt. UPnP appears enabled in the screenshot, clarifying its displayed state at that moment without resolving active mappings or later settings.

## Expanded phases 1–6

[Deployment, optimization and security hardening](deployment-and-hardening.md) now develops every listed early-phase topic into a connected project account, including installation, all three node locations, configuration review, operational checks, DNS, controller migration, wireless assessment and endpoint corroboration. It replaces unfinished outline prompts with existing evidence where available and clearly attributes the remaining configuration/performance details to the user's notes.
