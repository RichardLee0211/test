from scipy import special
import matplotlib.pyplot as plt
import numpy as np
import math as math

"""
x = np.linspace(-3, 3)
plt.plot(x, special.erfc(x))
plt.xlabel('$x$')
plt.ylabel('$erfc(x)$')
plt.show()
"""

mySum = 0
BIT_WIDTH = 32
N = 5000 # number of lines

if __name__ == "__main__":
    # f = open("./RandomData/random_fake.csv", "r")
    # f = open("./RandomData/randomLCG.csv", "r") # P_value: 0.3
    # f = open("./RandomData/randomLCG2.csv", "r") # P_value: 0.00000
    # f = open("./RandomData/random_00.clang++.csv", "r") # P_value: 0.00000
    # f = open("./RandomData/random_01.clang++.csv", "r") # P_value: 0.00000

    # f = open("./RandomData/random_rd.clang++.csv", "r") # P_value: 0.77564
    # f = open("./RandomData/random_LCG01_01.clang++.csv", "r") # P_value: 0.53855
    # f = open("./RandomData/random_LCG02_01.clang++.csv", "r") # P_value: 0.65271
    # f = open("./RandomData/random_mt19937_01.clang++.csv", "r") # P_value: 0.14156
    f = open("./RandomData/random_ranlux24base_01.clang++.csv", "r") # P_value: 0.61356
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>j) & 0x1
            if b==0:
                mySum-=1
            else:
                mySum+=1

    f.close()

    S_abs = math.fabs(mySum)/math.sqrt(N*BIT_WIDTH)
    P_value = special.erfc(S_abs/math.sqrt(2))
    print(f"mySum={mySum}")
    print(f"S_abs={S_abs:2.5f}")
    print(f"P_value = {P_value:2.5f}")
    # old styple in python
    # print(f"S_abs=%2.5f"%S_abs)
    # print("P_value = %2.5f"%P_value)

    # x = 1.3234
    # print(x.": ". special.erfc(x))
    # print(f"erfc({x}):{special.erfc(x)}")
