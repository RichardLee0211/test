#include<iostream>
#include<vector>

using namespace std;

// class

#if 0
int main(){
    int testCaseNu=0;
    while(--testCaseNu != 0){
    }
}

#endif

#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    int n, r;
    std::cin >> n;
    std::cin >> r;

    std::vector<bool> v(n);
    std::fill(v.end() - r, v.end(), true);

    do {
        for (int i = 0; i < n; ++i) {
            std::cout << v[i] << " ";
        }
        std::cout << "\n";
    } while (std::next_permutation(v.begin(), v.end()));
    return 0;
}
