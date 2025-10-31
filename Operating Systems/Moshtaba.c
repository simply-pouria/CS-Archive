#include <stdio.h>

void moshtaba_print(const int *arr, int size);
void moshtaba_reverse(const int *arr, int size);

int main(void) {
    int arr[100];
    int size;
    if (scanf("%d", &size) != 1) return 0;

    const int *p_in = arr;         
    for (int i = 0; i < size; i++) {
        scanf("%d", (int *)p_in);
        p_in = p_in + 1;
    }

    moshtaba_print(arr, size);
    moshtaba_reverse(arr, size);

    return 0;
}

void moshtaba_print(const int *arr, int size)
{
    const int *p = arr;
    printf("The Array is:   ");
    for (int i = 0; i < size; i++) {
        printf("%d ", *p);
        p = p + 1;
    }
    printf("\n");
}

void moshtaba_reverse(const int *arr, int size)
{
    if (size <= 0) {
        printf("Its reverse is:\n");
        return;
    }

    const int *p = arr + (size - 1);
    printf("Its reverse is: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", *p);
        p = p - 1;
    }
    printf("\n");
}
