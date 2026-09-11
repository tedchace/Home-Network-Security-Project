<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Python and XML Verification

## Verified inputs and results

Three XML files were supplied: Main pre, Main post, and Guest post. No Guest pre-segmentation XML was supplied. The earlier Guest baseline screenshot remains separate evidence.

| Dataset | XML start → finish (local timestamp text) | Hosts | Explicit open TCP records | Classified open records |
|---|---|---|---|---|
| Main pre | 2026-09-02 08:47:31 → 08:56:24 | 12 | 39 | 5 |
| Main post | 2026-09-04 10:17:31 → 10:30:15 | 10 | 34 | 1 |
| Guest post | 2026-09-04 14:15:57 → 14:18:50 | 4 | 14 | 2 |

All three identify TCP SYN scans with service detection and the same 1,000-port list. Main commands target 192.0.2.0/24; Guest targets 198.51.100.0/24. Main pre's internal output filename is home_network_nmap.xml, while the supplied file is named nmap_main_pre_segmentation.xml. The filenames therefore are not the sole basis of attribution. The Guest run summary reports four total addresses despite a /24 in its arguments; retain this discrepancy and do not certify exhaustive Guest coverage from this file.

Counts come from explicit host/port elements and state=open, not extraports summaries. All supplied host records are up; Main pre has 39 explicit open plus four explicit filtered records, explaining the 43-row service inventory. Its XML has one gateway host record, so Splunk's duplicate gateway row is not a second XML asset. The exact indexing/query cause remains unverified without Splunk event/config exports.

The Main CSVs match regenerated records field-for-field, including port/service strings and zero-open-port hosts. The supplied Markdown report matches the regenerated report's line content after allowing line-order differences. The script iterates sets for some host changes, so report ordering is not deterministic. A separate XML traversal agreed with the submitted parser for every supplied host and open service. This validates these inputs; it is not a claim of correctness for arbitrary XML.

Applying the documented Splunk port classification reproduces 5 → 1 from the Main XML. This reproduces the metric from source data without rerunning the actual Splunk panels. Saved panel filters, deduplication and Event 4625 extraction still need their own validation.

## Reconciliation of changes

The Main open-service total reconciles as **39 − 1 pool − 1 garage − 4 laptop − 1 workstation PostgreSQL + 2 newly observed host = 34**. Only the two IoT movements have matching Guest MAC evidence. The laptop's disappearance, new 192.0.2.82 host and workstation TCP/5432 disappearance remain observations with no demonstrated cause.

| Device | Main pre | Guest post | Correlation and remaining service |
|---|---|---|---|
| Garage Controller | 192.0.2.22 | 198.51.100.21 | Same MAC 02:00:00:00:00:0b and hostname; TCP/80 remains open on Guest |
| Pool Controller | 192.0.2.27 | 198.51.100.22 | Same MAC 02:00:00:00:00:01 and hostname; TCP/23 remains open on Guest |

Guest's scanner record is 198.51.100.88 with localhost-response, supporting the Guest vantage point. The later Nmap cross-segment screenshot shows 192.0.2.88 testing 198.51.100.22:23 as filtered. Thus the combined evidence supports a change in reachability across the boundary while the device service remains available from Guest at the earlier scan time. It does not establish complete or bidirectional isolation.

The workstation has no MAC in either Main XML and is matched by workstation.example.invalid; its Main address is 192.0.2.83 in both files. Missing laptop .74 has no corresponding Guest record. The new .82 MAC is different from the removed identities; this does not prove a newly purchased or previously unknown physical device.

## Script review

The [repository script](../Automation/network_security_report.py) contains the supplied logic with trailing whitespace normalized only. An unchanged original is retained privately with the source artifacts. It uses csv and ElementTree, reads two fixed filenames from the working directory, and writes the post CSV and Markdown report there. Its main function does not export the pre CSV or analyze Guest; the verifier calls the export/parser helpers for those datasets.

Limitations retained rather than silently changing the original project implementation:

- Host matching uses MAC, then hostname, then IP; missing/changed identifiers and key collisions can miscorrelate hosts. Supplied keys are nonempty and unique within each dataset.
- Host status and protocol are not explicitly filtered by the parser: any host element is included, and any open port protocol is accepted despite the TCP comment. The supplied files contain up hosts and TCP scans.
- Service identity includes the service label as well as port/protocol. A label change can look like removal/addition.
- Set iteration can change report ordering; the fixed output names can overwrite outputs in the chosen working directory.
- The segmentation paragraph is hard-coded for these named IoT devices; it is not a generic conclusion engine and does not itself inspect Guest XML.

## Reproduce the verification

Run from the repository root with Python 3:

```powershell
python -B Automation/verify_lab_data.py
```

The verifier reads local ignored XML under evidence/04-nmap/private and the private original report/CSVs under evidence/07-python/private/original-reports. It writes regenerated results to evidence/07-python/private/reproduced and checks CSV equality, report line-content equality, parser agreement and identity-key uniqueness. It does not perform network scans or access Splunk. Private files are required and intentionally absent from Git. [The evidence index](../evidence/07-python/README.md) maps filenames and hashes.

## Workflow context

[Project workflow context](project-workflow.md) distinguishes the user's contemporaneous notes from independently verified measurements. The original workflow is preserved without edits in a local ignored directory. It supplements this evidence; draft instructions and unfinished sections were not treated as new actions to execute.
