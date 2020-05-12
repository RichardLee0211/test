#include<iostream>

typedef unsigned int uint;
typedef struct Item_t{
    uint size;
    uint value;
} Item;

int main(){
    Item items[] {{1,1}, {2,2}, {3,3}, {4,4}, {5,5}, {6,6}};
    uint capacity{20};

    uint M[capacity+1];

    M[0] = 0;
    for(uint i=1; i<capacity+1; ++i){
        uint max = M[i-1];
        for(uint j{0}; j<sizeof(items)/sizeof(items[0]); ++j){
            // if(i-items[j].size>=0 && M[i-items[j].size]+items[j].value > max)
            // uint - uint produces uint
            if((int)(i-items[j].size)>=0 && M[i-items[j].size]+items[j].value > max)
                max = M[i-items[j].size]+items[j].value;
        }
        M[i] = max;
    }

    for(auto i :M)
        printf("%u\t", i);
    printf("\n");

}
