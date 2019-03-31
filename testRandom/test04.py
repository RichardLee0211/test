# import
from scipy import special
import math as math

BIT_WIDTH = 32
mySum =0

if __name__ == "__main__":
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
