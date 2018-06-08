#include<string>
#include<iostream>
#include<initializer_list>

using namespace std;

constexpr bool check(std::initializer_list<std::size_t> il){
    for(auto d: il){
        if(d<=0)
            return false;
    }
    return true;
}

template<std::size_t ... Ds>
struct Dims{
    static_assert(check({Ds...}));
};

int main(){
    Dims<1, 2> d;
    // Dims<1, 2, 0> d2;
}
