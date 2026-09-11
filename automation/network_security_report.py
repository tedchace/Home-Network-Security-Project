# SPDX-License-Identifier: MIT
#
# MIT License
#
# Copyright (c) 2026 Theodore Chace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Router Configuration Project Part 9: Python - Automation

# - Parse Scan/Log Data
# - Automate Asset Inventory
# - Compare Network States
# - Generate Security Reports

import csv
import xml.etree.ElementTree as ET

# Parse Nmap XML Scan Results
def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    assets = []

    for host in root.findall("host"):
        ipv4 = ""
        mac = ""
        vendor = ""
        hostname = ""

        # Get IPv4 address
        for address in host.findall("address"):
            addr_type = address.get("addrtype")

            if addr_type == "ipv4":
                ipv4 = address.get("addr", "")

            elif addr_type == "mac":
                mac = address.get("addr", "")
                vendor = address.get("vendor", "")

        # Get hostname
        hostname_elem = host.find("hostnames/hostname")
        if hostname_elem is not None:
            hostname = hostname_elem.get("name", "")

        # Get Open TCP Services
        open_services = []

        ports_elem = host.find("ports")

        if ports_elem is not None:
            for port in ports_elem.findall("port"):
                protocol = port.get("protocol", "")
                portid = port.get("portid", "")

                state_elem = port.find("state")
                service_elem = port.find("service")

                state = ""
                service = ""

                if state_elem is not None:
                    state = state_elem.get("state", "")

                if service_elem is not None:
                    service = service_elem.get("name", "")

                if state == "open":
                    open_services.append(
                        {
                            "port": portid,
                            "protocol": protocol,
                            "service": service
                        }
                    )
        assets.append(
            {
                "ip_address": ipv4,
                "mac_address": mac,
                "vendor": vendor,
                "hostname": hostname,
                "open_services": open_services
            }
        )
    return assets

