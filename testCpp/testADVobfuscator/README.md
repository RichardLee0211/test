this is for the reimplement obfuscatorCall under C++98

ALWAYS_INLINE is define in inline.h
```cpp
#if defined(_MSC_VER)
#define ALWAYS_INLINE __forceinline
#else
#define ALWAYS_INLINE __attribute__((always_inline))
#endif
```

constexpr
not exactly sure why I need it, since C++11

the feature of C++11
```cpp
testADVobfuscator git:(master) ✗ clang++ test.cpp
test.cpp:3:13: warning: variadic templates are a C++11 extension [-Wc++11-extensions]
template<int...I>
            ^
test.cpp:5:5: error: unknown type name 'constexpr'
constexpr inline MetaString1(const char* str):
                    ^
test.cpp:5:15: error: expected member name or ';' after declaration specifiers
constexpr inline MetaString1(const char* str):
                            ~~~~~~~~~ ^
test.cpp:23:1: error: unknown type name 'constexpr'
constexpr inline const char* operator "" _obfuscatoed1(const char* str, size_t)
                            ^
test.cpp:23:11: error: expected unqualified-id
constexpr inline const char* operator "" _obfuscatoed1(const char* str, size_t)
                                      ^
test.cpp:31:23: error: expected ';' after expression
std::cout<<"hello"_obfuscatoed1<<std::endl;
^
;
test.cpp:31:23: error: use of undeclared identifier '_obfuscatoed1'
1 warning and 6 errors generated.
```
