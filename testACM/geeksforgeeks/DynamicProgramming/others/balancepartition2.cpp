#include<iostream>
#include<vector>

#define DEBUG 1
typedef unsigned int uint;
typedef struct M_t{
    uint sum;
    std::vector<int> index;
#if DEBUG
    void print(void){
        printf("%u\t", this->sum);
        for(auto i: this->index)
            // printf("%u\t", A[i]);
        printf("\n");
    }
#endif
} M;
int main(){
    // uint A[] {1,2,3,4,5,6};
    uint A[] {
14,
89,
18,
105,
23,
4,
35,
99,
67,
76,
198,
20,
5,
38,
55,
201 };

    uint sum{0};
    for(auto i: A)
        sum += i;
    uint S = sum/2; printf("%d\n", S);
    M m;
    m.sum = 0;
    if(A[0]<S){
        m.sum = A[0]; m.index.push_back(0);
    }
    else
        m.sum = 0;
    // assume N is even
    uint N = sizeof(A)/sizeof(A[0]);
    for(int i{1}; i<(int)(N); ++i){
        if(m.index.size()< N/2 && m.sum+A[i] <S){
            m.sum += A[i];
            m.index.push_back(i);
        }
        else if(m.index.size()==N/2 && m.sum<S ){
            // for(auto j : m.index){
            for(int k{0}; k<(int)m.index.size(); ++k){
                int j = m.index[k];
                if(A[j]<A[i] && m.sum-A[j]+A[i]<S){
                    m.sum += (A[i]-A[j]);
                    m.index[k] = i;
                    break;
                }
            }
        }
#if DEBUG
        printf("%u\t", m.sum);
        for(auto i: m.index)
            printf("%u\t", A[i]);
        printf("\n");
#endif
    }
}
