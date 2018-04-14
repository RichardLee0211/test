#include<iostream>

template<int...I>
struct MetaString1{
    constexpr inline MetaString1(const char* str):
        buffer_{encrypt(str[I])...} {}

    const char* decrypt(){
        for(int i=0; i<sizeof...(I); ++i)
            buffer_[i] = decrypt(buffer_[i]);
        buffer_[sizeof...(I)] = 0;
        return buffer_;
    }

private:
    constexpr char encrypt(char c) const { return c^0x55; }
    constexpr char decrypt(char c) const { return encrypt(c); }

private:
    char buffer_[sizeof...(I)+1];
};

#if 0
constexpr inline const char* operator "" _obfuscatoed1(const char* str, size_t)
{
    return MetaString1<0, 1, 2, 3, 4, 5>(str).decrypt();
}
#endif

#define  OBFUSCATED(str) (MetaString1<0,1,2,3,4,5>(str).decrypt())

int main(){
    // std::cout<<"what"_obfuscatoed1<<std::endl;
    std::cout<<OBFUSCATED("hello")<<std::endl;
}
