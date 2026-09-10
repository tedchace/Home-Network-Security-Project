<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Nmap evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

These 11 screenshots are public redacted derivatives; originals are preserved privately. Numbering follows the assessment sequence; it is not an assertion of exact capture chronology where timestamps are absent. Printer enumeration precedes Garage Controller enumeration based on visible scan times. The final image is derived comparison output, not raw Nmap output.

| Evidence | Visible time / phase | Observation |
|---|---|---|
| [01-initial-main-lan-discovery.png](01-initial-main-lan-discovery.png) | Baseline | `nmap -sn 192.0.2.0/24`; topology includes Garage Controller `.22` and Pool Controller `.27` on Main. |
| [02-windows-endpoint-service-enumeration.png](02-windows-endpoint-service-enumeration.png) | 2026-08-28 13:50 EDT | Selected output is `nmap -sV 192.0.2.40`: TCP 135, 139, 445, 902, 912 open. The editable target bar shows `.27`; use the selected output, not that bar. |
| [03-vmware-netstat-tasklist-corroboration.png](03-vmware-netstat-tasklist-corroboration.png) | Endpoint follow-up; time not shown | Local `netstat -ano` shows 902/912 listening on `0.0.0.0`, PID 6388; `tasklist` maps PID to `vmware-authd.exe`. |
| [04-pool-controller-tcp23-telnet-exposure.png](04-pool-controller-tcp23-telnet-exposure.png) | 2026-08-28 14:02 EDT | `nmap -sV 192.0.2.27`: TCP/23 open, labeled telnet; TCP/8080 filtered. Unrecognized fingerprint includes Nucleus Shell text. |
| [05-printer-service-enumeration.png](05-printer-service-enumeration.png) | 2026-08-28 14:35 EDT | `nmap -sV 192.0.2.24`: TCP 80, 443, 515, 631, 9100, 9876, 9877 open. Product/service labels require corroboration. |
| [06-garage-door-http-exposure.png](06-garage-door-http-exposure.png) | 2026-08-28 17:02 EDT | `nmap -sV 192.0.2.22`: TCP/80 open; HTTP 200 JSON response includes device and network metadata. |
| [07-guest-network-initial-discovery.png](07-guest-network-initial-discovery.png) | Guest baseline; time not shown | `nmap -sn 198.51.100.0/24`; topology shows gateway `.1` and workstation `.20`, not the migrated IoT devices. |
| [08-post-segmentation-main-lan-discovery.png](08-post-segmentation-main-lan-discovery.png) | Post-segmentation; time not shown | Topology with `nmap -sV 192.0.2.0/24` in command field; original Garage Controller/Pool Controller entries not displayed. Workstation now shown at `.83`. |
| [09-post-segmentation-guest-iot-discovery.png](09-post-segmentation-guest-iot-discovery.png) | Post-segmentation; time not shown | Topology with `nmap -sV 198.51.100.0/24`; Garage Controller `.21`, Pool Controller `.22`, gateway `.1`, workstation `.88`. |
| [10-main-to-guest-tcp23-filtered.png](10-main-to-guest-tcp23-filtered.png) | 2026-09-04 14:42 EDT | Wi-Fi adapter `192.0.2.88/24`, gateway `192.0.2.1`; `nmap -Pn -p 23 198.51.100.22` returns TCP/23 filtered. |
| [11-pre-post-network-comparison.png](11-pre-post-network-comparison.png) | Derived comparison; time not shown | Reports `192.0.2.27`, `192.0.2.22`, `192.0.2.74` no longer observed; `192.0.2.82` newly observed; TCP/5432 no longer observed on correlated workstation `192.0.2.83`. |

## Source provenance

Original files were copied from the local project folder `Router Configuration & Test Project/Nmap Scans`. Ten were also available through the referenced conversation attachments; the comparison screenshot was recovered from the local folder. Original source files remain in place.

| Original filename | Repository filename |
|---|---|
| Nmap - Initial Network Discovery Scan.png | 01-initial-main-lan-discovery.png |
| Nmap - Asset Enumeration Windows Endpoint.png | 02-windows-endpoint-service-enumeration.png |
| Nmap - Endpoint Corroboration VMware.png | 03-vmware-netstat-tasklist-corroboration.png |
| Nmap - IoT Service Exposure Pool Controller.png | 04-pool-controller-tcp23-telnet-exposure.png |
| Nmap - Printer Service Enumeration.png | 05-printer-service-enumeration.png |
| Nmap - IoT Service Exposure Garage Door.png | 06-garage-door-http-exposure.png |
| Nmap - Guest Network Topology.png | 07-guest-network-initial-discovery.png |
| Nmap - Post Segmentation IoT Discovery Main.png | 08-post-segmentation-main-lan-discovery.png |
| Nmap - Post Segmentation IoT Discovery Guest.png | 09-post-segmentation-guest-iot-discovery.png |
| Nmap - Post Segmentation Access Validation.png | 10-main-to-guest-tcp23-filtered.png |
| Nmap - Pre & Post Network Comparison.png | 11-pre-post-network-comparison.png |

SHA-256 values are recorded in [sha256.csv](sha256.csv). The prior placeholder list is retained in [original-placeholder.txt](original-placeholder.txt).

## Interpretation

Read the selected scan output rather than relying on Zenmap's editable command bar or accumulated host sidebar. Topology screenshots provide visible inventory context, not a complete physical map or firewall policy. Discovery absence alone does not establish remediation. See [findings](../../Documentation/findings.md) and [validation](../../documentation/remediation-validation.md).

## Source-data reconciliation update

[Python/XML verification](../../documentation/python-xml-validation.md) is now complete for the three supplied XML files and the Main CSV/report outputs. It reproduces the Main totals and correlates both IoT devices by MAC on Guest, where TCP/80 and TCP/23 remain open. Unpublished Splunk query/event configuration remains unverified.
