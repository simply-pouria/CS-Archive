#include <stdio.h>

long long power(long long base, int exp) {
    long long result = 1;
    for(int i = 0; i < exp; i++) result *= base;
    return result;
}

long long fact(int n) {
    long long f = 1;
    for(int i = 1; i <= n; i++) f *= i;
    return f;
}

long long comb(int n, int k) {
    return fact(n) / (fact(k) * fact(n - k));
}

int main() {
    long long a, x, sum = 0;
    int n;
    scanf("%lld %lld %d", &a, &x, &n);
    for(int k = 0; k <= n; k++) {
        sum += comb(n, k) * power(x, k) * power(a, n - k);
    }
    printf("%lld", sum);
    return 0;
}






