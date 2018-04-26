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
        // sort wor alphabetically so we can find the duplicates
        sort(words.begin(), words.end());
        // unique reorders the input range so that each word apperas once in
        // the front portion of the range and returns an iterator one past the unique range
        auto end_unique = unique(words.begin(), worfs.end());
        // erase uses a vector operation to remove the nonunique elements
        words.erase(end_unique, words.end());
    }
```

this is a strange output after unique, what's after end_unique is unknown
```cpp
    template<typename T>
    int print(const vector<T> &that){
        for(auto i=that.cbegin(); i<that.cend(); ++i)
            std::cout<< *i <<" ";
        std::cout<<std::endl;
        return 0;
    }

    template<typename T>
    void elimDups(vector<T> &words){
        std::cout<<"origin: "; print(words);
        sort(words.begin(), words.end());
        std::cout<<"after sort: "; print(words);
        auto end_unique = unique(words.begin(), words.end());
        std::cout<<"after unique: "; print(words);
        words.erase(end_unique, words.end());
        std::cout<<"after erase: "; print(words);
    }

    int main(){
        vector<int> v1{11, 1, 3, 4, 5, 6, 1,2,3,4,5};
        vector<int> v2 = v1;
        elimDups(v1);
    }
```
```output
    ➜  testCppPrimer git:(master) ✗ ./a.out
    origin: 11 1 3 4 5 6 1 2 3 4 5
    after sort: 1 1 2 3 3 4 4 5 5 6 11
    after unique: 1 2 3 4 5 6 11 5 5 6 11
    after erase: 1 2 3 4 5 6 11
```
The library algorithms operate on iterators, not containers. Therefore,
an algorithm cannot (directly) add or remove elements.
but algorithms can change value by std::swap or assignment

#### using container operations or remove elements

## 10.3 customizing operations

### 10.3.1 passing a function to an algorithm
#### predicates
A predicate is an expression that can be called and that returns a value that can be used as a condition.
```cpp
    // comparison function to be used to sort by word length
    bool isShorter(const string &s1, const string &s2)
    {
        return s1.size() < s2.size();
    }
    // sort on word length, shortest to longest
    sort(words.begin(), words.end(), isShorter);
```
but this doesn't do secondary sort

#### sorting algorithms
- stable sort
maintain the original sequels if they are equal to sort function

### 10.3.2 lambda expression
- find_if
#### introducing lambdas
[capture list] (parameter list) -> return type { function body }
#### passing arguments to a lambda
#### using the capture list
#### call find_if
#### for_each algorithm
#### putting it all together
capture list is only for (non-static) varibles defined in the surrounding function
```cpp
    // put words in alphabetical order and remove duplicates
    // resort by length, maintaining alphabetical order among words of the same length
    // get an iterator to the first element whose size() is >= sz
    // compute the number of elements with size >= sz
    // print words of the given size or longer, each one followed by a space
    void biggies(vector<string> &words, vector<string>::size_type sz)
    {
        elimDups(words);
        stable_sort(words.begin(), words.end(), isShorter);
        // use lambda because the UnaryPredicate only could pass one parameter
        auto wc = find_if(words.begin(), words.end(),
                [sz](const string &a){ return a.size() >= sz; });
        auto count = words.end() - wc;
        cout << count << " " << make_plural(count, "word", "s")
            << " of length " << sz << " or longer" << endl;
        for_each(wc, words.end(),
                [](const string &s){cout << s << " ";}); cout << endl;
    }
```

### 10.3.3 lambda captures and returns
TODO: skipped, come back when you feel necessary
#### capture by value
#### capture by reference
#### implicit captures
#### mutable lambdas
#### specifying the lambda return type

### 10.3.4 binding arguments
#### ...

## 10.4 revisiting Iterators
### 10.4.1 insert iterators
### 10.4.2 iostream iterators
### 10.4.3 reverse iteratiors

## 10.5 structure of generic algorithm
## 10.6 container-specific algorithm

# ch11 associative containers
!!Associative and sequential containers differ from one another in a fundamental
way: Elements in an associative container are stored and retrieved by a key.
In contrast, elements in a sequential container are stored and accessed
sequentially by their position in the container.

The two primary associative-container types are map and set.

## 11.1 using an associative container
#### using a map
```cpp
    // count the number of times each word occurs in the input
    map<string, size_t> word_count; // empty map from string to size_t
    string word;
    while (cin >> word)
        ++word_count[word];
    for (const auto &w : word_count)
        cout << w.first << " occurs " << w.second
        << ((w.second > 1) ? " times" : " time") << endl;
```
#### using a set
```cpp
    // count the number of times each word occurs in the input
    map<string, size_t> word_count; // empty map from string to size_t
    set<string> exclude = {"The", "But", "And", "Or", "An", "A",
        "the", "but", "and", "or", "an", "a"};
    string word;
    while (cin >> word)
        if (exclude.find(word) == exclude.end())
            ++word_count[word]; // fetch and increment the counter for word
```

## 11.2 overview of the associative containers
### 11.2.1 defining an associative container
```cpp
    map<string, size_t> word_count; // empty
    // list initialization
    set<string> exclude = {"the", "but", "and", "or", "an", "a",
                            "The", "But", "And", "Or", "An", "A"};
    // three elements; authors maps last name to first
    map<string, string> authors = {
                    {"Joyce", "James"},
                    {"Austen", "Jane"},
                    {"Dickens", "Charles"} };
```

#### initializing a multimap or multiset
...

## 11.3 operations on associative containers
...

# ch16 templates and generic programming
## 16.1 defining a template
### 16.1.1 function templates
#### ...
#### nontype template parameters
```cpp
template<unsigned N, unsigned M>
int compare(const char (&p1)[N], const char (&p2)[M]){
    return strcmp(p1, p2);
}
```

#### ...
#### tempalte compilation
As a result, unlike nontemplate code, headers for templates typically include
definitions as well as declarations

### 16.1.2 class templates




# others
in my note system, TODO: and ?? is the most used mark
and what about warning, note, etc
