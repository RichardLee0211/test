#include<initializer_list>

constexpr bool is_prime(int n){
    for(int i=2; i<n; ++i){
        if(n%i==0)
            return false;
    }
    return true;
}

int main(){
    static_assert(is_prime(3), "Prime test failed.");
    static_assert(is_prime(5), "Prime test failed.");
    static_assert(is_prime(7), "Prime test failed.");
    // static_assert(is_prime(91), "Prime test failed.");
    // static_assert(is_prime(95), "Prime test failed.");

}
