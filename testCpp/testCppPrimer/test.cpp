#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<set>

using namespace std;

void foo(string str) {
    cout<<str<<endl;
}

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

// comparison function to be used to sort by word length
bool isShorter(const string &s1, const string &s2)
{
    return s1.size() < s2.size();
}

void biggies(vector<string> &words, vector<string>::size_type sz)
{
    elimDups(words);
    stable_sort(words.begin(), words.end(), isShorter);
    // use lambda because the UnaryPredicate only could pass one parameter
    auto wc = find_if(words.begin(), words.end(),
            [sz](const string &a){ return a.size() >= sz; });
    auto count = words.end() - wc;
    cout << count << " " // << make_plural(count, "word", "s")
        << " of length " << sz << " or longer" << endl;
    for_each(wc, words.end(),
            [](const string &s){cout << s << " ";});
    cout << endl;
}

int main(){
#if 0
    vector<int> v1{11, 1, 3, 4, 5, 6, 1,2,3,4,5};
    // vector<int> v2 = v1;
    // elimDups(v1);
    auto it = v1.begin();
    cout<< *(it+2)<<endl;

    vector<string> words{"what", "do", "you", "want", "went", "why"};
    // sort on word length, shortest to longest
    // stable_sort(words.begin(), words.end(), isShorter);
    // print(words);
    biggies(words, 3);
#endif

    map<string, size_t> word_count; // empty map from string to size_t
    set<string> exclude = {"The", "But", "And", "Or", "An", "A",
                            "the", "but", "and", "or", "an", "a"};
    string word;
    while (cin >> word)
        if (exclude.find(word) == exclude.end())
            ++word_count[word]; // fetch and increment the counter for word
}
