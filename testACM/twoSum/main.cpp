#include<unordered_map>
#include<vector>

using namespace std;

vector<int> twoSum(vector<int>& numbers, int target) {
    // Key is the number and value is its index in the vector.
    unordered_map<int, int> hash;
    vector<int> result;
    for (unsigned long i = 0; i < numbers.size(); i++) {
        int numberToFind = target - numbers[i];

        // if numberToFind is found in map, return them
        if (hash.find(numberToFind) != hash.end()) {
            result.push_back(hash[numberToFind]);
            result.push_back(i);
            return result;
        }

        //number was not found. Put it in the map.
        hash[numbers[i]] = i;
    }
    return result;
}

int main(){
    vector<int> numbers = {1, 1, 2, 3, 5};
    int target = 5;
    vector<int> result = twoSum(numbers, target);
    return 0;
}
