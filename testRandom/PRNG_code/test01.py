
"""
def lfsr(seed, taps):
    sr, xor = seed, 0
    i = 0
    while 1:
        for t in taps:
            xor += int(sr[t])

        if xor%2 == 0.0:
            xor = 0
        else:
            xor = 1

        sr = str(xor) + sr[:-1]
        xor = 0
        num = 0
        for j in range(len(seed)):
            # num += (sr[j]=='1' ? 2**j : 0)
            num += 2**j if sr[7-j]=='1' else 0
        print("sr: ", sr, "num: ", num)
        i+=1

        if sr == seed:
            break
    print("total number: ", i)
"""

# lfsr('11001001', (7, 5))      # example 8
# lfsr('10011001', (7,6,5,0))
# lfsr('10011011', (7,6,5,0))

# lfsr('10011011101011001100100111000011', (7,6,5,0)) # 32 bits going crazy
# "1001 1011 1010 1100 1100 1001 1100 0011"

import matplotlib.pyplot as plt
import numpy as np

seed = '10011011101011001100100111000011'
# taps = (7, 6, 5, 0)
taps = (4, 7, 5, 0)
sr = '10011011101011001100100111000011'

def lfsr_foo():
    global seed, taps, sr

    xor = 0
    for t in taps:
        xor += int(sr[t])

    if xor%2 == 0.0:
        xor = 0
    else:
        xor = 1

    sr = str(xor) + sr[:-1]
    xor = 0
    num = 0
    for j in range(len(seed)):
        # num += (sr[j]=='1' ? 2**j : 0) # c style
        num += 2**j if sr[7-j]=='1' else 0
    # print("sr: ", sr, "num: ", num)
    return num

"""
for _ in range(30):
    print(lfsr_foo() % 100)

testlist = [ lfsr_foo()%100 for _ in range(50)]
print(testlist)
"""

def generate_seq(n_sample, seq_length):
    ret = []
    for _ in range(n_sample):
        a = [lfsr_foo() for _ in range(seq_length)]
        ret.append(a)
    return np.array(ret)

test = generate_seq(400, 400)
# print(test)

plt.imshow(test, cmap= plt.cm.binary)
plt.title("baby LFSR flaw")
plt.show()
