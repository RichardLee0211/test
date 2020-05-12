#include<iostream>
#include<vector>
#include<math.h>

/**
 *               0 // heading space 13
 *       1               2 // heading space 6, interval space 15
 *   3       4       5       6 // heading space 2, interval space 7
 * 7   8   9   10  11  12  13  14 // heading space 0, interval space 3
 *
 * 111   222   333   444   555   666   777   888   999   000   111   222   333
 * 0
 * | \
 * 1  2
 * | \ | \
 * 3  45  6
 * elements Size :s
 * height : math.floor(log(s))+1
 * elements take up to 3 spaces
 */
template<class T>
void printoutHeap(const std::vector<T> &v){
    for(int i=0; i<v.size(); ++i){
        // TODO:
    }
}

int main(){
    std::vector<int> v {1, 2, 3, 4, 5, 3, 7};
    std::make_heap(v.begin(), v.end());
    for(auto e: v){
        std::cout<<e<<" ";
    }
}
