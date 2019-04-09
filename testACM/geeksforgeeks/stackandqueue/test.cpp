#include<stack>
#include<iostream>

int main(){
    std::stack<int> stk;
    // std::cout<<stk.top(); // !! error give segment fault
    int i = stk.top(); // !! error, why not through a exception or something else instead of error
    std::cout<<i;
}
// empty line 
