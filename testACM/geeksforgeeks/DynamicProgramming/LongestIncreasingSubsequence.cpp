/*
 * this is from
 * https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
 */

#include<iostream>
#include<vector>
// #include < bits/stdc++.h >

using namespace std;

// Binary search
// T is reference to tailIndices, which is always sorted
// return index of ceil in set of arr[tailIndices[i]], l<i<r
int GetCeilIndex(int arr[], vector<int> &T, int l, int r, int key){
    while (r - l > 1)
    {
        int m = l + (r - l)/2;
        if (arr[T[m]] >= key)
            r = m;
        else
            l = m;
    }

    return r;
}

// record the actual subarray by using tailIndices[len-1] and prevIndices[]
// return length of LongestIncreasingSubquence in arr
// way2
// time complexity: $\theta(n\log (n))$
int LongestIncreasingSubquence(int arr[], int n){
    // Add boundary case, when array n is zero
    // Depend on smart pointers

    vector<int> tailIndices(n, 0); // tailIndices[i] is the index of tail of subarray, length i+1. Initialized with 0
    vector<int> prevIndices(n, -1); // prevIndices[i] means index of A[i]'s previous element in subarray. initialized with -1

    int len = 1; // length of subarray, tailIndices[len-1] is index of tail of LongestIncreasingSubquence, tailIndices[len] is like sentinal
    for (int i = 1; i < n; i++)
    {
        if (arr[i] < arr[tailIndices[0]])
        {
            // new smallest value
            tailIndices[0] = i;
        }
        else if (arr[i] > arr[tailIndices[len-1]])
        {
            // arr[i] wants to extend largest subsequence
            prevIndices[i] = tailIndices[len-1];
            tailIndices[len++] = i;
        }
        else
        {
            // arr[i] wants to be a potential condidate of
            // future subsequence !!
            // It will replace ceil value in tailIndices
            int pos = GetCeilIndex(arr, tailIndices, -1,
                    len-1, arr[i]);

            prevIndices[i] = tailIndices[pos-1];
            tailIndices[pos] = i;
        }
    }

    cout << "LIS of given input" << endl;
    for (int i = tailIndices[len-1]; i >= 0; i = prevIndices[i])
        cout << arr[i] << " ";
    cout << endl;

    return len;
}

int main()
{
    int arr[] = { 2, 5, 3, 7, 11, 8, 10, 13, 6 };
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("LIS size %d\n", LongestIncreasingSubquence(arr, n));

    return 0;
}

/* way 1
 * couldn't record the actual subarray
 */
int main_test() {
    int t;
    cin >> t;
    while(t--) {
        int n; // number of elements
        cin >> n;
        vector<int> v(n), dp(n);
        for (int i=0; i < n; i++) {
            cin >> v[i]; // store values and
            dp[i] = 1; // its sorting value in substring
        }
        int ans = 0;
        for (int i=0; i < n; i++) {
            int tmp = 1;
            for (int j=i-1; j >= 0; j--) {
                if (v[j] < v[i])
                    tmp = max(tmp, dp[j]+1);
            }
            dp[i] = tmp;
            ans = max(ans, tmp);
        }
        cout << ans << "\n";
    }
    return 0;
}
