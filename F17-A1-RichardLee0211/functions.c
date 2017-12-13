#include "functions.h"

/**
 *
 * this is a function about Fibonacci
 * for 64 bit machine, int could be 10^19, and Fib[100] could be 10^20, so I
 * would like to create a Fib[100] to score all results of Fibonacci
 *
 * if n is Fib, return number
 * else return -1
 */
int isFib(unsigned long n) {
    int Fib[100] = {0, 1, 1, 0};

    Fib[0] = 0;
    Fib[1] = Fib[2] = 1;

    int i;
    for(i=3; i<=100; i++){
        Fib[i] = Fib[i-1] + Fib[i-2];
    }
    for(i=0; Fib[i]<=n; i++);
    if(Fib[i-1] == n)
        return i-1;
    else
        return -1;
}

/**
 * this is functions of count_vowels
 */

/**
 * oneBit10[]
 * zOrE 2
 * OnE 2
 * twO 1
 * thrEE 2
 * fOUr 2
 * fIvE 2
 * sIx 1
 * sEvEn 2
 * EIght 2
 * nInE 2
 */
unsigned int under9(unsigned long num){
    if(num > 9)
        return -1;
    int oneBit10[10] = {2, 2, 1, 2, 2, 2, 1, 2, 2, 2 };
    return oneBit10[num];
}

/**
 *
 * twoBit10_1[]
 * 10 tEn 1
 * 11 ElEvEn 3
 * 12 twElvE 2
 * 13 thIrtEEn 3
 * 14 fOUrtEEn 4
 * 15 fIftEEn 3
 * 16 sIxtEEn 3
 * 17 sEvEntEEn 4
 * 18 EightEEn 3
 * 19 nInEtEEn 3
 */
unsigned int under19(unsigned long num){
    if(num >19)
        return -1;
    if(num <= 9)
        return under9(num);

    int twoBit10_1[10] = {1, 3, 2, 3, 4, 3, 3, 4, 3, 3};
    return twoBit10_1[num%10];
}

/**
 *
 * 2X twEnty 1+oneBit10[X]
 * 3X thIrty 1+oneBit10[X]
 * 4X fOrty 1+oneBit10[X]
 * 5X fIfty 1+oneBit10[X]
 * 6X sIxty 1+oneBit10[X]
 * 7X sEvEnty 2+oneBit10[X]
 * 8X EIghty 2+oneBit10[X]
 * 9X nInEty 2+oneBit10[X]
 */
unsigned int under99(unsigned long num){
    if(num>99)
        return -1;
    if(num<=9)
        return under9(num);
    if(num<=19)
        return under19(num);

    /* when num is between 20 and 99 */
    int secBit = num/10;
    int firstBit = num%10;
    int twoBit10_2[10] = {-1, -1, 1, 1, 1, 1, 1, 2, 2, 2};
    if(firstBit == 0)
        return twoBit10_2[secBit];
    else
        return twoBit10_2[secBit] + under9(firstBit);
}

/**
 *
 * 1XX OnE hUndrEd 2+2+under99(XX)
 * 2XX twO hUndrEd 1+2+under99(XX)
 * 3XX thrEE hUndrEd 2+2+under99(XX)
 * 4XX oneBit10[4] +2+under99(XX)
 * 5XX oneBit10[5] +2+under99(XX)
 * 6XX oneBit10[6] +2+under99(XX)
 * 7XX oneBit10[7] +2+under99(XX)
 * 8XX oneBit10[8] +2+under99(XX)
 * 9XX oneBit10[9] +2+under99(XX)
 */
unsigned int under999(unsigned long num){
    if(num>999)
        return -1;
    if(num<=9)
        return under9(num);
    if(num<=19)
        return under19(num);
    if(num<=99)
        return under99(num);

    /* when num is bewteen 100 and 999 */
    int thirdBit = num/100;
    int secBit = num%100 /10;
    int firstBit = num%10;
    if(secBit == 0 && firstBit == 0)
        return under9(thirdBit) + 2;
    else
        return under9(thirdBit) + 2 +under99(num%100);
}

