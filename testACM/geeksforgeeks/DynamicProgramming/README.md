## Longest Increasing Subsequence
way1:
$ A[N]$ is that array
$ dp[n]$ means the A[n]'s highest ranking in multipy subarrays
$ dp[n] = max(max_{i<n && A[i]<A[n]}(dp[i]+1), 1 )$
time complicity: $ \theta(n^2) $
way2: see code
