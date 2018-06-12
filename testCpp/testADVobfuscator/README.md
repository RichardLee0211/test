# this is note of ADVobfucator
this is for the reimplement obfuscatorCall under C++98

## ALWAYS_INLINE is define in inline.h
```cpp
    #if defined(_MSC_VER)
    #define ALWAYS_INLINE __forceinline
    #else
    #define ALWAYS_INLINE __attribute__((always_inline))
    #endif
```

## constexpr
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

example/DetectDebugger
when debugger with mac, string disappear
```cpp
    OBFUSCATED_CALL_P0(DetectDebugger, ImportantFunctionInTheApplication);
```

example/ObfuscatedCalls
no surprise, but what this do to the original code??
```cpp
    OBFUSCATED_CALL0(FunctionToProtect);
    auto result = OBFUSCATED_CALL_RET(int, FunctionToProtectWithParameters, OBFUSCATED("did"), OBFUSCATED("again"));
```

example/ObfuscatedStrings
what does this code do ??

TODO: ??using objdump -disassemble <objectname>

context-free grammar: In formal language theory, a context-free grammar is a
certain type of formal grammar: a set of production rules that describe all
possible strings in a given formal language. Production rules are simple replacements.

in the macro, use code in MetaFSM.h

# learning Finite State Machine for ObfuscatedCalls
from https://www.boost.org/doc/libs/1_67_0/libs/msm/doc/HTML/pr01.html
where can I get the pdf of this document

document like this make me unable to make notes
concept: state machine, state, transition, event
from https://www.boost.org/doc/libs/1_67_0/libs/msm/doc/HTML/ch02s02.html

I like this kind of tutorial, boost_MSM_tutorial.pdf, it's in the original document

seem have many function called in MetaFSM.h
#define OBFUSCATED_CALL0(f) \
                andrivet::ADVobfuscator::ObfuscatedCall \
                <andrivet::ADVobfuscator::Machine1::Machine> \
                (MakeObfuscatedAddress(f, \
                andrivet::ADVobfuscator::MetaRandom<__COUNTER__, 400>::value + 278))

still have problem reading this part:
from MetaFSM.h
```cpp
    // When function F is not returning a value
    // FSM: Finite State Machine
    // F: Function (target)
    // Args: Arguments of target
    template<template<typename, typename = Void> class FSM, typename F, typename... Args>
    inline void ObfuscatedCall(F f, Args&&... args)
    {
        using E = event<Void, F, Args&...>;
        using M = msm::back::state_machine<FSM<E, Void>>;
        using Run = typename FSM<E, Void>::template Run<F, Args...>;

        M machine;
        Run::run(machine, f, std::forward<Args>(args)...);
    }
```

cann't use open in tmux, explained here:
https://apple.stackexchange.com/questions/243067/terminal-app-and-tmux-session-cant-use-open-command-without-tmux-it-works
```bash
    The window server could not be contacted. open must be run with a user logged in at the console, either as that user or as root.

    brew update
    brew install reattach-to-user-namespace
    brew upgrade reattach-to-user-namespace
    echo "set -g default-command \"reattach-to-user-namespace -l ${SHELL}\"" >> ~/.tmux.conf
```
and solved here:
http://www.elmund.io/2015/07/10/open-command-in-osx-tmux/

in the project, boost provide it's tutorial at .../boost_1_66_0/libs/msm/doc/PDF/examples

online tutorial here: http://redboltz.wikidot.com/boost-msm-guide

# learning from ADVobfuscator docs

## the 1st implement of obfuscator string
```cpp
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

        const char* getBuffer(){
            return this->buffer_;
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
#define  OBFUSCATED1(str) (MetaString1<0,1,2,3,4,5>(str).getBuffer())

    int main(){
        // std::cout<<"what"_obfuscatoed1<<std::endl;
        std::cout<<OBFUSCATED1("hello")<<std::endl;
    }
```
make use of template to make array memory in the struct, otherwise using Heap memory new
!! and this code make every part possible to complete in compile time

## the 2nd implement

