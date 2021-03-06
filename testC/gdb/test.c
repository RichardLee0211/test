/* compile with -pthread */
#include<stdio.h>
#include<pthread.h>

void *thread_func(void *p_arg){
    while(1){
        printf("%s\n", (char*)p_arg);
        sleep(2);
    }
}

int main(void){
    pthread_t t1, t2;

    pthread_create(&t1, NULL, thread_func, "Thread 1");
    pthread_create(&t2, NULL, thread_func, "Thread 2");

    while(1){
        printf("delay\n");
        sleep(10);
    }
    return 0;
}
