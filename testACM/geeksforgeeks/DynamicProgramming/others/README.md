this directory is not from geekforgeek, but very good for DP problem exercise:
here: https://people.cs.clemson.edu/~bcdean/dp_practice/

## integer Knapsack problem
the most important is the formula itself:
$M(n)$ means the max value the pack can contain when capacity is $n$
$S[i]$ means the size of $i$ item
$V[i]$ means the value of $i$ item
$ M(n) = max(M(n-1), max_{i \in [0, n]}(M(n-S[i])+V[i])) $

## balanced partition
#### without the constrain that $ sizeof(S_1) \eq sizeof(S_2) $
$A[N]$ is the array
let $ \sum_{i=0}^{N-1} A[i] = 2S $
$ M(n)$ means sum of subarray that is closest to S
$ M(n)=max(M(n-1), max_{i\in[0, n]}M(n-i)+A[n]) $

#### with $ sizeof(S_1) \eq sizeof(S_2) $
$A[N]$ is the array
$M[N/2]$ contains the index of subarray
let $ \sum_{i=0}^{N-1} A[i] = 2S $
$ M(n)$ means sum of subarray that is closest to S
$ M(n)=
    when M isn't full and sum(M)+A[n]<S, add n to M
    when M is full, and sum(M)<S, substitute A[n] with \all_{i\in[0, n-1]} A[M[i]], if(sum(M)-A[M[i]]+A[n] > sum(M)), then substitute
$

## Maximum Value contiguous Subsequence
$A[N]$ is the array
let $M[n]$ means the maximum value contiguous subsequence A[i~j] in A[1~n].
$ M[n] =
    when $ \sum_{k=j+1}^{n} (A[k]) >= 0 $, substitute j with n
    else M[n-1]
$
TODO: find test cases and code in C++

## others
a discussion about N, NP, NP-complete, NP-hard problem's defination, don't understand clearly: https://stackoverflow.com/questions/1857244/what-are-the-differences-between-np-np-complete-and-np-hard?rq=1
a good chinese article talking about this: http://www.matrix67.com/blog/archives/105
```cite
    Decision problem: A problem with a yes or no answer.
    P is a complexity class that represents the set of all decision problems that can be solved in polynomial time.
    NP is a complexity class that represents the set of all decision problems for which the instances where the answer is "yes" have proofs that can be verified in polynomial time.
    NP-complete is a complexity class which represents the set of all problems X in NP for which it is possible to reduce any other NP problem Y to X in polynomial time.
    NP-hard: a problem X is NP-hard, if there is an NP-complete problem Y, such that Y is reducible to X in polynomial time.
```
a kind of time complexity: $ \theta(1), \theta( \log(n)), \theta(n^a)$
another time complexity, bad for computer: $ \theta(a^n), \theta(n!)
