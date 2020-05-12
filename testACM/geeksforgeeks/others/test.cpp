#include<iostream>
#include<cmath>
#include <cstdio>
#include<ctime>
#include<cstdlib>

int main(){
#if 0
    // what's in the end of char array
    int A[]{-1, -2, 1, 2, 3};
    char C[] {'c', 'h', 'a', 'r'};
    for(int i{0}; C[i]; i++){
        printf("%c\t", C[i]);
    }
    printf("%d", C[4]); // warning, but print 0
#endif
#if 0
    // get the mostSignificantBit
    double N{32345.64};
    double K = log10(N);
    K = K - (int)K;
    int mostSignificantBit = pow(10, K);
    printf("%d", mostSignificantBit);
#endif
#if 0
    // skip the first line
    // printf("%d", 0b0011+0b0011);
    scanf("%*[^\n]\n", NULL);
    int a;
    scanf("%d", &a);
    printf("%d", a);
#endif

#if 0
    freopen("input_sum.txt", "r", stdin);
    // input test, get sum of each line, various number of integer
    char buffer[1000000];  // A large enough buffer
    int add, x;
    scanf("%*[^\n]\n", NULL); // skip the first line
    int n; gets(buffer); sscanf(buffer, "%d", &n); while (n--) {
        gets(buffer);
        unsigned long long sum{0};
        for (int s = 0; sscanf(buffer + s, "%d%n", &x, &add) != EOF; s += add) {
            // %n the number of character read so far, doesn't consume characters
            // printf("<%d>", x);
            sum += x;
        }
        printf("sum: %llu\n", sum);
        puts(""); // one addtional new line characters
    }
#endif
#if 0
    // generate random number
    int n{6};
    srand(time(NULL));
    while(n--)
        printf("%d ", rand()%10);
#endif
}
