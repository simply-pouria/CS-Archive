#include <stdio.h>
int main() {
    long long n, m, a, b, gcd, lcm;
    scanf("%lld %lld", &n, &m);
    a = n;
    b = m;
    while(b != 0) {
        long long t = b;
        b = a % b;
        a = t;
    }
    gcd = a;
    lcm = (n / gcd) * m;
    printf("%lld %lld", gcd, lcm);
    return 0;
}
