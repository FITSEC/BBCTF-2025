# Solution
## Step 1: Open the PCAP in Wireshark**

1. Open the file:
   wireshark brotherhood_cipher.pcap
 
2. Apply a filter to show only relevant packets:

  udp.port == 1337


---

## Step 2: Extract Payloads**

- Look at the Packet Bytes section.
- Identify Sequence Number and Payload in each UDP packet.
- Ignore Packet ID and Checksum.

Note:
- Extract the Payloads by going to the Packet Bytes Pane (Bottom Section).
- Look for Hex Data in the UDP Payload.
- The structure of each packet is:

  ```
  [ Packet ID | Sequence Number | Payload | Checksum ]
  ```

Example payload:
  ```
  0923 000b 4269 6720 6c
  ```
  - `0923` → Random Packet ID (Ignore)
  - `000b` → Sequence Number (Use this to sort)
  - `4269 6720 6c` → Payload (Extract and keep)

Manually note down each sequence number & payload:
```
Seq 0 → "bbct"
Seq 1 → "f{0p3"
```
Ignore the checksum (last byte).

---

Step 3: Reconstruct the Message

- Sort the extracted payloads by sequence number.
- Concatenate them to form the flag.
- Convert hex to ASCII.

### Important Notes:
- Ignore the first 4 bytes (0923, 252a, 0d76) – they are Packet IDs.
- Sequence numbers (000b, 0000, 0008) indicate order.
- Extract only the payload bytes (e.g., `4269 6720 6c, 6262 6374 17`).
- Ignore the last checksum byte.

---

Step 4: Sort Data by Sequence Number

| Seq Number (HEX) | Payload (HEX) | Decoded |
|------------------|--------------|---------|
| 0000            | 6262 6374     | bbct    |
| 0001            | 6637 3070     | f{0p3   |
| 0002            | 7234 746f     | r4to    |
| 0003            | 6e5f 7331     | n_s1    |
| 0004            | 6c33 6e74     | l3nt    |
| 0005            | 5f33 7933     | _3y3    |
| 0006            | 5f31 735f     | _1s_    |
| 0007            | 6730 7d       | g0}     |

### Final Flag:
```
bbctf{0p3r4t10n_s1l3nt_3y3_1s_g0}
```

---

### Alternative Solution (Command Line + Python)

#### Using tshark to Extract Hex Data
```bash
tshark -r brotherhood_cipher.pcap -Y "udp.port == 1337" -x > extracted_packets.txt
```

#### Python Script to Decode the Flag
```python
import re

def extract_flag(file_path):
    extracted_packets = {}

    with open(file_path, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        # Match valid hex bytes in the payload
        hex_match = re.findall(r'([0-9a-f]{2})', lines[i])

        if len(hex_match) > 6:  # Ensure it's a valid data packet
            seq_num = int(hex_match[2] + hex_match[3], 16)  # Extract sequence number
            payload = "".join(hex_match[4:-1])  # Extract payload, ignore checksum

            if all(c in "0123456789abcdef" for c in payload):  # Ensure valid hex
                extracted_packets[seq_num] = payload

    # Sort by sequence number
    sorted_payloads = [extracted_packets[i] for i in sorted(extracted_packets.keys()) if i in extracted_packets]

    final_flag_hex = "".join(sorted_payloads)

    try:
        final_flag = bytes.fromhex(final_flag_hex).decode("utf-8")
        print("\n🔹 Reconstructed Flag:", final_flag)
    except UnicodeDecodeError:
        print("\n⚠ Error: Some flag parts are missing due to packet loss. Try analyzing missing packets manually.")

# Run extraction script
extract_flag("extracted_packets.txt")
```

### Final Flag:
```
bbctf{0p3r4t10n_s1l3nt_3y3_1s_g0}
```



