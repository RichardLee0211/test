/**
 * from https://www.hackerrank.com/contests/bing-acm-sep-2017/challenges/coding-and-decodin
 */
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<complex>
#include<string>

using namespace std;

int swap(int& a, int& b){
    int tmp;
    tmp =a;
    a = b;
    b = tmp;
    return 0;
}

int main(){
    int count;
    scanf("%d", &count);

    for(int h=0; h<count; h++){
        int array[4][4] = {0};
        string tmp;
        cin>>tmp;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(tmp[i*4+j] == '1') array[i][j] = 1;
                else array[i][j] = 0;
            }
        }

        int newArray[4][4];
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                newArray[j][3-i] = array[i][j];
            }
        }

        int first =
            'a' -1 +
            newArray[0][0]*pow(2, 4)+
            newArray[0][1]*pow(2, 3)+
            newArray[0][2]*pow(2, 2)+
            newArray[0][3]*pow(2, 1)+
            newArray[1][0]*pow(2, 0);
        int second=
            'a' -1 +
            newArray[1][1]*pow(2, 4)+
            newArray[1][2]*pow(2, 3)+
            newArray[1][3]*pow(2, 2)+
            newArray[2][0]*pow(2, 1)+
            newArray[2][1]*pow(2, 0);
        int third=
            'a' -1 +
            newArray[2][2]*pow(2, 4)+
            newArray[2][3]*pow(2, 3)+
            newArray[3][0]*pow(2, 2)+
            newArray[3][1]*pow(2, 1)+
            newArray[3][2]*pow(2, 0);
        printf("%c%c%c\n", (char)first, (char)second, (char)third);

    }



    return 0;
}
