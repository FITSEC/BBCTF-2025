Just reverse the program, all it does is grab each set of 5 letters and reverse them, then four, then two.


```python
def undo_the_thing(target):
    alice = bytearray(b"")

    for i in range(len(target) // 2):
        temp = target[i * 2: i * 2 + 2]
        alice += shuffle(temp)

    target = alice
    alice = bytearray(b"")

    for i in range(len(target) // 4):
        temp = target[i * 4: i * 4 + 4]
        alice += shuffle(temp)

    target = alice
    alice = bytearray(b"")

    for i in range(len(target) // 5):
        temp = target[i * 5: i * 5 + 5]
        alice += shuffle(temp)

    return alice
```

^^ this gets the flag, all you do is copy what the encrypt does but backwards order.

bbctf{5hufF13_5HuFfl3_w17H_b1G_Br07H3Rr}
