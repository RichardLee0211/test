template<unsigned n>
struct facotrial
{
    static const unsigned value = n * facotrial<n-1>::value;
};

template<>
struct facotrial<0>
{
    static const unsigned value = 1;
};

#include<iostream>

int main(){
    facotrial<4> fa;
    std::cout<< fa.value <<std::endl;
}
