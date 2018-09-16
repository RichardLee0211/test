## type mangle
 from: https://gcc.gnu.org/onlinedocs/libstdc++/manual/ext_demangling.html
 Transforming C++ ABI identifiers (like RTTI symbols) into the original C++
 source identifiers is called “demangling.”
 why, it has it's own reason

solution from: https://stackoverflow.com/questions/281818/unmangling-the-result-of-stdtype-infoname

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
