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
