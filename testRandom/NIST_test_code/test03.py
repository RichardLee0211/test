## NIST random test baby implement
#
from scipy import special
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2
import numpy.linalg as npl

import math
import sys
# import os

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
    f.seek(0)
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
    f.seek(0)
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
    f.seek(0)
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
    f.seek(0)
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
    f.seek(0)
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

# TODO: what ttf return means and how to use it
def spectral_test(f):
    # arr_e = np.array()
    list_e = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            list_e.append(b)
    n = len(list_e)
    arr_e = np.array(list_e)
    arr_X = arr_e *2 -1
    arr_S = np.fft.fft(arr_X)
    arr_M = abs(arr_S[0:int(arr_S.size/2)])
    T = math.sqrt(2.995732274*n)
    N_0 =  0.95*n/2
    N_1 = 0
    for e in arr_M:
        if e<T:
            N_1 += 1
    d = abs(N_1 - N_0) / math.sqrt(n*0.95*.05/2)
    P_value = special.erfc(d/math.sqrt(2))
    print("====spectral_test: ")
    print(f"N_0={N_0:2.5f} N_1={N_1} d = {d}")
    print(f"P_value={P_value: 2.5f}")

def non_overlapping_template_matching_test(f):
    M = 32   # M should be 131'072, set to 32 for convinience
    N = 3000
    m = 8    # m = 9~148 should be tested
    B = 0x05 # this pattern should not be a matter, as it would be evenly appear
    arr_W = np.zeros(N)
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        j = 0
        while j <= BIT_WIDTH-m: # update j in the loop body
            b = (a>>(BIT_WIDTH-m-j)) & 0xFF
            if b==B:
                arr_W[i] += 1
                j += m
            else:
                j += 1
    mu = (M-m+1) / math.pow(2, m)
    sigma_sq = M *(1/math.pow(2, m) - (2*m-1)/math.pow(2, 2*m))
    X_obs = 0.0
    for i in range(N):
        X_obs += (arr_W[i] - mu)**2 / sigma_sq
    X_obs /= N # TODO: I doubt formula given in 2015 report, I add this line to make it look good
    P_value = chi2.pdf(X_obs, 2)
    print(f"====non_overlapping_template_matching_test: ")
    print(f"mu={mu:.5f} sigma_sq={sigma_sq:.5f}")
    print(f"total match={np.sum(arr_W)}")
    print(f"X_obs={X_obs:2.5f}")
    print(f"P_value={P_value:2.5f}")

# M should not be 32, the int generator different from sequence generator
def overlapping_template_matching_test_02(f):
    M = 32   # M should be 131'072, set to 32 for convinience
    N = 5000
    m = 4    # m = 9~148 should be tested
    B = 0x5 # this pattern should not be a matter
    arr_V = np.zeros(6)
    # TODO: this need to recalculate
    arr_Pi_02 = np.array([.324652, .182627, .142670, .106645, .077147]) # provided by NIST800-22, but different parameters
    arr_Pi = np.array([.367879, .183940, .137955, .099634, .069935, .140657])
    # arr_Pi = np.array([.2940, .4366, .2206, .0462, .0024, .0002])
    f.seek(0)
    f.readline() # header
    for i in range(N):
        mySum = 0
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        j = 0
        while j <= BIT_WIDTH-m: # update j in the loop body
            b = (a>>(BIT_WIDTH-m-j)) & ((0x1<<(m+1)) -1)
            if b==B:
                mySum += 1
            j += 1
        if mySum>=5:
            arr_V[5] += 1
        else:
            arr_V[mySum] += 1

    mu = (M-m+1) / math.pow(2, m)
    mylambda = mu/2
    X_obs = 0.0
    for i in range(6):
        X_obs += (arr_V[i] - N*arr_Pi[i])**2 / (N*arr_Pi[i])
    # P_value_02 = chi2.pdf(X_obs, 5)
    P_value = 1- special.gammainc(5/2, X_obs/2)

    print(f"====overlapping_template_matching_test: ")
    print(f"mu={mu:.5f} mylambda={mylambda:.5f}")
    for i in range(6):
        # print(f"arr_V[{i}]: {arr_V[i]} \texpectedValue: {(arr_Pi[i]*N):2.5f}")
        print(f"arr_V[{i}]: {arr_V[i]} \tratios:{arr_V[i]/N}")
    print(f"X_obs={X_obs:2.5f}")
    print(f"P_value={P_value:2.5f}")
    # print(f"P_value_02={P_value_02:2.5f}")

