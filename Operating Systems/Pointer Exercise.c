#include <stdio.h>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    int *p = numbers;
    *p = 15;
    *(p + 1) = 25;

    printf("%d\n", *p);
    printf("%d\n", *(p + 1));
    printf("%d\n", *(p + 3));
    printf("%d\n", *(p + 4));

    return 0;
}

