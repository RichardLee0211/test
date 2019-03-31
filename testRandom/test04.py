# import
import math
import random

from scipy import special
from scipy.stats import chi
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npl

# Default to nearest neighbor interpolation, gray colormap
import matplotlib
matplotlib.rcParams["image.interpolation"] = "nearest"
matplotlib.rcParams["image.cmap"] = "gray"


if __name__ == "__main__":
    # np.fft.fft(np.exp(2j*np.pi*np.arange(8)/8))
    e = np.array([1, 0, 0, 1, 0, 1, 0, 0, 1, 1])
    n = e.size
    X = e*2 -1
    S = np.fft.fft(X)
    M = abs(S[0:int(S.size/2)])
    T = math.sqrt(2.995732274*n)
    N_0 = 0.95*n/2
    N_1 = 0
    for e in M:
        if e<T:
            N_1 += 1
    d = abs(N_1 - N_0) / math.sqrt(n*0.95*.05/2)
    P_value = special.erfc(d/math.sqrt(2))
    print(f"N_0={N_0:2.5f} N_1={N_1} d = {d}")
    print(f"P_value={P_value: 2.5f}")


def main05():
    f = open("./RandomData/random_homemakeLCG_65536.csv", "r")

    f.readline() # header
    N = 256
    X = np.ones((N, N))
    for i in range(N):
        for j in range(N):
            # X[i][j] = random.random()
            a = f.readline()
            # print(a)
            X[i][j] = int(a, base=16)
    f.close()
    print(npl.matrix_rank(X))

def main04():
    # this doesn't help to tell the different
    # f = open("./RandomData/random_rd_65536.clang++.csv", "r")
    # f = open("./RandomData/random_srand0_65536.clang++.csv", "r")
    # f = open("./RandomData/random_LCG02_65536.clang++.csv", "r")
    f = open("./RandomData/random_homemakeLCG_65536.csv", "r")

    f.readline() # header
    N = 256
    X = np.ones((N, N))
    for i in range(N):
        for j in range(N):
            # X[i][j] = random.random()
            a = f.readline()
            # print(a)
            X[i][j] = int(a, base=16)
    f.close()
    plt.imshow(X)
    plt.show()


def main03():
    files = [("./base.yml"), ("./anaconda_update.log")]
    # files = ["./base.yml", "./anaconda_update.log"]
    files_1 = ["it", 3] # 666, although it designed to store homogenous items
    files_2 = ("it", 4)
    print(f"{files[1]}")


def main02():
    """
    fig, ax = plt.subplots(1, 1)
    df = 78
    mean, var, skew, kurt = chi.stats(df, moments='mvsk')
    x = np.linspace(chi.ppf(0.01, df), chi.ppf(0.99, df), 100)
    ax.plot(x, chi.pdf(x, df), 'r-', lw=5, alpha=0.6, label='chi pdf')
    plt.show()
    """
    """
    x = range(0, 20)
    y = chi.pdf(x, 100)
    plt.plot(x, y)
    plt.show()
    """
    # print(f"P_value={chi.pdf(7.2, 10): 2.5f}")




BIT_WIDTH = 32
mySum =0

def main01():
    # x = 0b01010101
    # x = 0b11'1100'1010'0001'1011'1111'0111'1001 19
    x = 0b111100101000011011111101111001
    for j in range(BIT_WIDTH):
        b = (x>>j) & 0x1
        if b==1:
            mySum+=1
        else:
            mySum-=1
    S_abs = math.fabs(mySum)/math.sqrt(1)
    # P_value = special.erfc(S_abs/math.sqrt(2))
    P_value = special.erfc(1.6/math.sqrt(2))
    print(f"P_value = {P_value}")
