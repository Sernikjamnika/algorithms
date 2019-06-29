#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <sys/time.h>


struct Node{
    struct Node *before;
    struct Node *after;
    int value;
};

struct CycleList{
    struct Node *head;
    int size;
};

struct CycleList newLinkedList(){
    return (struct CycleList){NULL, 0};
}

_Bool isEmpty(struct CycleList c){
    if(c.head == NULL){
        return 1;
    }
    return 0;
}

void enqueue(struct CycleList *c, int value){
    struct Node* newNode = (struct Node*) malloc(sizeof (struct Node));
    newNode -> value = value;
    if(isEmpty((*c))){
        c -> head = newNode;
        c -> head -> before = newNode;
    }
    //before new node is previous tail
    newNode -> before = c -> head -> before;
    //tail changes what stands after it
    c -> head -> before -> after = newNode;
    //before head there is new tail
    c -> head -> before = newNode;
    //after new node there is a head
    newNode -> after = c -> head;
    //before head there is new tail
    c -> head -> before = newNode;
    
    c -> size++;
}

int dequeue(struct CycleList *c){
    if(!isEmpty(*c)){
        int value = c -> head -> value;
        struct Node *tmp = c -> head;
        if(c -> size != 1){
            c -> head = tmp -> after;
            c -> head -> before = tmp -> before;
            tmp -> before -> after = c -> head;
        }
        else{
            c -> head = NULL;
        }
        c -> size--;
        free(tmp);
        return value;
    }
    printf("CycleList is already empty\n");
    return -1;
}

struct CycleList merge(struct CycleList l1, struct CycleList l2){
    struct CycleList tmp = {NULL, 0};
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

int getElement(struct CycleList c, int position){
    struct Node *tmp = c.head;
    if(position >= 0 && position < (c.size / 2)){
        for(int i = 0; i <= position; i++){
            tmp = tmp -> after;
        }
        return tmp -> value;
    }
    else if(position >= 0 && position < c.size){
        position = c.size - position - 1;
        for(int i = 0; i <= position; i++){
            tmp = tmp -> before;
        }
        return tmp -> value;
    }
    printf("Position out of range\n");
    return -1;
}

int findElement(struct CycleList c, int value){
    struct Node *tmp = c.head;
    for(int i = 0; i < c.size; i++){
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
    
    struct CycleList cycleList = newLinkedList();
    struct CycleList cycleList1 = newLinkedList();
    struct CycleList cycleList3 = newLinkedList();

    for(int i = 0; i < 1000; i++){
        enqueue(&cycleList3, rand()%1000);
    }

    clock_t time;
    time = clock();
    getElement(cycleList3, 0);
    time = clock() - time;
    printf("Runtime[s]: %f\n", ((double)time)/CLOCKS_PER_SEC);

    int variable = rand()%1000;
    time = clock();
    getElement(cycleList3, variable);
    time = clock() - time;
    printf("Runtime[s] %d: %f\n", variable, ((double)time)/CLOCKS_PER_SEC);
    
    enqueue(&cycleList, 1);
    enqueue(&cycleList, 4);
    enqueue(&cycleList, 7);
    enqueue(&cycleList1, 12);
    enqueue(&cycleList1, 43);
    enqueue(&cycleList1, 74);


    struct CycleList cycleList2 = merge(cycleList, cycleList1);
    struct Node *tmp = cycleList2.head;
    int help = cycleList2.size;
    for(int i = 0; i < help; i++){
        printf("%d\n", tmp -> value);
        tmp = tmp -> after;
    }
    printf("Value of tail:%d\nValue of head: %d\nValue of second to last: %d\n", cycleList2.head->before->value, cycleList2.head->value, cycleList2.head->before->before->value);
    // printf("Element at position 0: %d\n", getElement(CycleList2, 0));
    printf("Position of element 12: %d\n", findElement(cycleList2, 12));

    help = cycleList.size;
    for(int i = 0; i < help; i++){
        printf("%d ", dequeue(&cycleList));
    }
    if(isEmpty(cycleList)){
        printf("\nYes its empty\n");
    }


    return 0;
}