This challenge is just a VM, the instructions done are as follows

```
   * mov reg[1], 0x67
   * inc reg[1]
   * mov reg[0], reg[1]
   * inc reg[0]
   * mov reg[1], <cur_char>
   * xor reg[1], reg[0]
   * mov reg[0], reg[1]
   * inc reg[0]
   * inc reg[0]
   * inc reg[0]
   * inc reg[0]
   * ret
```

And this is done for each character, translated into normal python code this is just `(char ^ 0x69) + 4`.

So here is the solve on my python REPL

```
>>> flag = b"\x0f\x0f\x0e\x21\x13\x16\x5c\x3a\x09\x5c\x06\x5e\x3a\x62\x25\x5e\x3a\x0f\x61\x2b\x11\x3a\x62\x25\x5e\x14\x3a\x61\x1f\x5e\x3a\x0e\x25\x5c\x09\x2\
9\x18"
>>> for alice in flag:
...     print(chr((alice - 4) ^ 0x69), end="")
...     

bbctf{1_l1k3_7H3_b4Nd_7H3y_4r3_cH1lL}>>>
```


