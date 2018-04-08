#include<unistd.h>
#include<stdlib.h>

struct list{
    int data;
    struct list *next;
};

struct list *list = 0;
struct lock listlock;
void acquire(struct spinlock *lk){
    for(;;){
        if(!lk->locked){
            lk->locked = 1;
            break;
        }
    }
}

void
insert(int data){
    struct list *l;

    acquire(&listlock);
    l = malloc(sizeof *l);
    l->data = data;
    l->next = list;
    list = l;
    release(&listlock);
}

int main(){
    write(1, "what ??\n", 8);
    write(1, "what ??\n", sizeof(short));
}