def overlapping_template_matching_test(f):
    # N = 5000
    N = 65536
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)
    arr_bits = np.array(bits)

    # parameters
    M = 1032
    N = int(len(arr_bits) / M) # num of blocks
    m = 9    # m = 9~148 should be tested
    B = 0x054 # this pattern should not be a matter
    arr_Pi = np.array([.367879, .183940, .137955, .099634, .069935, .140657])

    arr_V = np.zeros(6)
    tmp = 0.0
    # per block
    for k in range(N):
        mySum = 0
        # per sequence
        for i in range(M-m):
            tmp=0.0
            for j in range(m):
                tmp += arr_bits[k*M+i+j] * 2**(m-1-j)
            if tmp == B:
                mySum += 1
        if mySum >= 5:
            arr_V[5] += 1
        else:
            arr_V[mySum] += 1

    mu = (M-m+1) / math.pow(2, m)
    mylambda = mu/2
    X_obs = 0.0
    for i in range(5):
        X_obs += (arr_V[i] - N*arr_Pi[i])**2 / (N*arr_Pi[i])
    P_value = chi2.pdf(X_obs, 5)

    print(f"====overlapping_template_matching_test: ")
    print(f"mu={mu:.5f} mylambda={mylambda:.5f}")
    for i in range(6):
        print(f"arr_V[{i}]: {arr_V[i]} \texpectedValue: {(arr_Pi[i]*N):.5f}")
    print(f"X_obs={X_obs:2.5f}")
    print(f"P_value={P_value:2.5f}")




def universal_statistical_test(f):
    N = 5000 # line
    L = 8 # choose 8 as it is easy for implement
    Q = 2560 # according to NIST
    table = np.zeros(int(math.pow(2, L)))

    mySum = 0.0
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        for j in range(4): # BIT_WIDTH/L
            b = (a >> ((4-1-j)*8)) &0xFF
            if i*4+j >= Q:
                mySum += math.log2((i*4+j) - table[b])
            table[b] = i*4+j

    K = N*4 - Q
    f_n = mySum / K
    expectedValue = 7.1836656
    variance = 3.238
    c = 0.6+(8/15)*math.pow(K, -3/8)
    delta = c*math.sqrt(variance/K)
    x= abs((f_n-expectedValue)/(math.sqrt(2)*delta))
    P_value = special.erfc(x)
    print(f"====universal_statistical_test: ")
    print(f"f_n={f_n:2.5f} expectedValue=7.1836656")
    print(f"P_value = {P_value:2.5f}")

# this could be expensive for now
# TODO: Berlekamp-Massey algorithm
def linear_complexity_test(f):
    pass

def serial_test(f):
    # using list for now
    N = 5000
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)

    m=3 # choose 3
    V_3 = np.zeros(int(2**3))
    V_2 = np.zeros(int(2**2))
    V_1 = np.zeros(int(2**1))
    for i in range(len(bits)):
        v_3 = bits[i]*(2**2) + bits[(i+1)%len(bits)]*(2) + bits[(i+2)%len(bits)]
        v_2 = bits[i]*2 + bits[(i+1)%len(bits)]
        v_1 = bits[i]
        V_3[v_3] += 1
        V_2[v_2] += 1
        V_1[v_1] += 1
    print(f"V_3 = {V_3}")
    print(f"V_2 = {V_2}")
    print(f"V_1 = {V_1}")

    V_3_sum = 0.0
    V_2_sum = 0.0
    V_1_sum = 0.0
    for i in range(len(V_3)):
        V_3_sum += V_3[i]**2
    for i in range(len(V_2)):
        V_2_sum += V_2[i]**2
    for i in range(len(V_1)):
        V_1_sum += V_1[i]**2
    psi_3_sq = 8/(N*BIT_WIDTH) * V_3_sum - (N*BIT_WIDTH)
    psi_2_sq = 4/(N*BIT_WIDTH) * V_2_sum - (N*BIT_WIDTH)
    psi_1_sq = 2/(N*BIT_WIDTH) * V_1_sum - (N*BIT_WIDTH)

    delta_psi_sq = psi_3_sq - psi_2_sq
    delta_sq_psi_sq = psi_3_sq - 2*psi_2_sq + psi_1_sq

    P_value_1 = 1 - special.gammainc(2, delta_psi_sq/2)
    P_value_2 = 1 - special.gammainc(1, delta_sq_psi_sq/2)

    print("====serial_test:")
    print(f"delta_psi_sq = {delta_psi_sq:2.5f}")
    print(f"delta_sq_psi_sq = {delta_sq_psi_sq:2.5f}")
    print(f"P_value_1={P_value_1:2.5f}")
    print(f"P_value_2={P_value_2:2.5f}")

