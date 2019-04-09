/*
 * from https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
 */
/*
 * using queue, FILO
 */

#include<iostream>
#include<queue>
#include<string>

enum Parenthesis{
    LeftBrace = '{',
    RightBrace = '}',
    LeftParenthsis = '(',
    RightParenthsis = ')',
    LeftBracket = '[',
    RightBracket = ']'
};

char map(const char tmpChar){
    if(tmpChar == '}')
        return '{';
    if(tmpChar == ']')
        return '[';
    if(tmpChar == ')')
        return '(';
    return '.';
}

int main(){
    int testCaseNum{0};
    std::cin>>testCaseNum;
    while(--testCaseNum >=0){
        char tmpChar;
        std::string input;
        std::queue<char> qchar;
        bool isBalance{true};

        std::getline(std::cin, input, '\n');
        for(size_t i=0; i<input.size(); ++i){
            tmpChar = input[i];
            if(tmpChar == '{' || tmpChar == '(' || tmpChar == '['){
                qchar.push(tmpChar);
                continue;
            }
            if(qchar.back() != map(tmpChar)){
                std::cout<<"not balanced\n";
                isBalance = false;
                break;
            }
        }
        if(isBalance == true)
            std::cout<<"Balanced\n";
    }
}
