# this is note of ADVobfucator
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

## TODO to deduce from C++11 code to C++98
- [ ] rvalue &&
- [ ] template<...>
- [ ] std::tuple
- [ ] constexpr
- [ ] std::enable_if

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
