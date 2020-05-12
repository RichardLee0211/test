/*
 * from https://practice.geeksforgeeks.org/problems/next-larger-element/0
 */

#include<iostream>
#include<stack>

void func(int* iArray, int arrayLength){
    std::stack<int> stk;
    std::stack<int> index;
    int ret[arrayLength];
    for(int i=0; i<arrayLength; ++i){
        int tmp = iArray[i];
        if(stk.empty() == true || stk.top() >= tmp){
            stk.push(tmp);
            index.push(i);
            continue;
        }
        while(stk.empty() == false && stk.top() < tmp){
            ret[index.top()]  = tmp;
            stk.pop();
            index.pop();
        }
        stk.push(tmp);
        index.push(i);
    }
    for(int i=0; i<arrayLength; ++i){
        if(ret[i] == 0) ret[i] = -1;
        std::cout<<ret[i]<<" ";
    }
    std::cout<<"\n";

}

int main(){
    int testCaseNum{0};
    std::cin>>testCaseNum;
    while(--testCaseNum >= 0){
        int arrayLength{0};
        std::cin>>arrayLength;
        int iArray[arrayLength];
        for(int i=0; i<arrayLength; ++i){
            std::cin>>iArray[i];
        }
        func(iArray, arrayLength);
    }
}
