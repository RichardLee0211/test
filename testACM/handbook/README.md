here: https://cses.fi/book/book.pdf
luck to find this book, when check C-style IO, and this book contain all the methods I get from internet
good, let's start

## ch4 data structures
### dynamic array
!! std::string is also dynamic array

### set structures
std::set self-balance-tree, base operation in &\theta(logn)&
std::unordered_set hashing function, basic operation in $\theta(1)$

### map structures
wait, for looking for repeat value in a array,
I could use map<value_t, int> to map from value to the number of value, great could solve in $\theta(n)$
I also could use std::set or std::unorder_setto find values...
this is like

### iterators and ranges

### other structures
bitset, interesting
queue
deque, two sides
priority queue, interesting
stack
policy-based data structures

### comparsion to sorting

## ch8 Amortized analysis
### two pointers method
- subarray sum
- two sum
- 3sum problem
here: https://en.wikipedia.org/wiki/3SUM
$\theta(n^2)$ method:
way1: for each i and j in array, find S-X[i]-X[j], using hash table so we can do search in $\thata(1) time$
so what using hash table means in c++ is to use std::unorderd_map<int, int> hash
way2: sort array, loop array with a; for each X[a], only need to find b and c in X[a+1 ~ n-1] such that X[b]+ X[c] = S - X[a]
- subset sum
here: https://en.wikipedia.org/wiki/Subset_sum_problem
there is a Pseudo-polynomial time dynamic programming solution in this wiki page

### mearst smaller elements
using stack to do work,
TODO: I need a application of this question ??
TODO: programming exercise

### sliding window minimum
using queue, this is increment queue

## Advanced topic
## ch21 number theory
### primes and factors
great, I wanna learn it
sum of factors: !!
TODO: how to improve that $p_i$ is prime number, then $\sum_i=1^n (p_i) + 1$ is also prime number. page.198
- basic algorithm
- sieve of eratosthenes
interesting series:
$ \sum_x=2^n (n/x) = n/2 + n/3 + ... + n/n = \bigoh(nlogn) $
this series: $ \sum_i=2^\infinte (1/i) $ is here: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)

- Euclid's algorithm
    greatest common devisor(gcd)
    least common multiple(lcm)
    for i \in [2, n], p_i is prime numbers needed
    a = p_1^{\alpha_1} * p_2^{\alpha_2} * ... * p_n^{\alpha_n}
    b = p_1^{\beta_1} * p_2^{\beta_2} * ... * p_n^{\beta_n}
    gcd(a, b) = p_1^{min(\alpha_1, \beta_1)} * p_2^{min(\alpha_2, \beta_2)} * ... * p_n^{min(\alpha_n, \beta_n)}
    lcm(a, b) = p_1^{max(\alpha_1, \beta_1)} * p_2^{max(\alpha_2, \beta_2)} * ... * p_n^{max(\alpha_n, \beta_n)}

    crazy:
    prove of Euclid's algorithm ?: recall that c|a in number theory means c is a factor of a. here: https://courses.cs.washington.edu/courses/cse311/14au/slides/lecture13.pdf
    ```cpp
        int gcd(int a, int b){
            if(b==0) return a;
            return gcd(b, a%b);
        }
    ```
    what does it do with Fibonacci numbers ?: easy to solve

    somethind about mod
    n%m = ((double) (n/m) - (long)(n/m)) * m

- Euler's totient function

### modular arithmetic
- modular exponentiation, page.202
smart
```cpp
    int modpow(int x, int n, int m){
        if(n==0) return 1%m;
        int u = modpow(x, n/2, m);
        u = (u*u) % m;
        if(n/2 == 1) u=(u*x) % m;
        return u;
    }
```

- Fermat's theorem and Euler's theorem
TODO: how and for what??

- modular inverse
great, useful in cryptosystem

## solving equations
### Diophantine equations

### chinese remainder theorem
TODO: don't understand ??

## ch22 combinatorics
all right, let's keeping going
### binomial coefficients
!!counting the number of ways to represent an integer n as a sum of positive integer, page.207
!!OMG: sum of binomial coefficients is n^2, and why pascal's triangle is important. (a+b)^n
- boxes and balls
!!OMG, scenario 2 and 3 are smart
- multinomial coefficients

### catalan numbers
- parenthesis expressions
TODO: formula1: don't understand why ??
!!formula2: 66
- counting trees
kepa

### inclusion-exclusion
- inclusion-exclusion

- derangements
understand the formula is just the first step to solve this kind of question
TODO: don't real understand f(n-1)??

### Burnside's lemma
TODO: low power to understand

### cayley's formula
TODO: low power

## ch27 square root algorithm

## ch28 segment trees revisited

## ch29 geometry
very happy to algorithm assignment lead me to here, hack it
!!Heron's formula: area of triangle:$s(s-a)(s-b)(s-c)^(1/2)$ where a, b, c is side of triangle, s=(a+b+c)/2
!!page.266, the magic area formalu, TODO: but how it come??
### complex numbers
std::complex<double>
std::abs()
std::arg()
std::polar(length, angle)
std::conj(vector) // conjugate

### points and lines
- point location
- line segment intersection
- point distance from a line
I would like to review vector, here: https://en.wikipedia.org/wiki/Euclidean_vector
dot product: $a \dot b = a_1 \times b_1 + a_2 \times b_2 + a_3 \times b_3 $
cross product: $ ... $
- point inside a polygon

### polygon area
!! page.271, the formula: 66
- pick's theroem

### distance functions
- rotating coordinates

## ch30 sweep line algorithms
WTF, the closest pair problem is in here
continue
### intersection points
### closest pair problem
### convex hull problem

TODO: to be continue, finish chapters that you like, heading to assignment


# others
when convert markdown to latex,
add \begin{align*} \end{align*}
add \\
add \text{} or \inserttext{}
* => \times
min => \min
max => \max