/**
 *
 * 1XXX OnE thOUsAnd under9(1) +3 +under999(XXX)
 * 2XXX twO thOUsAnd under9(2) +3 +under999(XXX)
 * ...
 * CCC XXX under999(CCC) +3 +under999(XXX)
 */
unsigned int under999999(unsigned long num){
    if(num>999999)
        return -1;
    if(num<=9)
        return under9(num);
    if(num<=19)
        return under19(num);
    if(num<=99)
        return under99(num);
    if(num<=999)
        return under999(num);

    /*  when num is between 1000 and 999999 */
    int top3bit = num/1000;
    if(num%1000 == 0)
        return under999(top3bit) +3;
    else
        return under999(top3bit) +3 +under999(num%1000);
}

/**
 * VVV XXXXXX VVV mIllIOn under999(VVV) +3 +under999999(XXXXXX)
 */
unsigned int under999999999(unsigned long num){
    if(num>999999999)
        return -1;
    if(num<=9)
        return under9(num);
    if(num<=19)
        return under19(num);
    if(num<=99)
        return under99(num);
    if(num<=999)
        return under999(num);
    if(num<=999999)
        return under999999(num);

    /* when num is between 1,000,000 and 999,999,999 */
    int top3bit = num/1000000;
    if(num%1000000 == 0)
        return under999(top3bit) +3;
    else
        return under999(top3bit) +3 +under999999(num%1000000);
}

unsigned int count_vowels(unsigned long num) {
    if(num>1000000000)
        return -1;
    if(num<=9)
        return under9(num);
    if(num<=19)
        return under19(num);
    if(num<=99)
        return under99(num);
    if(num<=999)
        return under999(num);
    if(num<=999999)
        return under999999(num);
    /*  when num is 1,000,000,000 */
    if(num == 1000000000)
        return under9(1) +3;
    else
        return -1;
}

unsigned int count_ones(long num) {
    int count=0;
    int i=64;/*32或64位比特位*/
    while(i--)
    {
        if((num&1) == 1)count++;
        num=num>>1;
        /*>>右移运算符；右移时负数补1、正数补0，num>>1指右移1位*/
    }
    return count;
}

unsigned long swap_bytes(unsigned long someInt) {
    unsigned long byte1 = someInt & 0x00000000000000FF;
    unsigned long byte2 = someInt & 0x000000000000FF00;
    unsigned long byte3 = someInt & 0x0000000000FF0000;
    unsigned long byte4 = someInt & 0x00000000FF000000;
    unsigned long byte5 = someInt & 0x000000FF00000000;
    unsigned long byte6 = someInt & 0x0000FF0000000000;
    unsigned long byte7 = someInt & 0x00FF000000000000;
    unsigned long byte8 = someInt & 0xFF00000000000000;
    /**
     * TODO: report integer literal is too large to be represented in any integer type
     * when use 0xFF00000000000000U or 0x1F00000000000000U
     * maybe first 4 bits has special meaning for unsigned 64 bit Int Literal
     * had been stuck for 2 hours
     */
    unsigned long newInt = (byte1 << 8) | (byte2 >> 8) |
        (byte3 << 8) | (byte4 >> 8) |
        (byte5 << 8) | (byte6 >> 8) |
        (byte7 << 8) | (byte8 >> 8);
    return newInt;
}

/**
 * do not include math.h ??
 * what does you mean by math library
 *
 * cause -100<a<100 -100<b<100
 * so maximum of result would be 100^4 - 0 = 10^8
 * and long int could be 10e9
 * so do worry about bandrary
 */
long a4_minus_b4(int a, int b) {
    /* return a*a*a*a - b*b*b*b; */
    return (a*a+b*b)*(a*a-b*b);

}
