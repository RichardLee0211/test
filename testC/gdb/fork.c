#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>

int main(){
    pid_t pid;
    pid = fork();
    if(pid<0)
        exit(1);
    else if (pid > 0)
        exit(0);
    printf("hello world\n");
    return 0;
}