def approximate_entropy_test(f):
    N = 5000
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)

    m=3 # choose 3
    subsequence_3 = 0
    subsequence_4 = 0

    arr_3 = np.zeros(int(2**3))
    arr_4 = np.zeros(int(2**4))
    for i in range(len(bits)):
        b_3 = bits[i]*(2**2) + bits[(i+1)%len(bits)]*(2) + bits[(i+2)%len(bits)]
        b_4 = bits[i]*(2**3) + bits[(i+1)%len(bits)]*(2**2) + bits[(i+2)%len(bits)]*(2)+bits[(i+3)%len(bits)]
        arr_3[b_3] += 1
        arr_4[b_4] += 1
    print(f"arr_3={arr_3}")
    print(f"arr_4={arr_4}")
    arr_3 /= len(bits)
    arr_4 /= len(bits)

    varphi_3 = 0.0
    varphi_4 = 0.0
    for i in range(len(arr_3)):
        varphi_3 += arr_3[i] * math.log(arr_3[i])
    for i in range(len(arr_4)):
        varphi_4 += arr_4[i] * math.log(arr_4[i])

    X_sq = 2*len(bits)*(math.log(2) - (varphi_3 - varphi_4))
    P_value = 1 - special.gammainc(4, X_sq/2)
    print("====approximate_entropy_test:")
    print(f"P_value={P_value:2.5f}")

def Cum_sum_test(f):
    N = 5000
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)

    arr_bits = np.array(bits)
    arr_bits = 2*arr_bits -1
    arr_cumsum = np.cumsum(arr_bits)
    # print(arr_bits)
    print(arr_cumsum)

    arr_cumsum_abs =  abs(arr_cumsum)
    z = max(arr_cumsum_abs)
    # print(z)

    from scipy.stats import norm
    # norm.cdf()

    n = len(arr_bits)
    k_start = int((-n/z + 1)/4)
    k_end = int((n/z -1) /4)
    print(f"k_start={k_start}")
    print(f"k_end={k_end}")

    sum_1 = 0.0
    for k in range(k_start, k_end+1):
        sum_1 += norm.cdf((4*k+1)*z/math.sqrt(n)) - norm.cdf((4*k-1)*z/math.sqrt(n))

    k_start_2 = int((-n/z -3)/4)
    k_end_2 = int((n/z -1)/4)
    sum_2 = 0.0
    for k in range(k_start_2, k_end_2+1):
        sum_2 += norm.cdf((4*k+3)*z/math.sqrt(n)) - norm.cdf((4*k+1)/math.sqrt(n))

    P_value = 1 - sum_1 + sum_2
    print(f"====Cum_sum_test:")
    print(f"P_value={P_value:2.5f}")

def random_excursions_test(f):
    N = 5000
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)

    arr_bits = np.array(bits)
    arr_bits = 2*arr_bits -1
    arr_cumsum = np.cumsum(arr_bits)
    # print(arr_bits)
    print(f"bits length={len(arr_cumsum)}")
    # plt.plot(arr_cumsum)
    # plt.show()
    # sys.exit(-1)

    # ciecles[i], (i+1)th circle
    # X standard for -4,-3,-2,-1,1,2,3,4
    # circles[i][X] for times of X occur in circle[i]
    circles = []
    a = np.zeros(8)
    for i in range(len(arr_cumsum)):
        if arr_cumsum[i]==0:
            circles.append(a)
            a = np.zeros(8)
        elif arr_cumsum[i]<=4 and arr_cumsum[i]>=-4:
            index = arr_cumsum[i]+4 if arr_cumsum[i] < 0 else arr_cumsum[i]+3
            a[index] += 1
        else:
            pass
    circles.append(a)
    J = len(circles)
    print(f"len(circles)={J}")
    # print(f"circles={circles}")

    # V[K][X], X occurs K times
    # K = 0, 1, 2, 3, 4, >=5
    # X = -4, -3, -2, -1, 1, 2, 3, 4 shift to range(8)
    V = np.array([np.zeros(8) for i in range(6)])
    for i in range(len(circles)):
        for j in range(8):
            K = int(circles[i][j]) if circles[i][j]<5 else 5
            V[K][j] += 1
    print(f"V[K][X]: X occurs K times in all circles\n{V}")

    # pi[K][X], thoery ratio that X show up K times in a circle
    # from NIST800-22
    pi = [[0 for i in range(5)] for j in range(6)]
    pi[0][1] = 0.5000; pi[1][1]=0.2500; pi[2][1]=0.1250; pi[3][1]=0.0625; pi[4][1]=0.0312; pi[5][1]=0.0312;
    pi[0][2] = 0.7500; pi[1][2]=0.0625; pi[2][2]=0.0469; pi[3][2]=0.0352; pi[4][2]=0.0264; pi[5][2]=0.0791;
    pi[0][3] = 0.8333; pi[1][3]=0.0278; pi[2][3]=0.0231; pi[3][3]=0.0193; pi[4][3]=0.0161; pi[5][3]=0.0804;
    pi[0][4] = 0.8750; pi[1][4]=0.0156; pi[2][4]=0.0137; pi[3][4]=0.0120; pi[4][4]=0.0105; pi[5][4]=0.0733;

    X_obs_1 = 0.0
    X_obs_2 = 0.0
    X_obs_3 = 0.0
    X_obs_4 = 0.0
    for K in range(6):
        X_obs_1 += (V[K][4] - J*pi[K][1])**2 / J*pi[K][1]
        X_obs_2 += (V[K][5] - J*pi[K][2])**2 / J*pi[K][2]
        X_obs_3 += (V[K][6] - J*pi[K][3])**2 / J*pi[K][3]
        X_obs_4 += (V[K][7] - J*pi[K][4])**2 / J*pi[K][4]

    P_value_1 = 1 - special.gammainc(5/2, X_obs_1/2)
    P_value_2 = 1 - special.gammainc(5/2, X_obs_2/2)
    P_value_3 = 1 - special.gammainc(5/2, X_obs_3/2)
    P_value_4 = 1 - special.gammainc(5/2, X_obs_4/2)
    print("====random_excursions_test:")
    print(f"P_value_1 = {P_value_1:2.5f}")
    print(f"P_value_2 = {P_value_2:2.5f}")
    print(f"P_value_3 = {P_value_3:2.5f}")
    print(f"P_value_4 = {P_value_4:2.5f}")

