#include<iostream>

typedef unsigned int uint;
int main(){
    uint A[] {1,2,3,4,5};
    uint sum{0};
    for(auto i: A)
        sum += i;
    uint S = sum/2;
    uint M[sizeof(A)/sizeof(A[0])];
    if(A[0]<S)
        M[0] = A[0];
    else
        M[0] = 0;
    for(int i{1}; i<(int)(sizeof(A)/sizeof(A[0])); ++i){
        M[i] =M[i-1];
        for(int j{0}; j<i; ++j){
            if(M[j]+A[i]>M[i] && M[j]+A[i]<=S)
                M[i]=M[j]+A[i];
        }
    }

    for(auto i:M)
        printf("%d\t", i);
    printf("\n");
}
