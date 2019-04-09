## there are some tricks for competitive programming
from: https://www.geeksforgeeks.org/c-tricks-competitive-programming-c-11/

1) Checking if the number is even or odd without using the % operator:
```cpp
    if (num & 1)
        cout << "ODD";
    else
        cout << "EVEN";
```

2) Fast Multiplication or Division by 2
```c++
    n = n << 1;   // Multiply n with 2
    n = n >> 1;   // Divide n by 2
```

3) Swapping of 2 numbers using XOR:
```c++
    // A quick way to swap a and b
    a ^= b;
    b ^= a;
    a ^= b;
```

4) Avoiding use of strlen():
```c++
    //  Use of strlen() can be avoided by:
    for (i=0; s[i]; i++)
    {
    }
    // loop breaks when the character array ends.
```

5)
...

9) Calculating the most significant digit: To calculate the most significant digit of any number log can be directly used to calculate it.
```seudocode
    Suppose the number is N then
    Let double K = log10(N);
    now K = K - floor(K);
    int X = pow(10, K);
    X will be the most significant digit.
```

10) Calculating the number of digits directly: To calculate number of digits in a number, instead of looping you can efficiently use log :
Number of digits in N =floor(log10(N)) + 1;

11) Efficient trick to know if a number is a power of 2 sing the normal technique of division the complexity comes out to be O(logN), but it can be solved using O(v) where v are the number of digits of number in binary form.
```c++
    // !! so cool
    /* Function to check if x is power of 2*/
    bool isPowerOfTwo (int x)
    {
        /* First x in the below expression is
        for the case when x is 0 */
        return x && (!(x&(x-1)));
    }
```

12) C++11 has in built algorithms for following:
```c++
    // are all of the elements positive?
    all_of(first, first+n, ispositive());

    // is there at least one positive element?
    any_of(first, first+n, ispositive());

    // are none of the elements positive?
    none_of(first, first+n, ispositive());
```
Please refer Array algorithms in C++ STL (all_of, any_of, none_of, copy_n and itoa) for details.

14) The Iota Algorithm The algorithm iota() creates a range of sequentially increasing values, as if by assigning an initial value to *first, then incrementing that value using prefix ++. In the following listing, iota() assigns the consecutive values {10, 11, 12, 13, 14} to the array arr, and {‘a’, ‘b’, ‘c’} to the char array c[].
```c++
    int a[5] = {0};
    char c[3] = {0};

    // changes a to {10, 11, 12, 13, 14}
    iota(a, a+5, 10);
    iota(c, c+3, 'a'); // {'a', 'b', 'c'}
```
Please refer Array algorithms in C++ STL (all_of, any_of, none_of, copy_n and itoa) for details.

15) Initialization in Binary form: In C++ 11 assignments can also be made in binary form.
```c++
    // C++ code to demonstrate working of
    // "binary" numbers
    #include<iostream>
    using namespace std;
    int main()
    {
        auto number = 0b011;
        cout << number;
        return 0;
    }
```

# scanf tricks
from https://www.cprogramming.com/tips/tip/the-power-of-scanf
```cpp
    scanf("%*[^\n]\n", NULL);
    // skip the first line

    char a[100]
    scanf("%[^\n]\n", a);
    // it means read until you meet '\n', then trash that '\n'

    canf("%[^,]", a);
    // this one doesn't trash the coma

    scanf("%[^,],",a);
    // this one trashes the coma

    scanf("%s %s", temp, last_name);
    // typical answer, using 1 temporary variable

    scanf("%s", last_name);
    scanf("%s", last_name);
    // another answer, only use 1 variable, but calls scanf twice

    scanf("%*s %s", last);
    // best answer, because you don't need extra temporary variable nor calling scanf twice
```
consider using fgets and sscanf rather than just scanf itself

# type and scanf and printf
short,      at least 16 bits
int,        at least 16 bits
long,       at least 32 bits
long long,  at least 64 bits

float, 32 bits
double, 64 bits

16 bits, +- 3.27*10^4  0~6.55*10^4
32 bits, +- 2.14*10^9 0~4.29*10^9
64 bits, +- 9.22*10^18 0~1.84*10^19

scanf reference here: http://www.cplusplus.com/reference/cstdio/scanf/?kw=scanf
%*[width][length]specifier

