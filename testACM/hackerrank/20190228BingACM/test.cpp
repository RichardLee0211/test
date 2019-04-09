#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include<map>
#include<vector>
#include<iostream>

/*
 * abcd efg
 * hijk lmn
 * opq rst
 * uvw xyz
 *
cgnajmxgk tjvvxixkxaxqv
factorial possibilities

vj oq pzsqmvagzs xc yjp rpva ogza aj lxhq pt
so we understand if you just want to give up now
 * */

    std::map<char, char> charMap{
        {'a', 't'},
        {'b',  ' '},
        {'c', 'f'},
        {'d', 'p'},
        {'e', 'x'},
        {'f', 'k'},
        {'g', 'a'}, // 7, 1
        {'h', 'h'},
        {'i', 'b'},
        {'j', 'o'},
        {'k', 'l'},
        {'l', 'g'},
        {'n', 'c'}, // 14, 3
        {'m', 'r'},
        {'o', 'w'},
        {'p', 'u'},
        {'q', 'e'},
        {'r', 'j'},
        {'s', 'd'},
        {'t', 'p'},
        {'u', ' '},
        {'v', 's'},
        {'w', 'h'},
        {'x', 'i'},
        {'z', 'n'}, // 26, 14
        {'y', 'y'},
    };

/* Enter your code here. Read input from STDIN. Print output to STDOUT */
int main() {
    int N=0;
    scanf("%d", &N);


    while(N-- >= 0){
        // std::vector<char> token;
        // char temp;
        // int status=0;
        std::string line;
        std::string token;
        size_t pos = 0;

        while(std::getline(std::cin, line)){
            while((pos = line.find(std::string(" "))) != std::string::npos){
                token = line.substr(0, pos);
                if(token[token.length()-1] > 'a' && token[token.length()-1] < 'z'){
                    bool tmp = true;
                    for(int i=0; i<(int)token.length(); i++){
                        if(token[i] != token[token.length()-i]){
                            tmp = false;
                            break;
                        }
                    }
                    if(tmp == true){
                        break;
                    }
                    else{
                        for(int i=0; i<(int)token.length(); i++){
                            printf("%d", charMap[token[i]]);
                        }
                    }
                }
                else{
                    //...
                }
            }
            line.erase(0, pos+1);

        }
    }
    return 0;
}
