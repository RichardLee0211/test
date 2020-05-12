#include<string>
#include<vector>

/**
 * Solution 1
 * limited characters, put in linked list,
 * get charContent, if it's
 * create a charNode,
 */
/*
class charNode{
private:
    char charContent;
    size_t pos;

public:
    charNode(char charContent, size_t pos);
};
*/

class Solution {
public:
    /**
     * failed since wrong decision of beginning of substring
     * e.g. dvdf, expect 3, result 2
     */
    int lengthOfLongestSubstring_fail(std::string s) {
        int content[256] = {0};  for (size_t j=0; j<256; ++j) content[j] = -1;
        int pos = 0, res = 0, tmp = 0;
        for(size_t i=0; i<s.size(); ++i){
            pos = (unsigned int) s[i];
            if (content[pos] == -1){
                ++tmp;
                content[pos] = i;
            } else {
                tmp = 1;
                for (size_t j=0; j<256; ++j) content[j] = -1;
                content[pos] = i;
            }
            if(tmp > res) res = tmp;
        }

        return res;
    }

    int lengthOfLongestSubstring_refer(std::string s) {
        std::vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (size_t i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = (maxLen > (int)(i-start)) ? maxLen : (i-start) ;
        }
        return maxLen;
    }

    int lengthOfLongestSubstring(std::string s) {
        int content[256] = {0};  for (size_t j=0; j<256; ++j) content[j] = -1;
        int pos = 0, maxLength = 0, start = -1;
        for(size_t i=0; i<s.size(); ++i){
            pos = (unsigned int) s[i];
            start = content[pos]>start ? content[pos] : start;
            content[pos] = i;
            maxLength = (maxLength > (int)(i-start)) ? maxLength : (i-start) ;
        }
        return maxLength;
    }
};

int main(){
    Solution* solution = new Solution();
    std::string str1 = "dvdf";
    solution->lengthOfLongestSubstring(str1);
    return 0;
}
