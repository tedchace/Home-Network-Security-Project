<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Splunk evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

Sixteen screenshots and one original dashboard PDF, published as redacted derivatives. Numbering follows the analysis workflow, not an asserted capture chronology: ingestion → extraction → baseline panels → post-state panels → comparison → detection → export. Original overview version numbers do not reliably identify dataset state; use panel contents and state labels.

## Evidence register

| ID / file | Observed evidence and limits |
|---|---|
| [S01 — 01-nmap-upload-configuration.png](01-nmap-upload-configuration.png) | Upload review selects nmap_main_pre_segmentation.xml, sourcetype nmap:xml, host lab-workstation, index home_network. This is the review step before Submit, not ingestion success by itself. |
| [S02 — 02-nmap-ingestion-search-validation.png](02-nmap-ingestion-search-validation.png) | All time search index=home_network returns 13 events, including Nmap XML with source nmap_main_pre_segmentation.xml and sourcetype nmap:xml. Visible XML records a September 2, 2026 scan. Event count is not unique host count. |
| [S03 — 03-asset-field-extraction.png](03-asset-field-extraction.png) | SPL extracts IPv4, MAC, vendor and hostname; Statistics (13) includes duplicate 192.0.2.1 rows. Do not report 13 distinct assets. Source filter and deduplication are absent from the visible search. |
| [S04 — 04-service-inventory-all-states.png](04-service-inventory-all-states.png) | rex and mvexpand extract port records; 43 result rows include open and filtered states. This is not 43 open services. Full XML/event-boundary parsing remains to be checked. |
| [S05 — 05-pre-segmentation-open-port-inventory.png](05-pre-segmentation-open-port-inventory.png) | Statistics (39) displays open TCP service rows. Full SPL is cropped; use as observed inventory output, not a complete reproducible query. |
| [S06 — 06-security-relevant-port-classification.png](06-security-relevant-port-classification.png) | Visible SPL filters state=open and classifies ports 23, 21, 445, 3389, 5800/5900, excluding Other. Five rows shown: pool TCP/23; laptop .74 TCP/445,5800,5900; workstation .83 TCP/445. Labels are review categories, not confirmed vulnerabilities. |
| [S07 — 07-baseline-dashboard-overview.png](07-baseline-dashboard-overview.png) | Earlier dashboard displays 12 hosts, 39 open services, 5 flagged services; Global Time Range Last 24 hours. Panel queries are not shown. |
| [S08 — 08-baseline-security-relevant-services.png](08-baseline-security-relevant-services.png) | Five classified rows match the baseline service list. Cropped panel lacks its source filter; baseline attribution follows matching rows, not a visible source selector. |
| [S09 — 09-baseline-open-services-by-host.png](09-baseline-open-services-by-host.png) | Chart includes .83 with 8, .1 with 7, .31/.76/.77 with 5 each, .74 with 4 and five hosts with 1 each. These displayed bars total 39; this is hosts with open services, not all discovered hosts. |
| [S10 — 10-baseline-service-categories.png](10-baseline-service-categories.png) | Category chart shows SMB/File Sharing 40%, VNC/Remote Access 40%, Legacy Remote Access 20%. These describe the five classified service rows, not proportions of vulnerable hosts. |
| [S11 — 11-baseline-service-inventory-panel.png](11-baseline-service-inventory-panel.png) | Paginated inventory excerpt includes pool TCP/23 and laptop TCP/445 and 5800. Panel title says complete inventory, but screenshot shows only a page excerpt. |
| [S12 — 12-post-segmentation-dashboard-summary.png](12-post-segmentation-dashboard-summary.png) | Dashboard shows 10 discovered hosts, 34 open services, 1 security-relevant service; Global Time Range All time. Post-state attribution is consistent with comparison panels and PDF, but panel SPL is not shown. |
| [S13 — 13-post-segmentation-classified-service.png](13-post-segmentation-classified-service.png) | One classified row remains: 192.0.2.83 TCP/445 microsoft-ds, SMB/File Sharing. This is one service under the chosen classification, not the only service or only remaining risk. |
| [S14 — 14-pre-post-comparison-and-missing-hosts.png](14-pre-post-comparison-and-missing-hosts.png) | Explicit state labels show open TCP services pre 39/post 34 and classified services pre 5/post 1. Missing-host table lists pool .27, laptop .74 and MyQ .22. Post appears left and pre right; read labels rather than bar position. |
| [S15 — 15-windows-failed-login-detection-logic.png](15-windows-failed-login-detection-logic.png) | Search index=windows_endpoint EventCode=4625 bins _time span=5m; stats by time, ComputerName and Account_Name; failed_logons>=3. Range 2026-09-03 13:45–14:00. Two rows at 13:55, each count 3, for TEDCHASE$ and lab-user on lab-workstation; failure reason Unknown user name or bad password, source 127.0.0.1. UI reports 3 events and 2 statistics rows; do not sum as six distinct failures. |
| [S16 — 16-windows-failed-login-alert-trigger.png](16-windows-failed-login-alert-trigger.png) | Windows - Multiple Failed Logins is enabled, scheduled (Cron Schedule), trigger Number of Results > 0, action Add to Triggered Alerts. History shows 2026-09-03 14:00:01 EDT. Exact cron/lookback and View Results contents are not shown. |
| [S17 — 17-home-network-security-dashboard.pdf](17-home-network-security-dashboard.pdf) | One-page image-based export inspected visually: 10/34/1 summary, one SMB row, post-state service chart, inventory page 1 of 4 and pre/post comparison. Export does not expose all paginated rows or dashboard SPL; it is another presentation of the dataset, not independent measurement. |

