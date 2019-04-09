#include<iostream>

// return the number of sets that add to total
// arr[i] could be add to sets of not, it's like recursive tree,
// left subtree add arr[i] to sets, right subtree don't
int rec(int *arr, int total, int i){
    if (total == 0)
        return 1; // find a set that add to total
    if (total < 0)
        return 0; // overflow set
    if (i < 0)
        return 0;
    if (total < arr[i])
        return rec(arr, total, i-1); // way too big total
    // main part of this func
    return rec(arr, total-arr[i], i-1) +
            rec(arr, total, i-1);
}

// return the number of sets that add to total
// arr is sorted
int count_sets(int *arr, int total, int size){
    return rec(arr, total, size);
}

int main(){
    // int* arr = new int{2, 3, 4, 10};
    int arr[] = {2, 3, 4, 5, 6, 10, 20, 30, 31};
    int total = 10;
    std::cout<<count_sets(arr, total, sizeof(arr)/sizeof(int) -1)<<"\n";
}