PageNo.23, MetaString2<Make_Indexs<sizeof(str)-1>::type> (str), how to implement MetaString2 ?: in DocCode, compile time recursion generator, look like crazy code
about check if something is at compile time, here: https://stackoverflow.com/questions/28988426/how-to-test-if-constexpr-is-evaluated-correctly
```cpp
    // uncomment to disable assert()
    // #define NDEBUG
    #include<cassert>
    constexpr inline size_t StringLengthCExpr(const char * const str) noexcept
    {
        return (*str == 0) ? 0: StringLengthCExpr(str+1) +1;
    }

    std::size_t StringLength(const char * str)
    {
        return (*str==0) ? 0 : StringLength(++str) + 1;
    }
    class StringID{
    public:
        constexpr inline StringID(const char * key)
            : hashID(StringLengthCExpr(key))
        {

        }
    private:
        const unsigned int hashID;
    };

    int main(){
        static_assert(StringLengthCExpr("hack")==4, "length of hack should be 4!");
        assert(StringLength("hack")==6);
        // StringID id("hello world");
    }
```
generating integer sequences at compile time, here: https://blog.galowicz.de/2016/06/24/integer_sequences_at_compile_time/
wired but easiest way to print parameter packs
```cpp
    template<typename... Ts> void func(Ts... args){
        const int size = sizeof...(args) + 2;
        int res[size] = {1,args...,2};
        // since initializer lists guarantee sequencing, this can be used to
        // call a function on each element of a pack, in order:
        int dummy[sizeof...(Ts)] = { (std::cout << args, 0)... };
    }
```
from http://en.cppreference.com/w/cpp/language/parameter_pack,
this could be the key to implement Interpolate
```cpp
#include <iostream>
    void tprintf(const char* format) // base function
    {
        std::cout << format;
    }

    template<typename T, typename... Targs>
    void tprintf(const char* format, T value, Targs... Fargs) // recursive variadic function
    {
        for ( ; *format != '\0'; format++ ) {
            if ( *format == '%' ) {
                std::cout << value;
                tprintf(format+1, Fargs...); // recursive call
                return;
            }
            std::cout << *format;
        }
    }

    int main()
    {
        tprintf("% world% %\n","Hello",'!',123);
        return 0;
    }
```

## 3rd implement
using <random> and template to do the compile time random
different keys for each string, thanks to __COUNTER__
different keys for each compilation, thanks to __TIME__

little note for namespace, from: https://www.geeksforgeeks.org/namespace-in-c-set-2-extending-namespace-and-unnamed-namespace/
Unnamed Namespaces:
- They are directly usable in the same program and are used for declaring unique identifiers.
- In unnamed namespaces, name of the namespace in not mentioned in the declaration of namespace.
- The name of the namespace is uniquely generated by the compiler.
- The unnamed namespaces you have created will only be accessible within the file you created it in.
- Unnamed namespaces are the replacement for the static declaration of variables.
```cpp
    namespace{ int val = 300; }

    int main(){
        int val=100;
        std::cout<<val<<std::endl;      // 100
        std::cout<<::val<<std::endl;    // 300
    }
```

and namespace here: https://www.geeksforgeeks.org/namespace-c-set-3-creating-header-nesting-aliasing-accessing/
normal space1::variable, or using namespace geek;
namespace alias, nested namespace

TODO: I understand the algorithm but what about hacker skill, learning IDA before moving to 4th implement

# application 2 - obfuscate calls
TODO: to be continue


## TODO to deduce from C++11 code to C++98
- [x] rvalue &&
- [x] template<...>
- [ ] std::tuple
- [ ] constexpr
- [ ] std::enable_if

## TODO:
- [x] static_assert, and assert: for testing program
- [x] how to evaluate inline effect, discussion of inline here: http://www.cplusplus.com/articles/2LywvCM9/
        TODO: wired thing is, even though I do inline, and clang++ -S, the assembly code still have a standalone function
- [x] differnce between static_cast, const_cast, reinterpret_cast, dynamic_cast :
        https://www.tutorialspoint.com/cplusplus/cpp_casting_operators.htm
        better one, http://www.cplusplus.com/doc/tutorial/typecasting/
        ```cpp
            double x = 10.3;
            int y;
            y = int (x);    // functional notation
            y = (int) x;    // c-like cast notation
        ```

tuple logs
```bash
    ./Lib/MetaFSM.h:24:#include <tuple>
    ./Lib/MetaFSM.h:61:            // Generate a list of indexes to extract arguments from tuple
    ./Lib/MetaFSM.h:79:        std::tuple<Args&...> data_;
    ./Lib/tags:100:data_    MetaFSM.h       /^        std::tuple<Args&...> data_;$/;"       m       struct:andrivet::ADVobfuscator::event
```

rvalue reference
```bash
    ./Lib/MetaFSM.h:88:     inline R ObfuscatedCallRet(F f, Args&&... args)
    ./Lib/MetaFSM.h:104:    inline void ObfuscatedCall(F f, Args&&... args)
    ./Lib/MetaFSM.h:123:    inline R ObfuscatedCallRetP(F f, Args&&... args)
    ./Lib/MetaFSM.h:140:    inline void ObfuscatedCallP(F f, Args&&... args)
```

more gaps between different compiler
```cpp
    // Custom literal suffix. Not supported by Intel compiler
    #if !defined(__ICC) && !defined(__INTEL_COMPILER)
    inline const char* operator "" _obfuscated2(const char* str, size_t)
    {
        using I = Make_Indexes<32>::type;
        return MetaString2<I>(str).decrypt();
    }
```

## reading white paper from ADVobfuscator
