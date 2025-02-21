#include <stdio.h>
#include "queue.h"

int n = 6;
int coins[7] = {0, 5, 1, 2, 10, 6, 2};
int chosen[6];

Queue* max_queue = NULL;
int counter = 0;

int max_save(int i);
int add_to_array(int arr[], int value);

int main() {

    max_queue = create_queue();
    enqueue(max_queue, coins[0]);
    enqueue(max_queue, coins[1]);

    printf("The Chosen Coins Are:\n");
    for (int i=2; i <= n; i++) {
        int i_max = max_save(i);
        enqueue(max_queue, i_max);
    };

    int max = dequeue(max_queue);
    printf("The Maximum is: %d\n", max);

    return 0;
};


int add_to_array(int arr[], int value) {
    arr[counter] = value;
    return counter++; // Return and then increment
}

int max_save(int i) {
    int f_2 = dequeue(max_queue);
    int f_1 = peek(max_queue);
    if (coins[i] + f_2 > f_1) {
        add_to_array(chosen, coins[i]);
        printf("1. Coin %d", coins[i]);
        return coins[i] + f_2;
    } else {
        return f_1;
    };
};













