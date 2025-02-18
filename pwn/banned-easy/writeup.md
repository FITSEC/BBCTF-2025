There is a buffer overflow when choosing to send a mean message which will overwrite the "ban" buffer in the .bss region.

If you send 32 bytes and then the string "LOSE" the `strcmp()` will pass and you will get the flag
```
AAAABBBBCCCCDDDDAAAABBBBCCCCDDDDLOSE
```

