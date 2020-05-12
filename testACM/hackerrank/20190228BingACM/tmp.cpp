#include<cstdio>
#include<map>
#define N 1000

std::map<char, char> charMap{{'c', 'a'}};

int main(){
    // printf("%c\n", charMap.at('c'));
    char buf[N];
    sprintf(buf, "what %c", charMap.at('c'));
    sprintf(buf, "what %c", charMap.at('c'));
    sprintf(buf, "what %c", charMap.at('c'));
    sprintf(buf, "what %c", charMap.at('c'));
    printf("%s", buf);
}
