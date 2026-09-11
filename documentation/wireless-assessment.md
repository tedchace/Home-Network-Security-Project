<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Authorized Wireless Assessment

## Scope and environment

The user reports testing their own home network from Kali Linux on a bootable USB. [F01](../evidence/03-wifite/01-wlan-discovery-handshake.png) shows the Kali session, Wifite2 2.7.0 and monitor-mode interface. Only the selected home target is in scope; incidental nearby network entries are not findings about those networks. This repository update documents existing evidence and performs no wireless testing.

## Observed sequence

1. **Discovery and capture:** Wifite lists wireless entries, selects one home target, captures a handshake and saves a .cap file. Its output reports validation by tshark and aircrack. PMKID testing is skipped because required tools are missing. The screenshot does not establish how any client reconnection was induced.
2. **Initial dictionary attempt:** Wifite's wordlist-probable.txt run fails to recover a password. Failure of that list is a limited result, not proof of password strength.
3. **Controlled offline validation:** [F02](../evidence/03-wifite/02-offline-dictionary-validation.png) shows Aircrack-ng 1.7 returning KEY FOUND with a five-entry custom list containing the recovered candidate. The capture is reported to contain one handshake. This establishes successful candidate validation against the captured exchange; it does not establish broad brute-force feasibility or a break of WPA cryptography.
4. **Reported entry:** The user reports using the recovered password to gain network access. Association, DHCP assignment and resource access are not shown in these images, so this remains an attributed outcome.
5. **Hardening:** [F03](../evidence/03-wifite/03-wpa3-enablement-confirmation.png) shows the initial WPA3 confirmation prompt. The [later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png) shows WPA3 enabled and UPnP disabled, corroborating the applied settings. The workflow reports a longer/stronger PSK and WPA2/WPA3 mixed-mode operation; per-client security mode is not shown.

## Findings and limits

The password was recoverable when its matching value was supplied in the controlled dictionary. Avoid presenting the small-list timing as a benchmark for unknown passwords. Do not transcribe the password or derived keys into report text; original screenshots are retained privately and public copies redact credentials and identifying fields.

The terminal labels WPA/WPA-P do not by themselves establish the exact WPA generation and cipher suite. The workflow supplies the WPA2 context. The [later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png) corroborates WPA3 enablement and UPnP disablement, but does not establish WPA3-only operation, successful per-client WPA3 negotiation or resistance to a repeated assessment.

UPnP appears enabled in F03 and disabled in the [later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png). These record settings at two points in the project; neither establishes active mappings or Internet exposure.

## Validation status

| Claim | Status |
|---|---|
| Selected home network discovered | Shown in F01 |
| Handshake captured and tool validation reported | Shown in F01; raw capture not supplied |
| Initial dictionary unsuccessful | Shown in F01 |
| Custom dictionary recovers matching key | Shown in F02 |
| Subsequent network entry | User-reported; connection evidence not supplied |
| WPA3 enablement initiated | Confirmation dialog shown in F03 |
| WPA3 enabled / UPnP disabled | Shown in the [later advanced settings screenshot](../evidence/02-hardening/04-wpa3-upnp-off-advanced-settings.png) |
| Stronger PSK / WPA2-WPA3 mixed mode | User/workflow-reported |
| Per-client WPA3 negotiation or post-hardening resistance | Not demonstrated in this image set |

The post-confirmation settings view is now supplied. Remaining evidence gaps concern per-client security negotiation and post-change effectiveness; no additional wireless testing was performed during this documentation update.
