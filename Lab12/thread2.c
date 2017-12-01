#include<stdio.h>
#include<pthread.h>

/* create a mutex this ready to be locked! */
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

int sum = 0;

void* count(void* param){
    int i;

    /* same thread that locks the mutex must unlock it */

    pthread_mutex_lock(&m);

    // other threads that call lock will ahve to wait until we call unlock
    for(i=0; i<1000000; i++){
        sum+=1;
    }

    pthread_mutex_unlock(&m);

    return NULL;
}

int main(){
    pthread_t tid1, tid2;
    pthread_create(&tid1, NULL, count, NULL);
    pthread_create(&tid2, NULL, count, NULL);

    // wait for both threads to finish
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    printf("ARRRRG sum is %d\n", sum);
    return 0;
}
