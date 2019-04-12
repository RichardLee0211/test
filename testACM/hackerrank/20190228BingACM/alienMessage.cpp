#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include<map>
#include<vector>
#include<iostream>


std::map<char, char> charMap{
    {'a', 't'},
    {'b', 'm'},
    {'c', 'f'},
    {'d', 'z'},
    {'e', 'x'},
    {'f', 'k'},
    {'g', 'a'}, // 7, 1
    {'h', 'v'},
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
    {'u', 'q'},
    {'v', 's'},
    {'w', 'h'},
    {'x', 'i'},
    {'y', 'y'},
    {'z', 'n'} // 26, 14
};

/* Enter your code here. Read input from STDIN. Print output to STDOUT */
int main() {
    int N=0;
    scanf("%d\n", &N);


    while(N-- >= 0){
        // std::vector<char> token;
        // char temp;
        // int status=0;
        std::string line;
        std::string token;
        char buf[1000];
        size_t pos = 0;

        while(std::getline(std::cin, line)){
            // std::cout<<line<<"\n";
            int buf_index = 0;
            int search_index = 0;
            while((pos = line.find(std::string(" "), search_index)) != std::string::npos){
                token = line.substr(search_index, pos-search_index);
                search_index = pos+1;
                int length = token.length();
                // std::cout<<token<<" "<<pos<<std::endl;

                /* handle , . ! ? */
                if(token[token.length()-1] < 'a' || token[token.length()-1] > 'z'){
                    length = token.length()-1;
                }

                bool isPalindrome= true;
                for(int i=0; i<(int)(length/2); i++){
                    if(token[i] != token[length-1-i]){
                        isPalindrome = false;
                        break;
                    }
                }
                if(isPalindrome  == false){
                    /* translate and print */
                    for(int i=0; i<length; i++){
                        sprintf(buf+buf_index, "%c", charMap.at(token[i]));
                        buf_index+=1;
                    }
                }
                /* printf period and space */
                if(length == (int)token.length()-1){
                    sprintf(buf+buf_index, "%c", token[token.length()-1]);
                    buf_index +=1;
                }
                sprintf(buf+buf_index, " ");
                buf_index+=1;
            }
            /* the last token */
            {
                token = line.substr(search_index, line.length()-search_index);
                int length = token.length();

                /* handle , . ! ? */
                if(token[token.length()-1] < 'a' || token[token.length()-1] > 'z'){
                    length = token.length()-1;
                }

                bool isPalindrome= true;
                for(int i=0; i<(int)(length/2); i++){
                    if(token[i] != token[length-1-i]){
                        isPalindrome = false;
                        break;
                    }
                }
                if(isPalindrome  == false){
                    /* translate and print */
                    for(int i=0; i<length; i++){
                        sprintf(buf+buf_index, "%c", charMap.at(token[i]));
                        buf_index+=1;
                    }
                }
                /* printf period and space */
                if(length == (int)token.length()-1){
                    sprintf(buf+buf_index, "%c", token[token.length()-1]);
                    buf_index +=1;
                }
            }
            /* print buf, skip leading space and tail space and double spaces */
            int i=0;
            while(buf[i]==' '){
                i++;
            }
            for(; i<buf_index; i++){
                if(buf[i]==' ' && buf[i+1]==' ') continue;
                printf("%c", buf[i]);
            }
            printf("\n");
        }
    }
    return 0;
}
