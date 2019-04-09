// subarray sum, page.77
#include<iostream>
#include<map>
#include<unordered_map>
#include<queue>

// using namespace std;




/*
// array of m length, need to find a n elements in array that sum to S
std::queue<int> nSum(int array[], int m, int n, int S){
    std::unordered_map<int, int> imap;
    for(int i{0}; i<m; ++i)
        imap.insert({array[i], i});
}
*/

// std::queue<int>
void
get3Sum(int array[], int m, int S, int n=3){
    std::unordered_map<int, int> imap;
    for(int i{0}; i<m; ++i)
        imap.insert({array[i], i});
    for(int i{0}; i<m; ++i){
        for(int j{i+1}; j<m; ++j){
            if(imap.find(S-array[i]-array[j]) != imap.end()){
                // return {i, j, imap.find(S-array[i]-array[j])->second};
                std::cout<<i<<j<<imap.find(S-array[i]-array[j])->second<<" ";
                // break;
            }
        }
    }
}
std::pair<int, int> subarraySum(int array[], int n, int S){
    int i{0}, j{0}, sum{0};
    if(sum+array[i] == S) return {j, i+1};
    else if(sum+array[i] > S){
        ++j;
    }
    else if(sum+array[i] < S)
        sum += array[i];

    while(++i<n){
        if(sum+array[i] == S) return {j, i+1};
        else if(sum+array[i] < S){
            sum += array[i];
            continue;
        }
        else if(sum+array[i] > S){
            while(j<i){
                if(sum+array[i]-array[j] == S)
                    return {j+1, i+1};
                else if(sum+array[i]-array[j]<S){
                    sum += (array[i] - array[j]);
                    j++;
                    break;
                }
                else if(sum+array[i]-array[j]>S){
                    sum -= array[j];
                    j++;
                    continue;
                }
            }
        }
    }

    return {-1, -1};

}

int main(){
#if 0
    /* test of subarraySum */
    int S{20};
    int array[][7]{
        {1,2,3,4,5,5, 0},
        {21,2,3,4,5,5,1},
        {0,2,3,4,5,5, 0},
        {1,2,3,4,5,5, 4}
    };
    // int j, i;
    std::cout<<subarraySum(array[3], 7, S).first;
    std::cout<<subarraySum(array[3], 7, S).second;
#endif
    int S{20};
    int array[][7]{
        {1,2,3,4,5,5, 0},
        {21,2,3,4,5,5,1},
        {0,2,3,4,5,5, 0},
        {1,2,3,4,5,5, 4}
    };
    get3Sum(array[0], 7, 11);
}
