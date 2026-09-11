# Publication Sanitization

The public working-tree files are derivatives of the original lab evidence. Redaction changes presentation, not the recorded technical outcomes. Original screenshots, reports, workflow files and source mappings are retained in a private backup outside this repository; local ignored source data also supports verification.

## Removed or Replaced

- Screenshots: recovered password, dictionary candidates, derived key material, SSIDs/BSSIDs, MAC addresses, personal hostnames/accounts, email addresses, personal filesystem paths, device identifiers, phone-profile/media details, and identifying portions of reflections.
- Network identifiers: original local IPv4/IPv6 addresses and identifying packet-byte panes are masked in screenshots. Fingerprint blocks containing encoded identifiers or serial numbers are masked as whole regions.
- Reports and documentation: Main uses the documentation prefix `192.0.2.0/24`; Guest uses `198.51.100.0/24`. These are illustrative aliases, not live configuration. Hostnames use `example.invalid`; MAC aliases use locally administered values. Stable aliases retain cross-file device correlation. Public DNS addresses, loopback, masks, ports, counts and service labels remain where useful.
- PNG files are freshly encoded RGB images without original ancillary metadata. The dashboard PDF is rebuilt from redacted raster pixels, excluding original PDF objects, attachments and metadata. Source manifests contain public filenames and derivative hashes rather than personal source paths.

Both ordinary report filenames and the previously empty *_sanitized variants now contain pseudonymized data. Private originals are not referenced as public downloadable evidence. The verification helper compares raw XML against private original reports so pseudonymization does not create false mismatches.

## Checks and Limits

All 49 screenshot derivatives and the dashboard PDF were visually reviewed. OCR was used to identify text and check for residual identifiers, supplemented by manual masks for fields OCR missed. Public text was searched for original identifiers, and CSV row counts, service records and device correlations were checked after pseudonymization. Public image/PDF hashes are recorded in each evidence index's manifest.

Masks can hide context alongside identifiers. Detailed findings describe the original observations; public images do not independently expose every identifying field. No synthetic screenshot content or replacement test results were generated.

Raw captures, raw XML, the original workflow and private verification outputs remain excluded by .gitignore. Do not force-add private files. The clean publication archive excludes all private files and Git metadata.

Existing Git history contains author/committer email metadata and was not rewritten. The working-tree sanitization does not change that metadata. Publishing the existing Git history requires a separate decision about attribution/privacy; the clean archive provides a history-free publication source. No commit, push or remote publication was performed.
