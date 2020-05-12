// from https://www.spoj.com/problems/INTEST/
// Enormous input test, pretty basic
// scanf and printf use .44 sec, cin and cout use 2.17 sec
#include<cstdio>

int main(){
#if 0
#endif
    long long n, d, count{0};
    scanf("%lld %lld\n", &n, &d);
    while(n--){
        long long temp;
        scanf("%lld", &temp);
        if(temp % d == 0)
            ++count;
    }
    printf("%lld\n", count);
}
