#include <stdio.h>
int main() {
    int n, f1 = 1, f2 = 2, f3, i, j;
    scanf("%d", &n);
    int fib[100] = {0};
    fib[0] = 1;
    fib[1] = 2;
    for(i = 2; ; i++) {
        f3 = fib[i - 1] + fib[i - 2];
        if(f3 > n) break;
        fib[i] = f3;
    }
    for(i = 1; i <= n; i++) {
        int found = 0;
        for(j = 0; fib[j] != 0; j++) {
            if(fib[j] == i) {
                found = 1;
                break;
            }
        }
        if(found) printf("+");
        else printf("-");
    }
    return 0;
}
