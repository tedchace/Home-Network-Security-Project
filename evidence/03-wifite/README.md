<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Wireless assessment evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

Three original screenshots published as redacted derivatives. Order follows discovery/capture → offline candidate validation → requested hardening. The capture filename contains 2026-09-08T17-40-54; this is filename context, not an independently verified clock or timestamp for all three images.

| Evidence | Observation and limits |
|---|---|
| [F01 — 01-wlan-discovery-handshake.png](01-wlan-discovery-handshake.png) | Wifite2 2.7.0 enables monitor mode on wlan0 and lists wireless networks. The selected home target yields a captured handshake; tshark and aircrack report a valid handshake in the saved capture. The initial wordlist-probable.txt attempt fails because the password is absent. Missing tools cause the PMKID attack to be skipped; no PMKID success is claimed. |
| [F02 — 02-offline-dictionary-validation.png](02-offline-dictionary-validation.png) | Aircrack-ng 1.7 reads the saved capture, reports one handshake and KEY FOUND using test-passwords.txt. The displayed custom list has five entries and includes the recovered password. This demonstrates offline verification of a matching candidate, not exhaustive brute force or recovery from an unknown large password space. |
| [F03 — 03-wpa3-enablement-confirmation.png](03-wpa3-enablement-confirmation.png) | Router settings show the Turn on WPA3? dialog with Turn on and Cancel buttons. This records initiation of the change, not confirmation that it was applied, the restart completed, or a client negotiated WPA3. UPnP appears enabled in the background; no port mapping or WAN exposure is established by this view. |

## Provenance and scope

The user identifies this as an authorized assessment of their own home network, performed from a bootable Kali Linux USB. The screenshots show a Kali session; the boot medium is user-reported. Other wireless entries are incidentally visible in discovery, but the evidence shows one selected home target, not testing of all discovered networks.

| Original filename | Repository filename |
|---|---|
| Wifite - SSID Detection.png | 01-wlan-discovery-handshake.png |
| Wifite - Offline Dictionary Attack.png | 02-offline-dictionary-validation.png |
| Wifite - WPA3 Remediation.png | 03-wpa3-enablement-confirmation.png |

Source: Router Configuration & Test Project/Wifite Simulation. Originals remain in place; [sha256.csv](sha256.csv) records public derivative hashes. original-placeholder.txt (private; not published) preserves the previous filename plan. Passwords, derived keys, and candidate strings are not transcribed into the documentation. The original images remain in the private backup outside the repository.

## Evidence boundary

F01 shows that the initial dictionary failed; F02 shows success with a small custom list containing the correct candidate. This is a controlled dictionary validation, not a demonstrated cryptographic break. The supplied images do not show a successful subsequent Wi-Fi association, DHCP lease, or resource-access test; network entry is reported by the user. No raw handshake file was supplied or analyzed in this update.

The user reports completing WPA3 hardening, and the original workflow describes WPA2/WPA3 operation and a stronger PSK. F03 alone is a pending confirmation view. It does not establish WPA3-only mode, per-client negotiated security, or resistance to a repeat assessment. No claim that the captured old handshake became unusable or that all legacy clients now use WPA3 follows from this screenshot.

See [wireless analysis](../../documentation/wireless-assessment.md), [findings](../../documentation/findings.md), and [validation](../../documentation/remediation-validation.md).
