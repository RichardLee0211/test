/*
 * from https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
 *
 */
/**
 * relatively easy, create a array of the same size and using as a mark to
 * achive the O(n) time-comlexity
 */
#include<iostream>

int main(){
    int testCaseNum{0};
    std::cin>>testCaseNum;
    while(--testCaseNum >= 0){
        // algorithm goes here
        int arrayLength{0};
        std::cin>>arrayLength;
        int array[arrayLength-1]; // array contains arrayLength-1 elements
        bool barray[arrayLength+1]; // barray[i] indecates that i exists
        for(int i=0; i<arrayLength-1; ++i){
            std::cin>>array[i];
            barray[array[i]] = true;
        }
        for(int i=1; i<arrayLength+1; ++i){ // barray[0] doesn't count
            if(barray[i] == false){
                std::cout<<i<<"\n";
                break;
            }
        }

    }
}

void printArray(bool* p, int n){
    for(int i=0; i<n; ++i)
        std::cout<<p[i]<<" ";
    std::cout<<"\n";
}
