<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Authorized Wireless Assessment

## Scope and environment

The user reports testing their own home network from Kali Linux on a bootable USB. [F01](../evidence/03-wifite/01-wlan-discovery-handshake.png) shows the Kali session, Wifite2 2.7.0 and monitor-mode interface. Only the selected home target is in scope; incidental nearby network entries are not findings about those networks. This repository update documents existing evidence and performs no wireless testing.

## Observed sequence

1. **Discovery and capture:** Wifite lists wireless entries, selects one home target, captures a handshake and saves a .cap file. Its output reports validation by tshark and aircrack. PMKID testing is skipped because required tools are missing. The screenshot does not establish how any client reconnection was induced.
2. **Initial dictionary attempt:** Wifite's wordlist-probable.txt run fails to recover a password. Failure of that list is a limited result, not proof of password strength.
3. **Controlled offline validation:** [F02](../evidence/03-wifite/02-offline-dictionary-validation.png) shows Aircrack-ng 1.7 returning KEY FOUND with a five-entry custom list containing the recovered candidate. The capture is reported to contain one handshake. This establishes successful candidate validation against the captured exchange; it does not establish broad brute-force feasibility or a break of WPA cryptography.
4. **Reported entry:** The user reports using the recovered password to gain network access. Association, DHCP assignment and resource access are not shown in these images, so this remains an attributed outcome.
5. **Hardening:** [F03](../evidence/03-wifite/03-wpa3-enablement-confirmation.png) shows the router's WPA3 confirmation prompt. The user reports completing the change; the original workflow also reports a longer/stronger PSK and WPA2/WPA3 operation. The screenshot does not independently verify completion or client security mode.

## Findings and limits

The password was recoverable when its matching value was supplied in the controlled dictionary. Avoid presenting the small-list timing as a benchmark for unknown passwords. Do not transcribe the password or derived keys into report text; original screenshots are retained privately and public copies redact credentials and identifying fields.

The terminal labels WPA/WPA-P do not by themselves establish the exact WPA generation and cipher suite. The workflow supplies the WPA2 context. The remediation image does not establish WPA3-only operation, successful WPA3 negotiation, or a repeated post-change test. Therefore the evidence supports a demonstrated recovery and a documented hardening action initiated, with completion reported by the user and effectiveness not independently tested here.

UPnP appears enabled in F03. This resolves the earlier notes' question about its displayed setting at that moment, but not its current state, active mappings, or Internet exposure. It is not a newly proven vulnerability.

## Validation status

| Claim | Status |
|---|---|
| Selected home network discovered | Shown in F01 |
| Handshake captured and tool validation reported | Shown in F01; raw capture not supplied |
| Initial dictionary unsuccessful | Shown in F01 |
| Custom dictionary recovers matching key | Shown in F02 |
| Subsequent network entry | User-reported; connection evidence not supplied |
| WPA3 enablement initiated | Confirmation dialog shown in F03 |
| WPA3 change completed / stronger PSK configured | User/workflow-reported |
| Per-client WPA3 negotiation or post-hardening resistance | Not demonstrated in this image set |

To close the evidence gap later, retain a post-confirmation settings view and connection/security-mode evidence, plus any authorized post-change validation results. These are documentation gaps, not instructions to conduct additional attacks now.
