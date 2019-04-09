/*
 * from
 * https://www.hackerrank.com/contests/buacm-march-2018/challenges/island-size
 */
#include<iostream>
#include<vector>

using namespace std;

struct Island{
    const int ID;
    int size;
    // could have a container containing reference back to elements of this
    // island
    Island(int ID): ID(ID), size(0){}
};

struct Element{
    const int row, col;
    const bool isIsland;
    int islandID; // 0 means never touch

    Element(int i, int j, bool isIsland):
        row(i), col(j), isIsland(isIsland), islandID(0){}
};

struct Area{
    const int height, width; // row<height, col<width
    Element*** elements; // element[i][j] is a pointer to an element
    vector<Island> islands;

    Area(int height, int width):  height(height), width(width){
        elements = new Element**[height];
        for(int i=0; i<height; ++i){
            elements[i] = new Element*[width];
            for(int j=0; j<width; ++j){
                bool temp;
                cin>>temp;
                elements[i][j] = new Element(i, j, temp);
            }
        }
    }
    ~Area(){
        for(int i=0; i<height; ++i){
            for(int j=0; j<width; ++j){
                delete elements[i][j];
            }
        }
    }
    void searchThisIsland(int i, int j, int islandID){
        elements[i][j]->islandID = islandID;
        islands[islandID-1].size++;
        // left
        if(j-1 != -1 &&
                elements[i][j-1]->isIsland && elements[i][j-1]->islandID == 0)
            searchThisIsland(i, j-1, islandID);
        // right
        if(j+1 != width &&
                elements[i][j+1]->isIsland && elements[i][j+1]->islandID == 0)
            searchThisIsland(i, j+1, islandID);
        // up
        if(i-1 != -1 &&
                elements[i-1][j]->isIsland && elements[i-1][j]->islandID == 0)
            searchThisIsland(i-1, j, islandID);
        // down
        if(i+1 != height &&
                elements[i+1][j]->isIsland && elements[i+1][j]->islandID == 0)
            searchThisIsland(i+1, j, islandID);
    }
    void findNewIsland(){
        for(int i=0; i<height; ++i){
            for(int j=0; j<width; ++j){
                if(elements[i][j]->isIsland && elements[i][j]->islandID == 0){
                    int islandID = islands.size() + 1;
                    islands.push_back(Island(islandID));
                    searchThisIsland(i, j, islandID);
#if 0
                    cout<<(*this)<<endl;
#endif
                }
            }
        }
    }
    int getMaxIslandSize(){
        int ret=0;
        for(auto e: islands){
            ret = e.size>=ret? e.size: ret;
        }
        return ret;
    }
    friend ostream &operator<<(ostream &os, Area &area){
        for(int i=0; i<area.height; ++i){
            for(int j=0; j<area.width; ++j){
                os<<area.elements[i][j]->isIsland<<area.elements[i][j]->islandID << " ";
            }
            os<<"\n";
        }
        os<<"\n";
        return os;
    }
};

int main(){
    int testCaseLength = 0;
    cin>>testCaseLength;
    while(--testCaseLength >= 0){
        int testNo, height, width;
        cin >> testNo;
        cin >> height >> width ;
        Area area(height, width);
        area.findNewIsland();
        cout<<testNo<<" "<<area.getMaxIslandSize()<<endl;
    }
}
