<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Splunk Monitoring and Detection

## Data ingestion and service analysis

[S01](../evidence/06-splunk/01-nmap-upload-configuration.png) records the intended upload settings. [S02](../evidence/06-splunk/02-nmap-ingestion-search-validation.png) shows indexed Nmap XML under `home_network` / `nmap:xml`, demonstrating successful search of uploaded data. This is uploaded scan analysis, not evidence of continuous live scanning.

[S03](../evidence/06-splunk/03-asset-field-extraction.png) extracts asset fields but visibly duplicates the gateway. [S04](../evidence/06-splunk/04-service-inventory-all-states.png) expands port records into 43 rows including filtered states; [S05](../evidence/06-splunk/05-pre-segmentation-open-port-inventory.png) shows 39 open service rows. The visible regular expressions rely on XML attribute order and event structure. Before reuse, validate that host and port records remain associated correctly, inspect header events, null MACs and duplicates, and separate source files. The supplied XML has now been independently reconciled below; validating the actual Splunk extraction pipeline still requires event and query configuration.

## Baseline and post-state interpretation

| Display | Baseline | Post-state | Evidence |
|---|---|---|---|
| Discovered hosts | 12 | 10 | [S07](../evidence/06-splunk/07-baseline-dashboard-overview.png), [S12](../evidence/06-splunk/12-post-segmentation-dashboard-summary.png); distinct time selectors and undisclosed panel queries |
| Open TCP service rows | 39 | 34 | [S14](../evidence/06-splunk/14-pre-post-comparison-and-missing-hosts.png) with explicit state labels |
| Classified service rows | 5 | 1 | [S14](../evidence/06-splunk/14-pre-post-comparison-and-missing-hosts.png); classification defined in [S06](../evidence/06-splunk/06-security-relevant-port-classification.png) |

The displayed open-service decline is 5/39 ≈ 12.8%; the classified decline is 4/5 = 80%. These numbers now agree with independently parsed XML records, but are not percentages of vulnerabilities remediated. The missing laptop 192.0.2.74 accounts for three baseline classified rows (445, 5800, 5900); only the pool controller's classified TCP/23 disappearance is corroborated by the reported migration and Guest discovery. Garage Controller HTTP is outside this classification even though it is an exposure finding.

[S13](../evidence/06-splunk/13-post-segmentation-classified-service.png) shows TCP/445 remaining on 192.0.2.83. This warrants scope/necessity review; it does not demonstrate exploitable SMB. The laptop's VNC-labeled services at .74 are distinct from the VMware 902/912 observation on the other Windows endpoint in the earlier Nmap evidence. Neither service identification establishes exploitability.

[S17](../evidence/06-splunk/17-home-network-security-dashboard.pdf) is a one-page visual export with post-state contents and comparison panels. It does not supply the dashboard definition or all service-table pages. Baseline panels and later panels must retain their separate context. Splunk and Python analyses of the same Nmap XML are independent implementations only if checked; they are not independent network observations.

## Failed-login detection

The following is transcribed from [S15](../evidence/06-splunk/15-windows-failed-login-detection-logic.png); it was not executed or changed during this documentation update.

```spl
index=windows_endpoint EventCode=4625
| bin _time span=5m
| stats count AS failed_logons
        values(Failure_Reason) AS failure_reason
        values(Source_Network_Address) AS source_address
        BY _time ComputerName Account_Name
| where failed_logons >= 3
| sort - _time
```

The query groups by fixed five-minute time bucket, endpoint, and account field. Three failures spanning a bucket boundary may not meet the threshold in either bucket, even if they occur within five elapsed minutes. The threshold is not a guarantee of sliding-window detection.

The displayed 13:45–14:00 search on September 3, 2026 shows two result rows for the 13:55 bucket, each with count 3, one for TEDCHASE$ and one for lab-user. The UI separately reports three events. Both rows show source 127.0.0.1 and Unknown user name or bad password. Do not add the counts to report six unique attempts. Raw events and field cardinality are needed to distinguish subject and target accounts and determine whether the rows share events.

[S16](../evidence/06-splunk/16-windows-failed-login-alert-trigger.png) shows the saved alert enabled and scheduled, triggering when result count exceeds zero and recording an entry in Triggered Alerts at 14:00:01 EDT. This demonstrates an operational trigger in the lab. The exact cron expression, search lookback, throttling settings, and saved search contents are not visible; the query screenshot is associated by context rather than an exported saved-search definition. The trigger's View Results was not inspected. No remote attack, account compromise, or external notification delivery is inferred.


## XML reconciliation completed

[Python/XML verification](python-xml-validation.md) independently reproduces 12/39 → 10/34 Main host/open-service counts and 5 → 1 classified counts. Main pre contains one gateway XML host record and four explicit filtered records alongside 39 open records. Thus the 13-row Splunk asset view contains duplication not present as an extra XML host. The exact Splunk indexing/extraction cause still requires event/config inspection. The actual saved dashboard queries and Event 4625 data were not supplied or rerun.

The displayed counts above agree with this completed source-data check. Agreement verifies the supplied scan-derived metrics, not causal attribution of every change to segmentation.
