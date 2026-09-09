# Home Network Infrastructure & Security Hardening Lab

## Executive Summary

## Project Objectives

## Network Architecture
### Before
- network-before.png
### After
- network-after.png

## Security Assessment Workflow
Deploy-->Baseline-->Assess-->Identify Exposure-->Remediate-->Validate-->Monitor-->Automate

Nmap
- attack-surface discovery
Wireshark
- packet-level validation
Wifite / Aircrack-ng
- authorized wireless-security assessment
Network segmentation
- preventive control
Splunk
- monitoring + detection
Python
- repeatable analysis + reporting

## Key Findings & Remediation
- Finding 1 - Wireless credential exposure
    - Wifite handshake capture
    - Aircrack-ng controlled dictionary recovery
    - WPA3 configuration
- Finding 2 - IoT service exposure
    - Nmap - pool controller TCP/23

## Validation Results
- Nmap Main --> Guest TCP/23 = filtered
- Wireshark Main --> Guest ICMP = no response observed

## Monitoring & Detection
### Monitoring
- Splunk segmentation comparison dashboard
    - panel showing "open services" and "security-relevant services" pre --> post
### Detection Engineering
- Windows failed-login SPL --> Triggered Alert
    - (put one in ReadMe and link to 2nd in Splunk Evidence directory)

## Security Automation
- Python-generated security_report.md

## Technologies Used

## Repository Structure

## Skills Demonstrated

## Limitations

## Responsible Use