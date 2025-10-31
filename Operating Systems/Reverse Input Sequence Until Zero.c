#include <stdio.h>
int main() {
    int a[1000], n = 0, x;
    while(1) {
        scanf("%d", &x);
        if(x == 0) break;
        a[n++] = x;
    }
    for(int i = n - 1; i >= 0; i--) {
        printf("%d\n", a[i]);
    }
    return 0;
}
