import random
import binascii

def enc_flag(flag):
    numbers = list(range(len(flag)))
    random.shuffle(numbers)
    freedom_text = b''
    for f, n in zip(flag, numbers):
        freedom_text += (ord(f) ^ n).to_bytes(1, 'big')
    print(binascii.hexlify(freedom_text).decode())

flag = 'bbctf{m4yb3_y0u_r3a11y_4r3_fr33}'
for i in range(1000000):
    enc_flag(flag)
