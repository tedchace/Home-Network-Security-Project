<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Wireshark evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

Eight redacted screenshot derivatives. Solid masks remove identifying fields and packet-byte panes; technical interpretation is based on the preserved private originals. Numbering follows the documentation sequence (baseline → analysis → pre-segmentation tests → post-segmentation test). Absolute capture dates are not shown, and relative timestamps from separate captures cannot establish chronology across files.

## Evidence register

### W01 — dns resolution analysis

[Open screenshot](01-dns-resolution-analysis.png)

- **Capture context:** Wi-Fi 2; `dns`; relative times 3.139–3.213 s; 6 displayed / 64 packets.
- **Observed:** 192.0.2.83 queries 192.0.2.1. PTR lookup for the gateway receives No such name; example.com A and AAAA queries receive address answers.
- **Interpretation and limits:** Confirms the observed client/router DNS exchange, not the router's upstream resolver, DNS filtering effectiveness, or DNSSEC validation.

### W02 — protocol hierarchy baseline

[Open screenshot](02-protocol-hierarchy-baseline.png)

- **Capture context:** Wi-Fi 2; No display filter; 846 frames; capture date/duration not shown.
- **Observed:** IPv4 572 (67.6%), IPv6 25 (3.0%), ARP 249 (29.4%); TCP 421 (49.8%), TLS 154 (18.2%). DNS, DHCP, mDNS, SSDP, SNMP, QUIC and ICMP are also listed.
- **Interpretation and limits:** Describes this capture only. Nested protocol rows overlap and must not be summed as independent categories. Does not establish a representative whole-network baseline or malicious activity.

### W03 — pool controller broadcast endpoints

[Open screenshot](03-pool-controller-broadcast-endpoints.png)

- **Capture context:** Ethernet Endpoints view; Limit to display filter checked; filter expression, interface, time and duration not visible.
- **Observed:** 02:00:00:00:00:01 transmits 923 packets / 39 kB; broadcast endpoint receives 923 displayed packets. Broadcast Total Packets is 1,011.
- **Interpretation and limits:** Filtered endpoint statistics support broadcast attribution. This screenshot alone does not identify packet protocol or prove ARP flooding; ARP context comes from W05 and W04.

### W04 — pool controller broadcast conversation

[Open screenshot](04-pool-controller-broadcast-conversation.png)

- **Capture context:** Wi-Fi 2; Ethernet Conversations; Limit to display filter checked; expression obscured. Relative start 0; conversation duration 1013.385215 s.
- **Observed:** One displayed conversation from the controller MAC to 02:00:00:ff:ff:ff: 1,988 packets / 83 kB A→B, zero B→A; selected packet bytes show ARP asking about 192.0.2.1 from 192.0.2.27.
- **Interpretation and limits:** Filtered Ethernet broadcast accounting is not a count of all controller traffic or proof of no unicast replies. Counts differ from W03 and must not be merged.

### W05 — pre segmentation icmp request reply

[Open screenshot](05-pre-segmentation-icmp-request-reply.png)

- **Capture context:** Cropped packet list; interface and filter not shown. Four complete visible pairs at relative times 11.242–14.295 s.
- **Observed:** 192.0.2.83 → 192.0.2.27 echo requests and reverse replies: frames 158/163, 166/167, 171/172, 180/181. Repeated ARP asks Who has 192.0.2.1? Tell 192.0.2.27. Frame 188 maps 192.0.2.27 to 02:00:00:00:00:01.
- **Interpretation and limits:** Confirms bidirectional ICMP for these exchanges, not every protocol. Repeated ARP merits context; its cause, performance impact, and whether gateway replies were visible cannot be established here.

### W06 — pre segmentation tcp23 incomplete handshake

[Open screenshot](06-pre-segmentation-tcp23-incomplete-handshake.png)

- **Capture context:** Wi-Fi 2; `ip.addr == 192.0.2.27 && tcp.port == 23`; 5 displayed / 110 packets; relative times 4.621–9.632 s.
- **Observed:** 192.0.2.83:33506 sends SYN to 192.0.2.27:23; controller sends SYN/ACK and repeated SYN/ACKs labeled retransmissions. Details show ACK/Data/FIN/RST absent and conversation incomplete.
- **Interpretation and limits:** Supports TCP/23 responsiveness. This view does not show a completed handshake, application data, successful login, or the cause of retransmissions.

### W07 — pre segmentation tcp23 telnet negotiation

[Open screenshot](07-pre-segmentation-tcp23-telnet-negotiation.png)

