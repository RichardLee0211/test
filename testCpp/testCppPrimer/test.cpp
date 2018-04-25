#include<iostream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

void foo(string str) {
    cout<<str<<endl;
}

template<typename T>
int print(const vector<T> &that){
    for(auto i=that.cbegin(); i<that.cend(); ++i)
        std::cout<< *i <<" ";
    std::cout<<std::endl;
    return 0;
}

int main(){
    vector<int> v1{1,2,3,4,5};
    vector<int> v2 = v1;
    print(v1);
    print(v2);

    // fill(v1.begin(), v1.begin()+3, 0);
    fill_n(v1.begin(), 4, 10);
    print(v1);
    print(v2);
}