about fast input, here: https://www.geeksforgeeks.org/fast-io-for-competitive-programming/
```cpp
#include <bits/stdc++.h>
    template<typename T> void scan(T &x)
    {
        x = 0;
        bool neg = 0;
        register T c = getchar();

        if (c == '-')
            neg = 1, c = getchar();

        while ((c < 48) || (c > 57))
            c = getchar();

        for ( ; c < 48||c > 57 ; c = getchar());

        for ( ; c > 47 && c < 58; c = getchar() )
            x= (x << 3) + ( x << 1 ) + ( c & 15 );

        if (neg) x *= -1;
    }

    template<typename T> void print(T n)
    {
        bool neg = 0;

        if (n < 0)
            n *= -1, neg = 1;

        char snum[65];
        int i = 0;
        do
        {
            snum[i++] = n % 10 + '0';
            n /= 10;
        }

        while (n);
        --i;

        if (neg)
            putchar('-');

        while (i >= 0)
            putchar(snum[i--]);

        putchar('\n');
    }

    // Driver Program
    int main()
    {
        int value;

        // Taking input
        scan(value);

        // Printing output
        print(value);
        return 0;
    }
```


## learning Cpp stream to deal with ACM input and output
from the C++ Standard Library - a tutorial and reference

from a good article online: http://acm.timus.ru/help.aspx?topic=cpp&locale=en
this is online Judge System
choose between standard(scanf, printf) or stream(cin, cout), stream is much slower
example of reading to the end of a stream
```cpp
#include <stdio.h>
    ...
    // numbers
    int n;
    while (scanf("%d", &n) != EOF)
    {
           ...
    }
    // lines
    char line[1000];
    while (gets(line))
    {
           ...
    }
    // characters
    int c;
    while ((c = getchar()) != EOF)
    {
           ...
    }
```
```cpp
#include <iostream>
    ...
    // numbers
    int n;
    while (std::cin >> n)
    {
           ...
    }
    // lines
    std::string line;
    while (std::getline(std::cin, line))
    {
           ...
    }
    // characters
    char c;
    while (std::cin.get(c))
    {
           ...
    }
```

from https://www.quora.com/Which-is-the-best-way-to-read-multiple-line-inputs-in-algorithmic-programming-contests-in-C++
case 1: given the number of integers on each line
```cpp
    int n, k, tmp;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                // replace "tmp" with something else
                // or assign the value of "tmp" to whatever variables you want to
                scanf("%d", &tmp);
            }
    }
```
a common case of data
```txt
N  K
n1  a_1 a_2 ... a_n1
n2  b_1 b_2 ... b_n2
...
n_N <n_N more ints>
```
simple handle
```cpp
    // excuse me for my bad code quality here, but this is how in practice
    // I wrote solutions for competitive programming; my teammates are
    // (were) used to it and did very similar (maybe less worse) things.
    int N; scanf("%d", &N); while (N--) {
        int n; scanf("%d", &n); while (n--) {
            int x; scanf("%d", &x); // handle "x" however you like
        }
    }
```

case 2: various number of integers
could use string and stringstream to deal with various number of characters, numbers, tokens and etc.
```cpp
    // TODO: exam doc
    stringstream ss; string line, obj;
    getline(cin, line);
    ss<<line;
    while(ss>>obj){
        // do some crazy stuff
    }
```
or go C style
```cpp
#include <cstdio>
    char buffer[1000000];  // A large enough buffer
    int add, x;

    int main() {
        int n; gets(buffer); sscanf(buffer, "%d", &n); while (n--) {
            gets(buffer);
            for (int s = 0; sscanf(buffer + s, "%d%n", &x, &add) != EOF; s += add) {
                // %n the number of character read so far, doesn't consume characters
                printf("<%d>", x);
            }
            puts(""); // one addtional new line characters
        }
    }
```

using this for competitive program
using stdin or inputFile for test, we could do it in several ways:
- using copy-and-paste, NO
- using FILE* if = fopen("inputFile", "r"); fscanf(if, "format", &value);
- using redirection in command line, and using scanf and printf to files
- using freopen as following
```c++
    // stdin and stdout is also FILE * type
    freopen("input_filename", "r", stdin);
    freopen("output_filename", "w", stdout);
```

#### useful <cstdio> functions
char* gets(char* str) is deprecated by c++11
char* fgets(char* str, int num, FILE* stream)
int ungetc(int character, FILE* stream)


int scanf(const char* format, ...) like call fscanf(stdin, format, ...)
int fscanf(FILE* stream, const char* format, ...)
int sscanf(const char* s, const char* format, ...)

int fseek(FILE* stream, long int offset, int origin)
long int ftell(FILE* stream)
int fsetpos(FILE* stream, fpos_t* pos) // a good way to put mark in stream
int fgetpos(FILE* stream, fpos_t* pos)
void rewind(FILE* stream)

// handle binary file
size_t fread(void* ptr, size_t size, size_t count, FILE* stream)

void perror(const char * str)

here: https://cses.fi/book/book.pdf
luck to find this book
