<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Configuration hardening evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

Google Home screenshots supplied by the user, preserved privately; public copies are redacted. See the [deployment and hardening account](../../documentation/deployment-and-hardening.md) and retained original filename plan (private; not published).

| ID | Screenshot | Observation and boundary |
|---|---|---|
| H01 | [Custom DNS](01-cloudflare-security-dns.png) | Custom selected, 1.1.1.2 displayed. Secondary 1.0.0.2 is workflow-reported; blocking efficacy is not tested here |
| H02 | [Device grouping](02-device-grouping.png) | Printer 1, Security System 4, Smart TV 1, Trusted Devices 11; SafeSearch off; no schedules. Management groups are not isolated segments |
| H03 | [Guest configuration](03-guest-iot-network-configuration.png) | Guest enabled, named SSID, masked password; password display on voice-assistant displays checked. Shared-device list not visible |
| H04 | [Advanced settings](04-wpa3-upnp-off-advanced-settings.png) | WPA3 enabled, UPnP disabled, IPv6 disabled, Custom DNS selected; WAN and LAN settings menus visible |

The Guest subnet is established by [Nmap evidence](../04-nmap/README.md), not these app views. The [client/router DNS exchange](../05-wireshark/01-dns-resolution-analysis.png) does not identify the upstream resolver. The [initial WPA3 image](../03-wifite/03-wpa3-enablement-confirmation.png) shows a confirmation prompt; [H04](04-wpa3-upnp-off-advanced-settings.png) shows WPA3 enabled and UPnP disabled. Client negotiation and mitigation effectiveness remain unverified. [Isolation validation](../../documentation/remediation-validation.md) remains scoped to the supplied tests.

[Source hashes](source-map.csv) record the original files and copies. Public derivatives have been sanitized; original evidence is retained privately.
