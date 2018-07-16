// the blocks problem, Uva 101
// mova a onto b
// move a over b
// pile a onto b
// pile a over b

#include<csstdio>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

const int maxn = 30;

int n;

vector<int> pile[maxn];

void find_block(int a, int& p, int& h){
    for(p=0; p<n; p++)
        for(h=0; h<pile[p].size(); h++)
            if(pile[p][h] == a) return;
}

void clear_block(int a)
