freedoms = None
with open('freedoms.txt', 'r') as f:
    freedoms = f.readlines()
bbctf = '62626374667b'
closing_brace = hex(ord('}'))[2:].ljust(2)

byte_map = [ {} for i in range(len(freedoms[0].strip()) // 2 - (len(bbctf) // 2 + 1)) ]

def analyze(freedom):
    global bbctf, byte_map
    for i in range(len(bbctf), len(freedom)-2,2):
        curr = freedom[i:i+2]
        bm_index = (i-len(bbctf))//2
        if curr in byte_map[bm_index]:
            byte_map[bm_index][curr] += 1
        else:
            byte_map[bm_index][curr] = 1

def print_max():
    global byte_map
    for c in byte_map:
        mk = 'NA'
        m = 0
        for key, value in c.items():
            if value > m:
                mk = key
                m = value
        print(mk, end='')
    print('\n')

null_in_body = []

for i in range(len(freedoms)):
    unmatched = True
    freedom = freedoms[i].strip()
    for j in range(0, len(bbctf), 2):
        if bbctf[j:j+2] == freedom[j:j+2]:
            unmatched = False
    if closing_brace == freedom[-2:]:
        unmatched = False
    if unmatched:
        #null_in_body.append(freedom)
        analyze(freedom)

print_max()