def random_excursions_variant_test(f):
    N = 5000
    bits = []
    f.seek(0)
    f.readline() # header
    for i in range(N):
        a = int(f.readline(), base=16)
        # print(f"{a:b}")
        for j in range(BIT_WIDTH):
            b = (a>>(BIT_WIDTH-1-j)) & 0x1
            bits.append(b)
    # print(bits)

    arr_bits = np.array(bits)
    arr_bits = 2*arr_bits -1
    arr_cumsum = np.cumsum(arr_bits)
    # print(arr_bits)
    print(f"bits length={len(arr_cumsum)}")
    unique, counts= np.unique(arr_cumsum, return_counts = True)
    a = dict(zip(unique, counts))
    J = a[0]
    print(f"====random_excursions_variant_test:")
    for i in range(-9, -1):
        P_value = special.erfc(abs(J-a[i])/ math.sqrt(2*J*(4*abs(i)-2)))
        print(f"P_value_{i}={P_value:2.5f}")




if __name__ == "__main__":
    """
    """
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file_num>")
        sys.exit(-1)

    millionFiles = [
        "./RandomData/random_rd_65536.clang++.csv",
        "./RandomData/random_homemakeLCG_65536.csv",
        "./RandomData/random_LCG02_65536.clang++.csv"
            ]

    files = [
            "./RandomData/random_rd.clang++.csv",
            "./RandomData/random_srand0_01.clang++.csv",
            "./RandomData/random_srand2_01.clang++.csv",
            "./RandomData/random_LCG01_01.clang++.csv",
            "./RandomData/random_LCG02_01.clang++.csv",
            "./RandomData/random_mt19937_01.clang++.csv",
            "./RandomData/random_ranlux24base_01.clang++.csv",
            "./RandomData/random_homemakeLCG_01.csv",
            "./RandomData/random_homemakeLCG_02.csv"
            ]
    tests = [
        frequency_test,
        frequency_test_block,
        run_test,
        run_test_block,
        binary_matrix_rank_test,
        spectral_test,
        non_overlapping_template_matching_test,
        overlapping_template_matching_test,
        universal_statistical_test,
        serial_test,
        approximate_entropy_test,
        Cum_sum_test,
        random_excursions_test,
        random_excursions_variant_test
        ]

    i = int(sys.argv[1])
    # print(f"file: {files[i]}")
    print(f"file: {millionFiles[i]}")
    # f = open(files[i], "r")
    f = open(millionFiles[i], "r")
    overlapping_template_matching_test(f)
    f.close()

    """
    for f in files:
        f = open(f, "r")
        tests[13](f)
        f.close()
    """

    """
    for test in tests:
        test(f)
    """

    # f.close()

    # old styple in python
    # print(f"S_abs=%2.5f"%S_abs)
    # print("P_value = %2.5f"%P_value)

    # frequency_test(f)
    # frequency_test_block(f)
    # run_test(f)
    # run_test_block(f)
    # binary_matrix_rank_test(f)
    # spectral_test(f)
    # non_overlapping_template_matching_test(f)
    # overlapping_template_matching_test(f)
    # universal_statistical_test(f)
    # serial_test(f)
    # approximate_entropy_test(f)
    # Cum_sum_test(f)
    # random_excursions_test(f)
    # random_excursions_variant_test(f)
