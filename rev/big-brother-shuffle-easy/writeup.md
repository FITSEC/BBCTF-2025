Just reverse the program, all it does is grab each set of 5 letters and reverse them, then shift all the letters over one, then recursively call. If you play around with it you'll see I recursively called 10 times on my program

```python
def undo_the_thing(target, count):
    alice = b""

    for i in range(len(target)):
        alice += int.to_bytes(target[(len(target) - 1 + i) % len(target)], 1)

    bob = bytearray(b"")

    for i in range(len(alice) // 5):
        temp = bytearray(alice[i * 5: i * 5 + 5])
        bob += shuffle(temp)

    if count != 0:
        undo_the_thing(bob, count - 1)

    return bob

print(undo_the_thing(bytearray(flag), 10))
```


bbctf{5hufF13_5HuFfl3_w17H_b1G_Br07H3Rr}
