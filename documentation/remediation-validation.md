Finding 
--> 
Control implemented 
--> 
Validation method 
--> 
Observed result

(i.e.)
Pool controller TCP/23 exposed on Main LAN 
--> 
Moved IoT controller to Guest network 
--> 
- Nmap cross-segment TCP/23 probe
- Wireshark ICMP isolation test
- Python pre/post comparison
- Splunk pre/post analytics
-->
- TCP/23 filtered from Main
- No ICMP response observed
- IoT absent from Main discovery
- IoT present on Guest discovery