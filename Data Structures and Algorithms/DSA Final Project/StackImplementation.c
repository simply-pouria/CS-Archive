// Pouria Moradpour 40240323040 - Project 1

# include <stdio.h>

//structs
typedef struct Node {
    int* data;
    struct Node* next;    // Pointer to next node
    struct Node* prev;    // Pointer to previous node
} Node;

typedef struct {
    Node* head;           // Points to the first node
    int size;             // Number of elements in list
    void (*free_data)(void*);  // Function to free data
} CircularList;

// operations declaration
void insert_head(CircularList *circular_list, int insert_value);

void insert_tail(CircularList *circular_list, int insert_value);

void delete_node(CircularList *circular_list, int delete_value);

void search(CircularList *circular_list, int search_value);

void print_list(CircularList *circular_list)

// driver code
int main() {

    return 0;
}

// operations definition









