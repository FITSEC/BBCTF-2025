flag = b'cbftuhbf5_5{Fl31uHfFw_711b3G70_H_}rB3HrR'


def shuffle(target):
    for i in range(len(target) // 2):
        temp = target[i]
        target[i] = target[len(target) - i - 1]
        target[len(target) - i - 1] = temp

    return target

def do_the_thing(target):
    alice = bytearray(b"")

    for i in range(len(target) // 5):
        temp = target[i * 5: i * 5 + 5]
        alice += shuffle(temp)

    target = alice
    alice = bytearray(b"")

    for i in range(len(target) // 4):
        temp = target[i * 4: i * 4 + 4]
        alice += shuffle(temp)

    target = alice
    alice = bytearray(b"")

    for i in range(len(target) // 2):
        temp = target[i * 2: i * 2 + 2]
        alice += shuffle(temp)

    return alice

