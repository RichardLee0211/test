/*
 */

#include<stdlib.h>
#include<stdio.h>

// #define NUM 5000
// #define RANDOM_MAX 1000
#define NUM 65536
#define SEED 0

int main_1(){
    srand(SEED);
    for(int i=0; i<NUM; ++i){
        printf("%08X\n", rand());
    }
    return 0;
}

#include<random>

#define uint unsigned int

int main_2(){
    std::random_device rd;
    std::uniform_int_distribution<uint32_t> dist(0);
    for(int i=0; i<NUM; ++i){
        printf("%08X\n", dist(rd));
    }
    return 0;
}

int main_3(){
    // https://en.cppreference.com/w/cpp/numeric/random/linear_congruential_engine
    // std::linear_congruential_engine<uint32_t, 16807, 0, 2147483647> gen;
    std::linear_congruential_engine<uint32_t, 48271, 0, 2147483647> gen;
    std::uniform_int_distribution<uint32_t> dist(0);
    for(int i=0; i<NUM; ++i){
        printf("%08X\n", dist(gen));
    }
    return 0;
}

int main_4(){
    // std::mt19937 eng{};
    std::ranlux24_base eng{};
    std::uniform_int_distribution<uint32_t> dist(0);
    for(int i=0; i<NUM; ++i){
        printf("%08X\n", dist(eng));
    }
    return 0;

}

int main(){
    main_3();
}
