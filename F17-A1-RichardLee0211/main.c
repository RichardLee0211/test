/*  main.c */
#include<stdio.h>
#include "functions.h"

int count_vowelsMain(){
    int num;
    printf("this is mainTest of count_vowels() \n");
    printf("input -1 to exit\n");
    while(1){
        printf("input your number: ");
        scanf("%d", &num);
        if(num == -1) return -1;
        printf("%d result is %d \n", num, count_vowels(num));

    }

    return 0;
}

int isFibMain(){
    int n;
    printf("\nthis is mainTest of isFib() \n");
    printf("input -1 to exit\n");
    while(1){
        printf("please input your number: ");
        scanf("%d", &n);
        if(n == -1) return -1;
        printf("\n result is ");
        printf("%d \n", isFib(n));
    }

    return 0;
}

int count_onesMain()
{
    long num;
    printf("\nthis is mainTest of count_ones() \n");
    printf("input -1 to exit\n");
    while(1){
        printf("please input your number: ");
        scanf("%ld",&num);
        if(num == -1) return -1;
        printf("count=%d \n", count_ones(num));

    }
    return 0;
}


int swap_bytesMain(){
    unsigned long someInt;
    while(1){
        printf("\nthis is testMain of swap_bytes()");
        printf("\ninput 0 to exit.");
        printf("\nplease input your number: ");
        scanf("%lx", &someInt);
        if(someInt == 0) return -1;
        printf("result is: %#lx", swap_bytes(someInt));
    }


    return 0;
}

int a4_minus_b4Main(){
    int a, b;
    printf("\nthis is testMain of a4_minus_b4()");
    printf("\n input a:");
    scanf("%d", &a);
    printf("\n input b:");
    scanf("%d", &b);
    printf("result of a^4-b^4: ");
    printf("%ld \n ", a4_minus_b4(a, b));

    return 0;
}
int main(int argc, char **argv) {
    isFibMain();
    count_vowelsMain();
    count_onesMain();
    swap_bytesMain();
    a4_minus_b4Main();


  return 0;
}
