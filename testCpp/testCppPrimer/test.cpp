#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<set>

using namespace std;


template<unsigned N, unsigned M>
int compare(const char (&p1)[N], const char (&p2)[M]){
    std::cout<<N<<" "<<M<<std::endl;
    return strcmp(p1, p2);
}

int main(){
    compare("waht", "name");
}
