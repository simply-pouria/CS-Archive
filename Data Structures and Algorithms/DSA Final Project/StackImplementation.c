#include <stdio.h>
#include <stdlib.h>

// Structs
typedef struct Node {
    int data;
    struct Node* next;    // Pointer to next node
    struct Node* prev;    // Pointer to previous node
} Node;

typedef struct {
    Node* head;          // Points to the first node
    int size;             // Number of elements in list
} CircularList;

// Operations declaration
void insert_head(CircularList* circular_list, int insert_value);
void insert_tail(CircularList* circular_list, int insert_value);
void delete_node(CircularList* circular_list, int delete_value);
void search(CircularList* circular_list, int search_value);
void print_list(CircularList* circular_list);

// Main Driver Code
int main() {
    CircularList circular_list = {NULL, 0}; // Initialize circular list

    // Example from lecture notes, k=2, n=9
    int n = 10;  // Number of people
    int k = 3;  // Step count for elimination
    for (int i = 1; i <= n; i++) {
        insert_tail(&circular_list, i);
    }

    printf("Initial Circle: ");
    print_list(&circular_list);

    // Josephus Problem Simulation
    Node* current = circular_list.head;
    while (circular_list.size > 1) {
        // Traverse k-1 nodes
        for (int count = 1; count < k; count++) {
            current = current->next;
        }

        // Remove the k-th node
        int eliminated = current->data;
        Node* next_node = current->next;  // Save the next node before deletion
        delete_node(&circular_list, eliminated);

        printf("Eliminated: %d\n", eliminated);
        current = next_node;  // Move to the next node
    }

    // Print the survivor
    printf("Survivor: %d\n", circular_list.head->data);

    return 0;
}

// Operations definition

// Function to create a new node
Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    new_node->data = value;
    new_node->next = new_node->prev = NULL; // Initialize next and prev
    return new_node;
}

// Insert at the head
void insert_head(CircularList* circular_list, int insert_value) {
    Node* new_node = create_node(insert_value);

    if (circular_list->head == NULL) {
        new_node->next = new_node->prev = new_node;
        circular_list->head = new_node;
    } else {
        Node* tail = circular_list->head->prev;
        new_node->next = circular_list->head;
        new_node->prev = tail;
        tail->next = new_node;
        circular_list->head->prev = new_node;
        circular_list->head = new_node; // Update head
    }
    circular_list->size++;
}

// Insert at the tail
void insert_tail(CircularList* circular_list, int insert_value) {
    Node* new_node = create_node(insert_value);

    if (circular_list->head == NULL) {
        new_node->next = new_node->prev = new_node;
        circular_list->head = new_node;
    } else {
        Node* tail = circular_list->head->prev; // Tail node
        new_node->next = circular_list->head;
        new_node->prev = tail;
        tail->next = new_node;
        circular_list->head->prev = new_node; // Update tail
    }
    circular_list->size++;
}

// Delete a node by value
void delete_node(CircularList* circular_list, int delete_value) {
    if (circular_list->head == NULL) { // List is empty
        printf("List is empty. Cannot delete.\n");
        return;
    }

    Node* current = circular_list->head;
    do {
        if (current->data == delete_value) {
            if (current->next == current) { // Single node in the list
                circular_list->head = NULL;
            } else {
                current->prev->next = current->next;
                current->next->prev = current->prev;
                if (current == circular_list->head) { // If head is to be deleted
                    circular_list->head = current->next;
                }
            }
            free(current);
            circular_list->size--;
            return;
        }
        current = current->next;
    } while (current != circular_list->head);

    printf("Value %d not found in the list.\n", delete_value);
}

// Search for a value in the list
void search(CircularList* circular_list, int search_value) {
    if (circular_list->head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* current = circular_list->head;
    int position = 0;
    do {
        if (current->data == search_value) {
            printf("Value %d found at position %d.\n", search_value, position);
            return;
        }
        current = current->next;
        position++;
    } while (current != circular_list->head);

    printf("Value %d not found in the list.\n", search_value);
}

// Print the list
void print_list(CircularList* circular_list) {
    if (circular_list->head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* current = circular_list->head;
    printf("Circular List: ");
    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != circular_list->head);
    printf("\n");
}

