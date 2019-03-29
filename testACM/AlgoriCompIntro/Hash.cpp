// this is implement of multiplication method of hash function descript in chapter 11.3.2
//
// #include<bits/stdc++.h>
// printf("sizeof int: %lu", sizeof(int)); // 4 bytes, 32 bits
// printf("sizeof long : %lu", sizeof(long)); // 8, 64 bits
// printf("sizeof int: %lu", sizeof(long long)); // 16, 64 bits
//
#include<iostream>
typedef unsigned int uint;

// k=123456, p=14, m=2^14=16384, w=32
int mulHash(long key){
    long s{2654435769};
    // printf("%ld\n", (long)key*s); // 327706022297664
    // printf("%d\n", (int32_t)(key*s)); // 17612864
    // printf("%08X\n", (int32_t)(key*s)); // 01 0C C0 40
    // printf("%08X\n", (int32_t)(key*s)>>18); // 00 00 00 43
    return (int32_t)(key*s)>>18;
}

int main(){
    long k{123456};
    // printf("%ld", mulHash(k));
    std::cout<<mulHash(k)<<"\n";
    std::cout<<mulHash(3)<<"\n";
    std::cout<<mulHash(4)<<"\n";
    std::cout<<mulHash(43)<<"\n";
    std::cout<<mulHash(1239203)<<"\n";
    std::cout<<mulHash(3)<<"\n";

}
