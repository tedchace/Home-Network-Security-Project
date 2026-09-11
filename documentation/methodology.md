<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Methodology

## Project workflow

Deploy → Baseline → Assess → Identify exposure → Remediate → Validate → Monitor → Automate.

The existing project follows nine phases. Deployment establishes connectivity; troubleshooting establishes a usable baseline; hardening reviews configuration; segmentation introduces a Guest/IoT trust zone; wireless assessment evaluates wireless access controls; Nmap inventories hosts/services; Wireshark examines packets; Splunk supports monitoring/detection; Python supports repeatable comparison and reporting. The phase list is organizational, not a claim that segmentation preceded every baseline scan. This update documents Nmap, Wireshark, Splunk, and Python/XML evidence; other phases retain their project-context status pending evidence integration.

## Nmap assessment sequence

1. Discover Main-LAN hosts with `nmap -sn 192.0.2.0/24` and correlate names with the project inventory ([N01](../evidence/04-nmap/01-initial-main-lan-discovery.png)).
2. Enumerate selected endpoints with `nmap -sV <address>`: Windows 192.0.2.40, Pool Controller 192.0.2.27, printer 192.0.2.24, Garage Door Controller 192.0.2.22 ([N02](../evidence/04-nmap/02-windows-endpoint-service-enumeration.png), [N04](../evidence/04-nmap/04-pool-controller-tcp23-telnet-exposure.png), [N05](../evidence/04-nmap/05-printer-service-enumeration.png), [N06](../evidence/04-nmap/06-garage-door-http-exposure.png)).
3. Corroborate Windows TCP/902 and TCP/912 locally using `netstat -ano` and `tasklist /FI "PID eq 6388"`; both listeners map to `vmware-authd.exe` ([N03](../evidence/04-nmap/03-vmware-netstat-tasklist-corroboration.png)). PID is specific to that observation.
4. Discover the Guest network with `nmap -sn 198.51.100.0/24` ([N07](../evidence/04-nmap/07-guest-network-initial-discovery.png)).
5. After the reported IoT migration, inspect Main and Guest topology screenshots. Their command fields show `nmap -sV 192.0.2.0/24` and `nmap -sV 198.51.100.0/24` ([N08](../evidence/04-nmap/08-post-segmentation-main-lan-discovery.png), [N09](../evidence/04-nmap/09-post-segmentation-guest-iot-discovery.png)); full scan output is not visible.
6. Check Main interface addressing and probe the Guest controller with `nmap -Pn -p 23 198.51.100.22` ([N10](../evidence/04-nmap/10-main-to-guest-tcp23-filtered.png)).
7. Review the derived pre/post comparison ([N11](../evidence/04-nmap/11-pre-post-network-comparison.png)) and separate known migrations from other inventory changes.

These are transcriptions of recorded work, not scans executed during this documentation update. Service scan outputs show Nmap 7.95. Default service scans are not exhaustive all-port/UDP assessments, and host discovery is not a complete asset inventory.

## Evidence handling and interpretation

The [evidence index](../evidence/04-nmap/README.md) records original names, repository names, visible times, observations, and caveats. Original images are preserved privately. Published images use irreversible solid masks, with separate public SHA-256 hashes. Filename numbering follows workflow order with visible timestamps used where available; missing timestamps are not invented.

Use the selected scan output in Zenmap. In the Windows image, the editable target/command bar refers to 192.0.2.27 while selected output describes 192.0.2.40. The sidebar can include accumulated scan results and should not be treated as the result set of every selected scan. Topology colors are not vulnerability severity ratings.

Correlate hostnames, router inventory, and available MAC evidence across DHCP changes. Compare equivalent scan scopes, options, vantage points, and device availability before calculating exposure changes. The initial discovery-only screenshot and later service-scan topology are not equivalent service-count datasets. Preserve uncertainty where raw output, routes, or packet evidence is absent.

## Wireshark analysis sequence

1. Inspect client/router DNS query-response pairs with `dns` ([W01](../evidence/05-wireshark/01-dns-resolution-analysis.png)); distinguish successful A/AAAA resolution from the failed reverse lookup.
2. Review Protocol Hierarchy with no display filter ([W02](../evidence/05-wireshark/02-protocol-hierarchy-baseline.png)). Treat results as capture-specific, accounting for nested protocols.
3. Review filtered Ethernet Endpoints and Conversations ([W03](../evidence/05-wireshark/03-pool-controller-broadcast-endpoints.png), [W04](../evidence/05-wireshark/04-pool-controller-broadcast-conversation.png)), then corroborate repeated ARP in the packet list ([W05](../evidence/05-wireshark/05-pre-segmentation-icmp-request-reply.png)). Record each view's separate counts and filter limitations.
4. Match ICMP echo requests to replies using packet references and sequence numbers ([W05](../evidence/05-wireshark/05-pre-segmentation-icmp-request-reply.png)).
5. Inspect TCP/23 using `ip.addr == 192.0.2.27 && tcp.port == 23` ([W06](../evidence/05-wireshark/06-pre-segmentation-tcp23-incomplete-handshake.png)). Preserve the incomplete-handshake result rather than assuming a session completed.
6. Inspect the separate scan-associated capture filtered by `ip.addr == 192.0.2.27` ([W07](../evidence/05-wireshark/07-pre-segmentation-tcp23-telnet-negotiation.png)). Correlate a complete handshake and Telnet negotiation with Nmap's service identification. Process attribution comes from project context, not packet headers.
7. Review post-segmentation traffic with `ip.addr == 198.51.100.21 || ip.addr == 198.51.100.22` ([W08](../evidence/05-wireshark/08-post-segmentation-main-to-guest-icmp.png)). Record outgoing requests and absent observed replies without treating a dissector warning as proof of a firewall rule.

