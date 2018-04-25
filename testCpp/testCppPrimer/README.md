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

```cpp
    /**
     * # from c++ primer
     * ### 12.1.1 the  share_ptr class
     */

#include<string>
#include<vector>
#include<initializer_list>

    using namespace std;

    class StrBlob{
    public:
        typedef std::vector<std::string>::size_type size_type;
        StrBlob();
        StrBlob(std::initializer_list<std::string>);
        size_type type_size() const { return data->size(); }
        bool empty() const { return data->empty(); }
        // add and remove elements
        void push_back(const std::string &t) { data->push_back(t); }
        void pop_back();
        // element access
        std::string &front() const;
        std::string &back() const;

    private:
        std::shared_ptr<std::vector<std::string>> data;
        // throws msg if data[i] isn't valid
        void _check(size_type i, const std::string &msg) const;
    };

    StrBlob::StrBlob() : data(std::make_shared<std::vector<std::string>>()) { }
    StrBlob::StrBlob(std::initializer_list<std::string> list) :
        data(make_shared<vector<string> >(list)) { }

    void StrBlob::_check(size_type i, const string &msg) const{
        if(i >= data->size())
            throw out_of_range(msg);
    }

    string &StrBlob::back() const{
        this->_check(0, string("back on empty StrBlob"));
        return data->back();
    }

    void StrBlob::pop_back(){
        this->_check(0, string("back on empty StrBlob"));
        data->pop_back();
    }
    std::string &StrBlob::front() const{
        // this->_check(this->type_size()-1, "front")
        return this->data->front();
    }

    int main(){
    }
```

### 12.1.2 managing memory directly
### 12.1.3 using shared_ptrs with new, PageNo.559
```cpp
    share_ptr<int> p1 = new int(1024); // error: must use direct initializeion
    share_ptr<int> p2(new int(1024)); // ok: uses direct initialize

    share_ptr<int> clone(int p){
        return new int(p); // error: implicit  conversion to share_ptr<int>
    }
    shared_ptr<int> clone(int p){
        // ok: explicity create a shared_ptr<int> from int*
        return shared_ptr<int> (new int(p));
    }
```

# ch10 Generic Algorithms
## 10.1 overview
algorithm act like c function, a free function
```cpp
    int val = 42;
    auto result = find(vec.cbegin(), vec.cend(), val);
    cout << "The value " << val<<
            (result == vec.cend()
            ? " is not present" : " is present") << endl;
```

## 10.2 A first look at the algorithms
### 10.2.1 Read-Only Algorithms
- find
- count
- accumulate
- equal

when find the input range is not in one contain, find still do the action,
surprise~, undefined behavior
```cpp
    vector<int> v1{1,2,3,4,5};
    vector<int> v2 = v1;
    for(auto i=v2.begin(); i<v2.end(); ++i){
        cout<<*i<<" ";
    }
    auto i = find(v1.begin(), v2.end(), 7);
    cout<<endl<<*i<<endl;
```

string literal treat as const char*
could initialize a string with
```cpp
    string str = "what"; // ok, but not prefer
    string str2("what"); // prefered
    string str3{" you doing ?"}; // best since c++14
    void foo(string str) {}
    int main(){
        foo("waht");  // OK, but not prefer
        foo(string("what"));
    }
```

TODO: operator== of myclass relate to num, do I need to implement everyone of
them with int, double, long, long long??

### 10.2.2 Algorithms That Write Container Elements
- fill
- fill_n

OGM, unknow that algorithm library have this undefined behavior, use with care
```cpp
    vector<int> vec; // empty vector
    // disaster: attempts to write to ten (nonexistent) elements in vec
    fill_n(vec.begin(), 10, 0);
```

#### introduce back_inserter
- back_inserter
``cpp
    vector<int> vec; // empty vector
    // ok: back_inserter creates an insert iterator that adds elements to vec
    fill_n(back_inserter(vec), 10, 0); // appends ten elements to vec
```


Remember, algorithms do not perform container operations, so they have no way
themselves to change the size of a container.

#### copy algorithms
- copy
example with buildin array
```cpp
    int a1[] = {0,1,2,3,4,5,6,7,8,9};
    int a2[sizeof(a1)/sizeof(*a1)]; // a2 has the same size as a1
    // ret points just past the last element copied into a2
    auto ret = copy(begin(a1), end(a1), a2); // copy a1 into a2
```

- replace
- replace_copy

### 10.2.3 Algorithms that record container elements
- sort

#### Eliminating Duplicates
```cpp
    void elimDups(vector<string> &words){
        // sort wor alphabetically so we can find
    }
```
