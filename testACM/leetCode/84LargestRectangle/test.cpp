// https://leetcode.com/problems/largest-rectangle-in-histogram/description/
// explanation of best answer here: geekforgeek.org
#include<vector>
#include<iostream>

/* time compleixity = n^2, sucks */
int largestRectangleArea_1(const std::vector<int>& heights) {
    int area = 0, size = heights.size();
    for(int i=0; i<size; ++i){
        int j=i, h=i, width = 1;
        while(j-1>=0 && heights[--j]>=heights[i]) ++width;
        while(h+1<size && heights[++h]>=heights[i]) ++width;
        if(area<width*heights[i])
            area = width*heights[i];
    }
    return area;
}

#define DEBUG 1

int largestRectangleArea(std::vector<int>& height) {

    int ret = 0;
    height.push_back(0);
    std::vector<int> index;

    for(int i = 0; i < (int)height.size(); i++)
    {
        while(index.size() > 0 && height[index.back()] >= height[i])
        {
            int h = height[index.back()];
            index.pop_back();

            int sidx = index.size() > 0 ? index.back() : -1;
            if(h * (i-sidx-1) > ret)
                ret = h * (i-sidx-1);
        }
        index.push_back(i);
#if DEBUG
        std::cout<<"i: "<<i<<" ret:"<<ret<<"\n";
        for(auto h: index) std::cout<<h<<" ";
        std::cout<<"\n";

#endif /* DEBUG */
    }

    return ret;
}

int main(){
    std::vector<int> vec{0, 1, 2, 3, 4, 5, 6};
    // std::vector<int> vec{0};
    // std::cout<<vec[2]<<"\n"; // output 0
    std::cout<<largestRectangleArea(vec)<<"\n";
}