These steps describe supplied evidence, not new live captures or scans. Wi-Fi 2 is visible in most full-window screenshots; cropped views omit some metadata. Absolute dates and complete capture durations are unavailable. Relative packet times cannot align separate captures. The [Wireshark register](../evidence/05-wireshark/README.md) records the visible filters, counts, interfaces, and limits for each image.

Source addresses vary: pre-segmentation 192.0.2.83, Nmap cross-segment 192.0.2.88, and post-segmentation ICMP 192.0.2.92. Do not combine these into one test session. Filtered views can omit other traffic, including router-generated ICMP errors. No raw packet capture was analyzed, and screenshot statistics were not extrapolated to total network traffic.

## Splunk analysis and detection sequence

1. Review Nmap upload settings and confirm indexed events ([S01](../evidence/06-splunk/01-nmap-upload-configuration.png), [S02](../evidence/06-splunk/02-nmap-ingestion-search-validation.png)).
2. Extract asset and port fields; distinguish duplicate assets and filtered states from unique hosts/open services ([S03](../evidence/06-splunk/03-asset-field-extraction.png), [S04](../evidence/06-splunk/04-service-inventory-all-states.png), [S05](../evidence/06-splunk/05-pre-segmentation-open-port-inventory.png)).
3. Classify selected open ports as review categories ([S06](../evidence/06-splunk/06-security-relevant-port-classification.png)), then inspect baseline and post-state dashboard panels and explicit comparison labels ([S14](../evidence/06-splunk/14-pre-post-comparison-and-missing-hosts.png)).
4. Correlate missing-device rows with Nmap Guest discovery and Wireshark reachability. Treat Splunk as analysis of the Nmap dataset, not another scan.
5. Inspect the Event 4625 search, fixed five-minute aggregation, and threshold result ([S15](../evidence/06-splunk/15-windows-failed-login-detection-logic.png)); separately confirm the recorded scheduled-alert trigger ([S16](../evidence/06-splunk/16-windows-failed-login-alert-trigger.png)).
6. Review the PDF export visually ([S17](../evidence/06-splunk/17-home-network-security-dashboard.pdf)), preserving pagination and panel-state limitations.

[Splunk analysis](../documentation/splunk-analysis.md) records the transcribed detection query, observed metrics and reproducibility limits. No Splunk searches were executed or modified during this update. Time selectors differ between screenshots; full panel source filters and saved alert configuration remain unavailable.


## Python and XML verification sequence

Review the supplied script before execution; parse all three XML files independently; inspect internal scan arguments/times and explicit host/port states; compare parser outputs; regenerate both Main CSVs and report into an isolated folder; compare CSV records and report line content; correlate Garage Controller/Pool Controller identities by MAC on Guest. A separate Guest CSV is generated as a derivative. These checks passed for the supplied files. No new network scans were run.

[Python/XML verification](../documentation/python-xml-validation.md) records the scope, exact results and limitations, including nondeterministic report ordering and a hard-coded lab-specific assessment paragraph. [Workflow context](../documentation/project-workflow.md) supplies the original nine-phase narrative without treating incomplete notes as verified measurements or instructions to act.

## Wireless assessment sequence

Review [F01–F03](../evidence/03-wifite/README.md) in workflow order: home-target discovery, handshake capture and tool validation, failed initial dictionary, successful custom-list offline verification, and WPA3 enablement prompt. Attribute Kali USB boot, subsequent network entry and completed hardening to the user's account where screenshots do not independently demonstrate them. Do not equate candidate recovery with an established network session or a confirmation dialog with verified mitigation. [Wireless analysis](../documentation/wireless-assessment.md) records each boundary. No new wireless commands were run during this update.

## Deployment and operational baseline

Before interpreting scan results, the project established working household connectivity: router installation, wireless mesh placement, SSID/PSK configuration, device onboarding and Google Home connectivity/performance checks. Troubleshooting moved from endpoint checks to multi-device testing, router/ISP-device power cycling, direct Ethernet testing and Windows DHCP renewal. Recurring app checks supplied a user-recorded operational baseline, now corroborated by [Google Home screenshots](../evidence/01-deployment/README.md) showing node health and speed history with visible improvement. No latency series or continuous uptime measurement is supplied.

The configuration review then covered DNS, DHCP reservations, LAN settings, double NAT remediation, WPA3 enablement, UPnP review and exposure reduction. Service discovery informed selective Guest migration, followed by identity correlation, scoped reachability tests and reported cloud-app usability checks. [The expanded phases 1–6](../documentation/deployment-and-hardening.md) documents every stage and its evidence boundary. These phases are organizational; their numbering does not prove exact chronological order for every recorded action.
