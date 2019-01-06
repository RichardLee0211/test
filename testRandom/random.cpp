/* this is random generator code that put 1000 pseudo random number between 0~999 to random.txt
 *
 */

#include<stdlib.h>
#include<stdio.h>

#define NUM 1000
#define RANDOM_MAX 1000
#define SEED 1

int main(){
    srand(SEED);
    for(int i=0; i<NUM; ++i){
    // for(int i=0; i<10; ++i){
        // printf("%03d, ", rand()%RANDOM_MAX);
        printf("%03d\n", rand()%RANDOM_MAX);
    }
}
