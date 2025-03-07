# Solution
## Extract DNS queries for "bigbrother.gov"
In wireshark apply following filter:
```
dns.qry.name == "bigbrother.gov"
```
---------------or----------------------- 
```sh
tshark -r suspicious_comms.pcap -Y 'dns.qry.name == "bigbrother.gov"' -T fields -e frame.number -e dns.id | sort -n | awk '{print $2}' | sed 's/0x//g' > extracted_hex.txt
```
## Sort by frame number to ensure correct flag order.
Remove the 0x prefix from the hexadecimal values.

## Output: 62626374667b6231675f627230746833725f356e303070316e677d
Convert hexadecimal to ASCII character
## Convert hex to text: 
```
bbctf{b1g_br0th3r_5n00p1ng}
```
