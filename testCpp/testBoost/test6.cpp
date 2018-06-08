// how to differ ctor and operator() in the same class ?:
// just ctor is used when construct a class, operator can be used multiple times

#include<iostream>

class A{
public:
    int i;
    A() { std::cout<<"A::A()\n"; }
    A(int i) : i{i} { std::cout<<"A::A(int) called\n"; }
    void operator() (){
        std::cout<<"operator() called\n";
    }
};
int main(){
    A a;
    a();
    A b(1);
    b();
}
