#include <stdio.h>
#include <stdlib.h>
#include "queue.h"


Queue* create_queue(){
    Queue* queue = (Queue*)malloc(sizeof(Queue));
    queue->size = 0;
    queue->front = NULL;
    queue->rear = NULL;
    return queue;
};

void enqueue(Queue* queue, int data) {
    LinkedNode* linked_node = (LinkedNode *)malloc(sizeof(LinkedNode));
    linked_node->data = data;
    linked_node->next = NULL;
    if (queue->rear == NULL) {
        queue->rear = queue->front = linked_node;
    }
    else {
        queue->rear->next = linked_node;
        queue->rear = linked_node;
    };
    queue->size ++;

};

int dequeue(Queue* queue) {

    if (queue->front == NULL) {
        printf("queue underflow\n");
        exit(1);
    } else {
        int data = queue->front->data;
        LinkedNode* temp = queue -> front;
        queue->front = queue->front->next;

        if (queue->front == NULL) {
            queue->rear = NULL;
        }

        free(temp);
        queue->size --;
        return data;
    };
};

int is_empty(Queue* q) {
    return (q->front == NULL);
};

int peek(Queue* queue){
    if (is_empty(queue)) {
        printf("queue underflow");
        exit(1);
    } else {
        return queue->front->data;
    }
};

void destroy_queue(Queue* queue){
    LinkedNode* current = queue->front;
    LinkedNode* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    };
    free(queue);
};















