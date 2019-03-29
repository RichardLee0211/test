something about constexpr
```cpp
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
```
```cpp
#include<string>
#include<iostream>
#include<initializer_list>
    using namespace std;

    constexpr bool check(std::initializer_list<std::size_t> il){
        for(auto d: il){
            if(d<=0)
                return false;
        }
        return true;
    }

    template<std::size_t ... Ds>
    struct Dims{
        static_assert(check({Ds...}));
    };

    int main(){
        Dims<1, 2> d;
        // Dims<1, 2, 0> d2;
    }
```

something about % a negetive
```cpp
    int main(){
        int num = -1;
        cout<<num%10<<endl; // output -1
        return 0;
    }
```
## note about vim short cut
<leader>il " identifier list
<leader>fl " file list


start to find out I don't realy nerdtree and file list in vim or the tags list
I'm getting enough familar with C++ programing and these plugin doesn't speed me up

but I will need
- syntax highlight
- static check
- and autocomplete to help me fast coding
