# from c++ primer
### 12.1.1 the  share_ptr class
std::out_of_range() reference in http://www.cplusplus.com/reference/stdexcept/out_of_range/

#### about pass string as argument, pass string literal
```cpp
#if 0
    void print(std::string s){ // ok, will call string("whatever you put here")
        std::cout<<s<<std::endl;
    }
    void print(const std::string &s){ // buggy, don't pass string literal, pass string temporary
        std::cout<<s<<std::endl;
    }
    void print(const char* s){ // ok
        std::cout<<s<<std::endl;
    }
#endif

    void print(char* s){ // error, since implement can change s
        s[1] = '1';
        printf("%s\n", s);
    }

    int main(){
        print("what");
    }
```
```error
    ➜  testCppPrimer git:(master) ✗ clang++ test1.cpp
    test1.cpp:17:11: warning: conversion from string literal to 'char *' is deprecated [-Wc++11-compat-deprecated-writable-strings]
        print("what");
                  ^
                  1 warning generated.
```

- initializer_list is since c++11
- initializer_list<vector<string>> is a error because of >> confusing
```error
    test.cpp:34:35: error: a space is required between consecutive right angle brackets (use '> >')
    data(make_shared<vector<string>>(list)) { }
    ^~
    > >
    test.cpp:34:38: error: use of undeclared identifier 'list'
    data(make_shared<vector<string>>(list)) { }
    ^
    8 errors generated.
```

### 12.1.2 managing memory directly
