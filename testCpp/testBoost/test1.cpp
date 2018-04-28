#include<iostream>

template<unsigned long N>
struct binary{
    static unsigned const value =
        binary<N/10>::value << 1 // prepend higher bits
        | N%10; // to lowest bit
};

template<>
struct binary< 0 >
{
    static unsigned const value = 0;
};

int main(){
    unsigned const one = binary<1>::value;
    unsigned const three = binary<11>::value;
    unsigned const five = binary<101>::value;
    unsigned const seven = binary<111>::value;
    unsigned const nine = binary<1001>::value;
    std::cout<<one<<" "<<three<<" "<<
        five<<" "<<seven<<" "<<nine<<std::endl;
}
