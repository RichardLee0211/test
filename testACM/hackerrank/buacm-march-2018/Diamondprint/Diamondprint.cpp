/**
 * from
 * https://www.hackerrank.com/contests/buacm-march-2018/challenges/diamond-print
 */
/* two method: force print, and calculation */
#if 0
/*

*/
#endif /* 0 */
#include<cstdio>
#include<iostream>
#include<vector>
#include<string>

using namespace std;

struct Line{
    int num;
    int lineNum;
    int heading;
    int interval;
    Line(int n, int lineNum):
        num(n), lineNum(lineNum),
        heading(n%2==1? (n-1)/2 - lineNum: (n-2)/2 - lineNum),
        interval(n%2==1? (-1)+2*lineNum: 0+2*lineNum) {
    }
    void printOut(){
        for(int i=0; i<heading; ++i){
            printf(" ");
        }
        printf("*");
        // interval, last star and return
        if(interval == -1){
            printf("\n");
            return;
        }
        if(interval == 0) {
            printf("*\n");
            return;
        }
        for(int i=0; i<interval; ++i){
            printf(" ");
        }
        printf("*\n");
        return;
    }
};

struct Diamond{
    int num;
    int height;
    int realNeedLineNum;
    vector<Line> lines;

    Diamond(int n): num(n), height((n%2)==1? n: n-1), realNeedLineNum((n+1)/2){
        for(int i=0; i<realNeedLineNum; ++i){
            lines.push_back(Line(num, i));
        }
    }
    void printOut(){
        for(int i=0; i<realNeedLineNum; ++i){
            lines[i].printOut();
        }
        for(int i=realNeedLineNum-2; i>=0; --i){
            lines[i].printOut();
        }
    }
};
void func(int n){
    Diamond diamond(n);
    diamond.printOut();
}
int main(){
    int num;
    std::cin>>num;
    func(num);
}
