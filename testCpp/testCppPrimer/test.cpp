#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<set>

using namespace std;



template<unsigned N, unsigned M>
int compare(const char (&p1)[N], const char (&p2)[M]){
    std::cout<<N<<" "<<M<<std::endl;
    return strcmp(p1, p2);
}

int main(){
    compare("waht", "name");
}

template<typename T> class Blob{
public:
    typedef T value_type;
    typedef typename std::vector<T>::size_type size_type;
    // ctor
    Blob() {}
    Blob(std::initializer_list<T> list) {}
    ~Blob() {}
    // number of elements in the Blob
    size_type size() const { return data->size(); }
    bool empty() const { return data->empty(); }
    // add and remove elements
    void push_back(T &t) { data->push_back(t); }
    // move version;
    void push_back(T &&t) { data->push_back(std::move(t)); }
    void pop_back();
    // element access
    T &back();
    T &operator[](size_type i)  { }
private:
    std::shared_ptr<std::vector<T>> data;
    // throws msg if data[i] isn't valid
    void check(size_type i, const std::string &msg)  const;

};