# Create CSV Report for Scanned Results
def export_asset_inventory(assets, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = [
            "ip_address",
            "mac_address",
            "vendor",
            "hostname",
            "open_port_count",
            "open_ports",
            "services",
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for asset in assets:
            ports = []
            services = []

            for service in asset["open_services"]:
                ports.append(
                    f'{service["port"]}/{service["protocol"]}'
                )

                services.append(
                    f'{service["port"]}/{service["protocol"]}:{service["service"]}'
                )

            writer.writerow(
                {
                    "ip_address": asset["ip_address"],
                    "mac_address": asset["mac_address"],
                    "vendor": asset["vendor"],
                    "hostname": asset["hostname"],
                    "open_port_count": len(asset["open_services"]),
                    "open_ports": ", ".join(ports),
                    "services": ", ".join(services)
                }
            )

# Print Summary
def print_summary(assets):
    total_hosts = len(assets)
    total_open_services = sum(
        len(asset["open_services"])
        for asset in assets
    )

    print("\nHome Network Asset Inventory")
    print("=" * 50)

    print(f"Hosts parsed: {total_hosts}")
    print(f"Open services discovered: {total_open_services}")

    print("\nAssets:")

    for asset in assets:
        print("-" * 50)
        print(f'IP:        {asset["ip_address"]}')
        print(f'Hostname:  {asset["hostname"] or "Unknown"}')
        print(f'Vendor:    {asset["vendor"] or "Unknown"}')

        if asset["open_services"]:
            print("Open services:")

            for service in asset["open_services"]:
                print(
                    f'    {service["port"]}/{service["protocol"]}'
                    f'  -  {service["service"] or "Unknown"}'
                )
        else:
            print("Open services: None")

# Compare Network States
def compare_network_states(pre_assets, post_assets):
    def build_host_map(assets):
        host_map = {}

        for asset in assets:
            key = asset["mac_address"] or asset["hostname"] or asset["ip_address"]

            services = {
                (
                    service["port"],
                    service["protocol"],
                    service["service"]
                )
                for service in asset["open_services"]
            }

            host_map[key] = {
                "ip_address": asset["ip_address"],
                "hostname": asset["hostname"],
                "mac_address": asset["mac_address"],
                "vendor": asset["vendor"],
                "services": services
            }
        return host_map
    pre_map = build_host_map(pre_assets)
    post_map = build_host_map(post_assets)

    pre_keys = set(pre_map.keys())
    post_keys = set(post_map.keys())

    removed_hosts = pre_keys - post_keys
    added_hosts = post_keys - pre_keys
    common_hosts = pre_keys & post_keys

    service_changes = []

    for key in common_hosts:
        pre_services = pre_map[key]["services"]
        post_services = post_map[key]["services"]

        removed_services = pre_services - post_services
        added_services = post_services - pre_services

        if removed_services or added_services:
            service_changes.append(
                {
                    "host_key": key,
                    "pre": pre_map[key],
                    "post": post_map[key],
                    "removed_services": removed_services,
                    "added_services": added_services,
                }
            )

    return {
        "removed_hosts": [
            pre_map[key]
            for key in removed_hosts
        ],
        "added_hosts": [
            post_map[key]
            for key in added_hosts
        ],
        "service_changes": service_changes
    }

# Print Network Comparison
def print_network_comparison(comparison):
    print("\nNetwork State Comparison")
    print("=" * 50)

    print("\nHosts no longer observed from the Main LAN:")
    if comparison["removed_hosts"]:
        for host in comparison["removed_hosts"]:
            print(
                f'- {host["ip_address"]} '
                f'({host["hostname"] or "Unknown"})'
            )
    else:
        print("- None")
    print("\nNewly observed hosts:")
    if comparison["added_hosts"]:
        for host in comparison["added_hosts"]:
            print(
                f'- {host["ip_address"]} '
                f'({host["hostname"] or "Unknown"})'
            )
    else:
        print("- None")

    print("\nService changes on hosts observed in both scans:")

    if comparison["service_changes"]:
        for change in comparison["service_changes"]:
            host = change["post"]

            print("-" * 50)
            print(
                f'Host: {host["ip_address"]} '
                f'({host["hostname"] or "Unknown"})'
            )

            if change["removed_services"]:
                print("Removed or no longer observed services:")

                for port, protocol, service in sorted(
                    change["removed_services"]
                ):
                    print(
                        f"  - {port}/{protocol} "
                        f"{service or 'Unknown'}"
                    )
            if change["added_services"]:
                print("Added or newly observed services:")

                for port, protocol, service in sorted(
                    change["added_services"]
                ):
                    print(
                        f"  + {port}/{protocol} "
                        f"{service or 'Unknown'}"
                    )
    else:
        print("- No service changes detected")

# Generate Network Security Report
def generate_security_report(
        pre_assets,
        post_assets,
        comparison,
        output_file
):
    pre_host_count = len(pre_assets)
    post_host_count = len(post_assets)

    pre_service_count = sum(
        len(asset["open_services"])
        for asset in pre_assets
    )

    post_service_count = sum(
        len(asset["open_services"])
        for asset in post_assets
    )

    with open(output_file, "w", encoding="utf-8") as report:

        report.write("# Home Network Project Security Report\n\n")

        # Report Overview
        report.write("## Security Report Overview\n\n")
        report.write(
            "This report was automatically generated from Nmap XML "
            "reconnaissance data collected before and after network "
            "segmentation. The Python script compares discovered hosts "
            "and open network services to document observed changes in "
            "the Main LAN attack surface.\n\n"
        )

        # Pre-Segmentation State
        report.write("## Pre-Segmentation State\n\n")
        report.write(f"- Hosts observed: {pre_host_count}\n")
        report.write(f"- Open services observed: {pre_service_count}\n\n"
        )

        # Post-Segmentation State
        report.write("## Post-Segmentation State\n\n")
        report.write(f"- Hosts observed: {post_host_count}\n")
        report.write(f"- Open services observed: {post_service_count}\n\n"
        )

        # Changes Detected
        report.write("## Network State Changes\n\n")
            # Removed Hosts
        report.write("### Hosts No Longer Observed from the Main LAN\n\n"
        )

        if comparison["removed_hosts"]:
            for host in comparison["removed_hosts"]:
                report.write(
                    f'- {host["ip_address"]} - '
                    f'{host["hostname"] or "Unknown"}\n'
                )
        else:
            report.write("- None\n")
            # New Hosts
        report.write("\n### Newly Observed Hosts\n\n")

        if comparison["added_hosts"]:
            for host in comparison["added_hosts"]:
                report.write(
                    f'- {host["ip_address"]} - '
                    f'{host["hostname"] or "Unknown"}\n'
                )
        else:
            report.write("- None\n")
            # Service Changes
        report.write("\n## Service Exposure Changes\n\n")

        if comparison["service_changes"]:
            for change in comparison["service_changes"]:
                host = change["post"]

                report.write(
                    f'### {host["hostname"] or host["ip_address"]}\n\n'
                )

                report.write(
                    f'- current IP address: {host["ip_address"]}\n'
                )

                if change["removed_services"]:
                    report.write("- Services no longer observed: \n"
                    )
                    for port, protocol, service in sorted(
                        change["removed_services"]
                    ):
                        report.write(
                            f'  - {port}/{protocol} - '
                            f'{service or "Unknown"}\n'
                        )
                if change["added_services"]:
                    report.write(
                        "- Newly observed services: \n"
                    )

                    for port, protocol, service in sorted(
                        change["added_services"]
                    ):
                        report.write(
                            f'  - {port}/{protocol} - '
                            f'{service or "Unknown"}\n'
                        )
                report.write("\n")
        else:
            report.write(
                "No service changes were detected on hosts "
                "observed in both scans.\n\n"
            )

        report.write("## Segmentation Assessment\n\n")
        report.write(
            "The post-segmentation Main LAN scan showed changes in "
            "observed hosts compared to the results from the "
            "pre-segmentation Main LAN scan. The Hayward OmniLogic "
            "pool controller and MyQ garage door opener, which were "
            "previously observed on the Main LAN, were no longer "
            "observed in the post-segmentation Main LAN scan. This "
            "result is consistent with the intended migration of "
            "these IoT devices to the segmented Guest Network.\n\n"
        )

        report.write("## Additional Notes\n\n")
        report.write(
            "A host or service not appearing in a later network scan "
            "does not by itself prove that the asset or service was "
            "removed or successfully segmented. Devices may be offline, "
            "asleep, dynamically addressed, filtered, or otherwise "
            "unavailable during collection. Guest Network discovery, "
            "network configuration, device inventory, and isolation "
            "testing can provide additional evidence when validating "
            "segmentation. Automated comparison results should therefore "
            "be interpreted alongside these supporting data sources.\n"
        )

# Main
def main():
    pre_file = "nmap_main_pre_segmentation.xml"
    post_file = "nmap_main_post_segmentation.xml"

    pre_assets = parse_nmap_xml(pre_file)
    post_assets = parse_nmap_xml(post_file)

    print("\nPre-Segmentation Results")
    print_summary(pre_assets)

    print("\nPost-Segmentation Results")
    print_summary(post_assets)

    export_asset_inventory(
        post_assets,
        "asset_inventory_post_segmentation.csv"
    )

    comparison = compare_network_states(
        pre_assets,
        post_assets
    )

    print_network_comparison(comparison)

    generate_security_report(
        pre_assets,
        post_assets,
        comparison,
        "security_report.md"
    )

    print(
        "\nAutomation Outputs:"
        "\n- asset_inventory_post_segmentation.csv"
        "\n- security_report.md"
    )

if __name__ == "__main__":
    main()
