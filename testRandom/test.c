/* try to implement a LCG */
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

int main(int argc, char** argv){
    if(argc != 6){
        printf("usage: ./%s a c m seed iter_count\n", argv[0]);
        return -1;
    }

    uint64_t a = atol(argv[1]);
    uint64_t c = atol(argv[2]);
    uint64_t m = atol(argv[3]);
    uint64_t seed = atol(argv[4]);
    uint64_t iter_count= atol(argv[5]);
    uint64_t x_1, x_2;

    x_1 = (a*seed + c) % m;
    printf("%0llX\n", x_1);

    for(uint64_t i=0; i<iter_count; ++i){
        x_2 = (a*x_1 + c) % m;
        printf("%0llX\n", x_2);
        x_1 = x_2;
    }
}