## Provenance

Source: the user's local `Router Configuration & Test Project/Splunk Activities` folder. Original files remain in place. SHA-256 hashes in [sha256.csv](sha256.csv) verify public derivatives. The earlier filename plan is retained in original-placeholder.txt (private; not published).

| Original | Repository filename |
|---|---|
| Splunk - Configured Splunk Index.png | 01-nmap-upload-configuration.png |
| Splunk - Nmap Data Ingestion & Splunk Search Validation.png | 02-nmap-ingestion-search-validation.png |
| Splunk - Splunk Asset Discovery.png | 03-asset-field-extraction.png |
| Splunk - Splunk Network Service Inventory.png | 04-service-inventory-all-states.png |
| Splunk - Open Port Inventory Pre Segmentation.png | 05-pre-segmentation-open-port-inventory.png |
| Splunk - Potentially Exposed Ports.png | 06-security-relevant-port-classification.png |
| Splunk - Network Security Dashboard 1.0.png | 07-baseline-dashboard-overview.png |
| Splunk - Dashboard Overview 1.2.png | 08-baseline-security-relevant-services.png |
| Splunk - Dashboard Overview 1.3.png | 09-baseline-open-services-by-host.png |
| Splunk - Dashboard Overview 1.4.png | 10-baseline-service-categories.png |
| Splunk - Dashboard Overview 1.5.png | 11-baseline-service-inventory-panel.png |
| Splunk - Dashboard Overview 1.1.png | 12-post-segmentation-dashboard-summary.png |
| Splunk - Dashboard Overview 1.7.png | 13-post-segmentation-classified-service.png |
| Splunk - Dashboard Overview 1.6.png | 14-pre-post-comparison-and-missing-hosts.png |
| Splunk - Windows Endpoint Detection - Failed Login Detection Logic.png | 15-windows-failed-login-detection-logic.png |
| Splunk - Windows Endpoint Detection - Alert Trigger Validation.png | 16-windows-failed-login-alert-trigger.png |
| Home Network Security Dashboard.pdf | 17-home-network-security-dashboard.pdf |

## Reading the results

- S02's 13 events and S03's 13 rows are not 13 distinct hosts; S03 visibly duplicates the gateway. S07 separately displays 12 discovered hosts.
- S04 includes filtered ports. S05's 39 open rows and S14's explicit pre/post comparison are the relevant open-service evidence.
- S07 uses Last 24 hours; S12 and S14 use All time. The supplied XML now reproduces the metrics independently; source filters, deduplication, XML event boundaries and panel SPL still require query/config exports to verify Splunk's implementation. All time alone does not isolate pre/post datasets.
- S08–S11 preserve baseline-like panel contents, while S12–S13 and the PDF show post-state contents. Do not combine every overview screenshot into one internally consistent snapshot. The PDF inventory is paginated and only the visible page is exported.
- S14 shows a five-row decline (39 → 34, approximately 12.8%) and four-row decline in the chosen classification (5 → 1, 80%). These are arithmetic changes in displayed counts, not measured vulnerability or risk reductions. The missing laptop's three classified rows are not established segmentation successes.
- S06 classifies open ports: 23 Legacy Remote Access; 21 Cleartext File Transfer; 445 SMB / File Sharing; 3389 Remote Desktop; 5800 or 5900 VNC / Remote Access. Other is excluded. Port-based categories are a review aid and are not exhaustive risk assessment.
- S15's fixed five-minute bins are not a sliding window. Account_Name may contain multiple values; inspect raw Event 4625 fields and target-account extraction before interpreting the two rows as independent attempts. Source 127.0.0.1 is loopback, not an identified remote attacker.
- S16 proves a recorded alert trigger, but not notification delivery, complete incident investigation, or malicious activity. Test-generation details remain project context unless separately evidenced.

See [Splunk analysis](../../documentation/splunk-analysis.md), [findings](../../documentation/findings.md), and [validation](../../documentation/remediation-validation.md). [Python/XML verification](../07-python/README.md) is complete for the supplied files.

## Source-data reconciliation update

[Python/XML verification](../../documentation/python-xml-validation.md) is now complete for the three supplied XML files and the Main CSV/report outputs. It reproduces the Main totals and correlates both IoT devices by MAC on Guest, where TCP/80 and TCP/23 remain open. Unpublished Splunk query/event configuration remains unverified.
