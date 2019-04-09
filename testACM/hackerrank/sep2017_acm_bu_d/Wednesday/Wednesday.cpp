/*
 * case-insensitive compare
 */

#include<string>
#include<iostream>
#include<ctype.h>

using namespace std;

bool is_letter(char a)
{
    if((a>='A'&&a<='Z') || (a>='a'&&a<='z'))
        return true;
    return false;
}

bool case_insensitive_compare(string str1, string str2)
{
    if(str1.length() != str2.length()) return false;

    for(int i=0; i<(int)str1.length(); ++i){
        if(is_letter(str1[i])){
            if(toupper(str1[i]) != toupper(str1[i]))
                return false;
        }else{
            if(str1[i] != str2[i])
                return false;
        }
    }
    return true;
}

int main()
{
    string str1 = "wendesday";
    string str2 = "Wendesday";
    cin>>str2;
    if(case_insensitive_compare(str1, str2))
        cout<<"It is Wednesday, my dudes\n";
    else
        cout<<"me too thanks\n";

    return 0;
}
