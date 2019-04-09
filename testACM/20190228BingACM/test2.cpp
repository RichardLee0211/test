#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include<iostream>
#include<string>
#include<assert.h>

/* Enter your code here. Read input from STDIN. Print output to STDOUT */
int main() {
    int N;
    std::string str;
    int num{3}, tmp, tmp1, tmp2, common;
    std::cin >>N;
    std::cin >> tmp >> tmp1 >> tmp2;
    if(tmp != tmp1 && tmp != tmp2){
        printf("1");
    }else if(tmp1 != tmp && tmp1 != tmp2){
        printf("2");
    }else if(tmp2 != tmp && tmp2 != tmp1){
        printf("3");
    }else if(tmp == tmp1 && tmp1== tmp2){
        common = tmp;
        while(std::cin >> tmp){
            num++;
            if(tmp != common){
                std::cout << num;
                return 0;
            }
        }
    }else{
        assert(0);
    }
    // std::cout << str;

    return 0;
}
