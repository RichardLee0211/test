#include<stdio.h>
#include<pthread.h>

/**
 * each thread could get a different worker function or
 * the same worker function could be used by multiple functions
 */

void* worker_function(void* payload){
    /* thread code goes here */
    printf(" In thread %lx\n", (unsigned long)payload);
    printf("  count++: %d\n", ++*(int*)payload);
    return NULL;
}

#define NUM_THREADS 3

int main(){
    pthread_t threads[NUM_THREADS];
    int i;

    /* Declare payload here */
    int count = 0;
    void* payload = &count;

    for(i=0; i<NUM_THREADS; ++i){
        pthread_create(&threads[i], NULL, worker_function, (void*)payload);
    }

    printf(" In main threab\n");

    for(i=0; i<NUM_THREADS; i++){
        pthread_join(threads[i], NULL);
    }

    printf("Exiting main thread\n");
    return 0;
}
