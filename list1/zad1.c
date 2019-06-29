#include<stdio.h>
#include<stdlib.h>


struct Node{
    struct Node *after;
    int value;
};

struct Fifo{
    struct Node *head;
    struct Node *tail;
    int size;
};

_Bool isEmpty(struct Fifo f){
    if(f.head == NULL){
        return 1;
    }
    return 0;
}

void enqueue(struct Fifo *f, int value){
    struct Node* newNode = (struct Node*) malloc(sizeof (struct Node));
    newNode -> value = value;
    if(isEmpty((*f))){
        f -> head = newNode;
    }
    else{
        f -> tail -> after = newNode;
    }
    f -> tail = newNode;
    f -> size++;
}

int dequeue(struct Fifo *f){
    if(!isEmpty(*f)){
        int value = f -> head -> value;
        struct Node *tmp = f -> head;
        f -> head = tmp -> after;
        f -> size--;
        if(isEmpty((*f))){
            f -> tail = NULL;
        }
        free(tmp);
        return value;
    }
    printf("List is already empty\n");
    return -1;
}


int main(){

    struct Fifo fifo = {NULL, NULL, 0};
    struct Fifo fifo1 = {NULL, NULL, 0};
    enqueue(&fifo, 1);
    enqueue(&fifo, 4);
    enqueue(&fifo, 7);
    enqueue(&fifo1, 12);
    enqueue(&fifo1, 43);
    enqueue(&fifo1, 74);
    
    struct Node *tmp = fifo.head;
    int help = fifo.size;
    for(int i = 0; i < help; i++){
        printf("%d ", dequeue(&fifo));
    }

    int value = dequeue(&fifo);
    if(isEmpty(fifo)){
        printf("Yes its empty\n");
    }
    dequeue(&fifo);
    dequeue(&fifo);
    if(isEmpty(fifo)){
        printf("Yes its empty\n");
    }
    return 0;
}