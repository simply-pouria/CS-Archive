#include <stdio.h>
int main() {
    int n, i;
    long long fact = 1;
    scanf("%d", &n);
    for(i = 1; i <= n; i++) {
        fact *= i;
    }
    printf("%lld", fact);
    return 0;
}
