This challenge is written in pure assembly so that way people can't just depend on a decompiler like ghidra.

All this is doing is this

``` python
>>> flag = b"bbctf{7h3_d3c0mP1l3r_d03S_n07_l1k3_7H1s_0n3}"
>>> bytes = [0x89, 0xab, 0xf2]
>>> a = b""
>>> for i in range(len(flag)):
...     a += flag[i] ^ bytes[i % 3] + 2
```

But you have to figure that out in the assembly

