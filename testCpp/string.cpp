#include<iostream>
#include<string>
#include<stdio.h>
#include<string.h>

int main(){
    const char* src = "hello";
    printf("%d\n", strlen(src)); // 5
    printf("%d\n", sizeof(src)); // 8
}
