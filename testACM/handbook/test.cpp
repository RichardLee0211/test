#include<iostream>
#include<algorithm>
#include<map>
#include<set>

typedef unsigned int uint;
/* algorithm: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes */
void getPrimes(uint n){
    bool barray[n+1]; // default initial to 0
    for(uint i=0; i<n+1; ++i){
        barray[i] =true;
    }
    barray[0] = false; barray[1] = false;
    for(uint i{2}; i<n+1;){
        barray[i] = true;
        for(uint j{2*i}; j<n+1; j+=i){
            barray[j] = false;
        }
        while(++i<n+1 && barray[i] == false)
            ;
    }
    /* print out */
    for(uint j{0}; j<n+1; ++j){
        if(barray[j] == true)
            printf(" %04u", j);
        if(j%200 == 0) printf("\n");
    }
}

int main(){
#if 0
    {
        // test of std::sort std::reverse, and std::random_shuffle
        std::map<int, int> imap{{1,1}, {2,2}, {3,3},{4,4}};
        int array[]{1,2,23,4,5};
        std::sort(array, array+6);
        std::reverse(array, array+5);
        std::random_shuffle(array, array+5);
        /*
        for(auto i: imap){
            std::cout<<i.first<<"\t";
            std::cout<<"what\n";
        }
        for(auto i: array){
            std::cout<<i<<"\t";
        }
        */

        std::set<int> iset{1,2,3,4,5,6,7,8,9,0};
        std::cout<<*iset.lower_bound(-13);
    {
#endif
        {
            getPrimes((uint)10000);
        }
}
