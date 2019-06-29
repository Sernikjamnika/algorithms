#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <sys/time.h>


struct Node{
    struct Node *before;
    struct Node *after;
    int value;
};

struct LinkedList{
    struct Node *head;
    struct Node *tail;
    int size;
};

struct LinkedList newLinkedList(){
    return (struct LinkedList){NULL, NULL, 0};
}

_Bool isEmpty(struct LinkedList l){
    if(l.head == NULL){
        return 1;
    }
    return 0;
}

void enqueue(struct LinkedList *l, int value){
    struct Node* newNode = (struct Node*) malloc(sizeof (struct Node));
    newNode -> value = value;
    if(isEmpty((*l))){
        l -> head = newNode;
        printf("%ls", (int*)l->head);
    }
    else{
        newNode -> before = l->tail;
        l -> tail -> after = newNode;
    }
    l -> tail = newNode;
    l -> size++;
}

int dequeue(struct LinkedList *l){
    if(!isEmpty(*l)){
        int value = l -> head -> value;
        struct Node *tmp = l -> head;
        l -> head = tmp -> after;
        l -> size--;
        if(isEmpty((*l))){
            l -> tail = NULL;
        }
        else{
            tmp -> after -> before = NULL;
        }
        free(tmp);
        return value;
    }
    printf("List is already empty\n");
    return -1;
}

struct LinkedList merge(struct LinkedList l1, struct LinkedList l2){
    struct LinkedList tmp = {NULL, NULL, 0};
    struct Node *help;

    help = l1.head;
    for(int i = 0; i < l1.size; i++)
    {
        enqueue(&tmp, help->value);
        help = help -> after;
    }

    help = l2.head;
    for(int i = 0; i < l2.size; i++)
    {
        enqueue(&tmp, help->value);
        help = help -> after;
    }

    return tmp;
}

int getElement(struct LinkedList l, int position){
    struct Node *tmp = l.head;
    if(position < l.size){
        for(int i = 0; i <= position; i++){
            tmp = tmp -> after;
        }
        return tmp -> value;
    }
    printf("Position out of range\n");
    return -1;
}

int findElement(struct LinkedList l, int value){
    struct Node *tmp = l.head;
    for(int i = 0; i < l.size; i++){
        if(tmp -> value == value){
            return i;
        }
        tmp = tmp -> after;
    }
    printf("No such an element\n");
    return -1;
}

int main(){
    srand(time(NULL));
    
    struct LinkedList linkedList = newLinkedList();
    struct LinkedList linkedList1 = newLinkedList();
    struct LinkedList linkedList3 = newLinkedList();

    for(int i = 0; i < 1000; i++){
        enqueue(&linkedList3, rand()%1000);
    }

    clock_t time;
    time = clock();
    getElement(linkedList3, 213);
    time = clock() - time;
    printf("Runtime[s]: %f\n", ((double)time)/CLOCKS_PER_SEC);

    time = clock();
    getElement(linkedList3, rand()%1000);
    time = clock() - time;
    printf("Runtime[s]: %f\n", ((double)time)/CLOCKS_PER_SEC);
    
    enqueue(&linkedList, 1);
    enqueue(&linkedList, 4);
    enqueue(&linkedList, 7);
    enqueue(&linkedList1, 12);
    enqueue(&linkedList1, 43);
    enqueue(&linkedList1, 74);


    struct LinkedList linkedList2 = merge(linkedList, linkedList1);
    struct Node *tmp = linkedList2.head;
    int help = linkedList2.size;
    for(int i = 0; i < help; i++){
        printf("%d\n", tmp -> value);
        tmp = tmp -> after;
    }
    printf("Value of tail:%d\nValue of head: %d\nValue of second to last: %d\n", linkedList2.tail->value, linkedList2.head->value, linkedList2.tail->before->value);
    printf("Element at position 0: %d\n", getElement(linkedList2, 0));
    printf("Position of element 7: %d\n", findElement(linkedList2, 7));

    help = linkedList.size;
    for(int i = 0; i < help; i++){
        dequeue(&linkedList);
    }

    if(isEmpty(linkedList)){
        printf("Yes its empty\n");
    }


    return 0;
}
