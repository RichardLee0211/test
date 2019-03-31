from scipy import special
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
import numpy.linalg as npl

import math
import sys

"""
x = np.linspace(-3, 3)
plt.plot(x, special.erfc(x))
plt.xlabel('$x$')
plt.ylabel('$erfc(x)$')
plt.show()
"""

BIT_WIDTH = 32
N = 5000 # number of lines
# N = 32*16 # number of lines
n = N*BIT_WIDTH

def frequency_test(f):
    mySum = 0
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

    S_abs = math.fabs(mySum)/math.sqrt(N*BIT_WIDTH)
    P_value = special.erfc(S_abs/math.sqrt(2))
    print(f"====frequency_test: ")
    print(f"mySum={mySum}")
    print(f"S_abs={S_abs:2.5f}")
    print(f"P_value = {P_value:2.5f}")

def frequency_test_block(f):
    M = BIT_WIDTH # choose to 32 for convinience
    X_obs = 0.0
    X_obs_4M = 0.0
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        pi_x = 0.0
        mySum = 0
        for j in range(BIT_WIDTH):
            b = (a>>j) & 0x1
            if b==1:
                mySum+=1
        pi_x = mySum/BIT_WIDTH
        X_obs_4M +=  (pi_x-0.5)**2
        # print(f"pi_x={pi_x:0.5f}  X_obs_4M={X_obs_4M:0.5f}")

    X_obs = 4*M*X_obs_4M
    print(f"====frequency_test_block: ")
    print(f"X_obs_4M={X_obs_4M:f}")
    print(f"X_obs={X_obs:f}")
    P_value = chi2.pdf(X_obs, N-1)
    print(f"P_value={P_value:2.5f}")

def run_test(f):
    mySum = 0
    f.readline() # header of csv file
    for i in range(N):
        a = int(f.readline(), base=16)
        for j in range(BIT_WIDTH):
            b = (a>>j) & 0x1
            if b==1:
                mySum+=1
    pi = mySum/(N*BIT_WIDTH)
    pi_test = abs(pi-0.5)
    tau = 2/math.sqrt(n)
    if pi_test>tau:
        print(f"bad")

    old_b = 0x0
    V_obs = 1
    # f.seek(SEEK_SET)
    f.seek(0)
    f.readline() # header of csv file
    for i in range(N):
        a = int(f.readline(), base=16)
        ## compare last bit of last line with a[0]
        a_0 = a>>(BIT_WIDTH-1)
        if old_b != a_0:
            V_obs += 1
        ## LOOP bits in the line to compare a[x] with a[x+1]
        for j in range(BIT_WIDTH):
            if j == BIT_WIDTH-1:
                ## preserve old_b to compare it with first bit in the next line
                old_b =  (a>>(BIT_WIDTH-1-j)) &0x1
            else:
                b = (a>>(BIT_WIDTH-1-j)) &0x1
                b_1 = (a >> (BIT_WIDTH-1-j-1)) &0x1
                if b != b_1:
                    V_obs += 1

    x = abs(V_obs - 2*n*pi*(1-pi)) / (2*math.sqrt(2*n)*pi*(1-pi))
    P_value = special.erfc(x)
    print(f"====run test: ")
    print(f"n={n} V_obs= {V_obs} pi={pi}")
    print(f"P_value = {P_value:2.5f}")

def run_test_block(f):
    K=5; M=128;
    V = [0, 0, 0, 0, 0, 0]
    pi = [ 0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124 ]
    num_block = int(N/4)
    f.readline() # header
    for i in range(num_block):
        a_0 = int(f.readline(), base=16)
        a_1 = int(f.readline(), base=16)
        a_2 = int(f.readline(), base=16)
        a_3 = int(f.readline(), base=16)
        a = [ a_0, a_1, a_2, a_3 ]
        # old_b = 0x0
        max_run = 0
        current_run = 0
        # print(f"{a:b}")
        for k in range(4):
            for j in range(BIT_WIDTH):
                b = (a[k]>>(BIT_WIDTH-1-j)) &0x1
                if b==0x1:
                    current_run+=1
                else:
                    if current_run > max_run:
                        max_run = current_run
                    current_run = 0
        if max_run<=4:
            V[0] += 1
        elif max_run == 5:
            V[1] += 1
        elif max_run == 6:
            V[2] += 1
        elif max_run == 7:
            V[3] += 1
        elif max_run == 8:
            V[4] += 1
        elif max_run >= 9:
            V[5] += 1
        else:
            assert False
        max_run = 0

    print(f"====run_test_block: ")
    X_obs = 0.0
    for i in range(K+1):
        X_obs += ((V[i] - num_block*pi[i])**2 / (num_block*pi[i]))
    P_value = chi2.pdf(X_obs, K);
    print(f"X_obs= {X_obs:2.5f}")
    print(f"P_value={P_value:2.5f}")

# I highly doubt it when it come it F_m-1 0.576 and int randomness
def binary_matrix_rank_test(f):
    M=32
    X = np.zeros((M, M))
    F_M = 0
    F_M_1 = 0
    F_else = 0
    N_block = int(N/M)
    f.readline() # header
    for k in range(N_block):
        for i in range(M):
            a = int(f.readline(), base=16)
            for j in range(BIT_WIDTH):
                b = (a>>j) & 0x1
                X[i][j] = b
        rank = npl.matrix_rank(X)
        # print(f"rank={rank}")
        if rank == M:
            F_M += 1
        elif rank == M-1:
            F_M_1 += 1
        elif rank < M-1 and rank > 0:
            F_else += 1
        else:
            assert false
    X_obs = (F_M-0.2888*N_block)**2 / (0.2888*N_block) + \
            (F_M_1 - 0.5776*N_block)**2 / (0.5776*N_block) + \
            (F_else - 0.1336*N_block)**2 / (0.1336*N_block)
    P_value = chi2.pdf(X_obs, 2)
    print(f"====binary_matrix_rank_test:")
    print(f"F_M={F_M} F_M-1={F_M_1} F_else={F_else}")
    print(f"X_obs={X_obs:2.5f}")
    print(f"P_value={P_value:2.5f}")

def spectral_test(f):
    arr_e = np.array()
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            arr_e.append(b)







if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file_num>")
        sys.exit(-1)

    files = [
            "./RandomData/random_rd.clang++.csv",
            "./RandomData/random_srand0_01.clang++.csv",
            "./RandomData/random_srand2_01.clang++.csv",
            "./RandomData/random_LCG01_01.clang++.csv",
            "./RandomData/random_LCG02_01.clang++.csv",
            "./RandomData/random_mt19937_01.clang++.csv",
            "./RandomData/random_ranlux24base_01.clang++.csv",
            "./RandomData/random_homemakeLCG_01.csv.clang++.csv",
            "./RandomData/random_homemakeLCG_02.csv.clang++.csv"
            ]
    i = int(sys.argv[1])
    print(f"file: {files[i]}")
    f = open(files[i], "r")

    # frequency_test(f)
    # frequency_test_block(f)
    # run_test(f)
    # run_test_block(f)
    binary_matrix_rank_test(f)
    f.close()

    # old styple in python
    # print(f"S_abs=%2.5f"%S_abs)
    # print("P_value = %2.5f"%P_value)
