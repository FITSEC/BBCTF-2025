xor = b'\xbe\xef\xca\xfe'

sp = None
with open('secret_printer', 'rb') as f:
    sp = f.read()

with open('bad_printer', 'wb') as f:
    for i in range(0, len(sp), 4):
        for b, x in zip(sp[i:i+4], xor):
            print(hex(x))
            f.write((b ^ x).to_bytes(1,'big'))
