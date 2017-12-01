#include<stdio.h>
#include<pthread.h>

#define MAX_NUM 1024


pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

char array[MAX_NUM] = {0, 0};
int count = 0;

void* handle_input(){
    pthread_mutex_lock(&m);

    scanf("%s", array);
    // while(scanf("%c", &array[count++]));

    pthread_mutex_unlock(&m);
    return NULL;
}

void* handle_output(){
    pthread_mutex_lock(&m);

    // for(int i=0; i<=count; ++i)
        // printf("%c", array[i]);
    printf("%s", array);
    printf("\n");

    pthread_mutex_unlock(&m);
    return NULL;
}

int main(){
    pthread_t tid1, tid2;
    pthread_create(&tid1, NULL, handle_input, NULL);
    pthread_create(&tid2, NULL, handle_output, NULL);

    // wait for both threads to finish
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    // printf("ARRRRG sum is %d\n", sum);
    return 0;
}
