#include <stdio.h>
int main() {
    int a, b, c, max, x, y;
    scanf("%d%d%d", &a, &b, &c);
    max = a;
    if(b > max) max = b;
    if(c > max) max = c;
    if(max == a) { x = b; y = c; }
    else if(max == b) { x = a; y = c; }
    else { x = a; y = b; }
    if(max * max == x * x + y * y) printf("YES");
    else printf("NO");
    return 0;
}