- **Capture context:** Wi-Fi 2; `ip.addr == 192.0.2.27`; 2,172 displayed / 2,978 packets; excerpt around 57.299–76.500 s.
- **Observed:** Frames 2769/2771/2772 show SYN, SYN/ACK, ACK for 192.0.2.83:52766 ↔ 192.0.2.27:23, followed by data and TELNET negotiation. Other exchanges include zero-window, FIN/ACK and RST/ACK annotations.
- **Interpretation and limits:** Corroborates Nmap's Telnet-compatible exposure at packet level. Filename/project context attributes traffic to Nmap; screenshot alone does not identify the generating process. No successful authentication or shell command execution is demonstrated.

### W08 — post segmentation main to guest icmp

[Open screenshot](08-post-segmentation-main-to-guest-icmp.png)

- **Capture context:** Wi-Fi 2; `ip.addr == 198.51.100.21 || ip.addr == 198.51.100.22`; 8 displayed / 475 packets; requests span relative times 17.697–58.588 s.
- **Observed:** 192.0.2.92 sends four ICMP echo requests to 198.51.100.21 (Garage Door Controller per Nmap inventory) and four to 198.51.100.22 (Pool Controller). Each is annotated no response found; no echo replies appear.
- **Interpretation and limits:** Consistent with restricted Main-to-Guest ICMP reachability during this observation. Does not identify a blocking rule or exclude device availability, routing or capture visibility as explanations; it is not proof of complete isolation.

## Provenance

Source: the user's local `Router Configuration & Test Project/Wireshark Captures` folder. Original source files remain in place. Copies are verified byte-for-byte by SHA-256, recorded in [sha256.csv](sha256.csv). The prior suggested filename list remains in [original-placeholder.txt](original-placeholder.txt); the register above supersedes it.

| Original filename | Repository copy |
|---|---|
| Wireshark - DNS Resolution Analysis.png | [01-dns-resolution-analysis.png](01-dns-resolution-analysis.png) |
| Wireshark - Protocol Hierarchy.png | [02-protocol-hierarchy-baseline.png](02-protocol-hierarchy-baseline.png) |
| Wireshark - Pool Controller ARP Traffic.png | [03-pool-controller-broadcast-endpoints.png](03-pool-controller-broadcast-endpoints.png) |
| Wireshark - Endpoints and Conversations.png | [04-pool-controller-broadcast-conversation.png](04-pool-controller-broadcast-conversation.png) |
| Wireshark - ICMP Request and Reply.png | [05-pre-segmentation-icmp-request-reply.png](05-pre-segmentation-icmp-request-reply.png) |
| Wireshark - TCP Conversation.png | [06-pre-segmentation-tcp23-incomplete-handshake.png](06-pre-segmentation-tcp23-incomplete-handshake.png) |
| Wireshark - Nmap TCP23 Traffic.png | [07-pre-segmentation-tcp23-telnet-negotiation.png](07-pre-segmentation-tcp23-telnet-negotiation.png) |
| Wireshark = Post Segmentation Isolation Validation.png | [08-post-segmentation-main-to-guest-icmp.png](08-post-segmentation-main-to-guest-icmp.png) |

## Cross-tool interpretation

W05's ARP mapping and W07's Ethernet details correlate the pool controller's 192.0.2.27 address with the MAC shown in the [Nmap service scan](../04-nmap/04-pool-controller-tcp23-telnet-exposure.png). W07 adds packet-level Telnet negotiation to that service observation, without proving exploitation.

W08 uses Main source 192.0.2.92. The [Nmap filtered TCP/23 test](../04-nmap/10-main-to-guest-tcp23-filtered.png) shows 192.0.2.88; the pre-segmentation ICMP/TCP views use 192.0.2.83. These are separate observations, not one simultaneous experiment. Guest device names are correlated using [Guest discovery](../04-nmap/09-post-segmentation-guest-iot-discovery.png), not exposed by W08 itself.

The post-segmentation filter selects traffic containing the two Guest IPs; an ICMP error sourced by an intermediate router may not match those outer addresses. Do not infer that no diagnostic errors occurred outside the displayed view. No raw captures were analyzed in this update. A displayed zero-drop counter does not establish visibility of all network traffic.

See [findings](../../Documentation/findings.md), [methodology](../../Documentation/methodology.md), and [validation](../../documentation/remediation-validation.md). See the integrated [Splunk evidence](../06-splunk/README.md).

## Source-data reconciliation update

[Python/XML verification](../../documentation/python-xml-validation.md) is now complete for the three supplied XML files and the Main CSV/report outputs. It reproduces the Main totals and correlates both IoT devices by MAC on Guest, where TCP/80 and TCP/23 remain open. Unpublished Splunk query/event configuration remains unverified.
