#ifndef QUEUE_H
#define QUEUE_H

// Structs
typedef struct LinkedNode{
    int data;
    struct LinkedNode* next;
} LinkedNode;

typedef struct {
    LinkedNode* front;
    LinkedNode* rear;
    int size;
} Queue;


// Function Declarations
Queue* create_queue();
void enqueue(Queue* queue, int data);
int dequeue(Queue* queue);
int peek(Queue* queue);
void destroy_queue(Queue* queue);

#endif