<!-- Public derivative: identifiers are pseudonymized; see documentation/publication-sanitization.md. -->
# Python automation evidence

> Public screenshots are redacted derivatives. Addresses and names in the documentation are aliases, not literal transcriptions of the masked fields. Analysis was checked against private originals.

The supplied screenshot, script, two CSVs and Markdown report are integrated. Three XML files and the original workflow are preserved locally. Public images and reports have been sanitized; raw source data remains private.

| Artifact | Repository location | Handling |
|---|---|---|
| Report screenshot | [01-python-security-assessment-report.png](01-python-security-assessment-report.png) | Redacted image |
| Script | [network_security_report.py](../../Automation/network_security_report.py) | Original logic; trailing whitespace normalized; unchanged source retained privately |
| Main pre inventory | [asset_inventory_pre_segmentation.csv](../../reports/asset_inventory_pre_segmentation.csv) | Pseudonymized supplied CSV |
| Main post inventory | [asset_inventory_post_segmentation.csv](../../reports/asset_inventory_post_segmentation.csv) | Pseudonymized supplied CSV |
| Supplied report | [security_report.md](../../reports/security_report.md) | Pseudonymized supplied Markdown |
| Guest derived inventory | [asset_inventory_guest_post_segmentation.csv](../../reports/asset_inventory_guest_post_segmentation.csv) | Generated during verification; not a supplied artifact |
| Reconciliation | [python-xml-validation.md](../../documentation/python-xml-validation.md) | Results, scan metadata, identity correlation and limitations |
| Reproduction tool | [verify_lab_data.py](../../Automation/verify_lab_data.py) | Local-only verification; writes into ignored private output folder |

Source files came from the user's Router Configuration & Test Project and Python Scripts folders. [sha256.csv](sha256.csv) records public derivative filenames and hashes. The original filename plan remains in original-placeholder.txt (private; not published).

Raw XML is under `evidence/04-nmap/private/`; the unchanged script is `evidence/07-python/private/network_security_report.original.py`; the workflow is `documentation/private/original-project-workflow.docx`. These ignored files remain local. The *_sanitized reports now contain pseudonymized derivatives. Verification uses the private original reports, not the public aliases.

## Verified result

Main inventories reproduce 12 → 10 hosts and 39 → 34 open TCP service records. The chosen Splunk classification reproduces 5 → 1. Both supplied CSVs match regenerated records, and report lines match allowing set-related ordering differences. Guest XML records four hosts/14 open service records, including the same MyQ/Hayward MACs and their still-open TCP/80 and TCP/23 services. See the reconciliation for scope and the Guest run-summary discrepancy.
