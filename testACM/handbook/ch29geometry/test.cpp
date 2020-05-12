#include<iostream>
#include<complex>
typedef long long C;
typedef std::complex<C> P_int;
// typedef std::complex<C> P;
typedef std::complex<double> P;
#define X real()
#define Y imag()


int main(){
    P p1{1,2};
    P p2{3, 4};
    P p3 = p1 + p2+ P{0,10};
    std::cout<<p3<<"\n";
    std::cout<<"abs: "<<abs(p3)<<"\n";
    std::cout<<"arg: "<<std::arg(p3)<<"\n";
    p3*=std::polar(1.0, 0.5);
    std::cout<<p3<<"\n";

}
