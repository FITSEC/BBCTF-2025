flag = b'tcbbfuh5{5_31FlfFuH71w_3G1b_H70rB_}rR3Hf'


def shuffle(target):
    for i in range(len(target) // 2):
        temp = target[i]
        target[i] = target[len(target) - i - 1]
        target[len(target) - i - 1] = temp

    return target

def do_the_thing(target, wash_count):
    alice = b""

    for i in range(len(target) // 5):
        temp = target[i * 5: i * 5 + 5]
        alice += shuffle(temp)

    bob = b""

    for i in range(len(alice)):
        bob += int.to_bytes(alice[(i + 1) % len(alice)], 1)

    print(bob)
    alice = bytearray(bob)

    if wash_count != 0:
        do_the_thing(alice, wash_count - 1)

    return alice


