#include <stdio.h>
#include "queue.h"

int n = 6;
int coins[7] = {0, 5, 1, 2, 10, 6, 2};

Queue* max_queue = NULL;

int max_save(int i);

int main() {


    max_queue = create_queue();
    enqueue(max_queue, coins[0]);
    enqueue(max_queue, coins[1]);

    printf( "The Chosen Coins Are:\n");
    printf("Coin %d\n", coins[1]);

    for (int i=2; i <= n; i++) {
        int i_max = max_save(i);
        if (i_max != peek(max_queue)) {
            printf("Coin %d\n", coins[i]);
        };
        enqueue(max_queue, i_max);
    };

    dequeue(max_queue);
    int max = dequeue(max_queue);
    printf("The Maximum is: %d\n", max);
    return 0;
};

int max_save(int i) {
    int f_2 = dequeue(max_queue);
    int f_1 = peek(max_queue);
    printf("this is i: %d\n", i);
    printf("f_1 = %d   f_2 = %d\n", f_1, f_2);

    if (coins[i] + f_2 >= f_1) {
        return coins[i] + f_2;
    } else {
        return f_1;
    };
};
