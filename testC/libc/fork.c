#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//os includes
#include <sys/types.h>
#include <unistd.h>
#define fatal printf

typedef struct
{
	int index;
	pid_t pid;
	int p2cPipe[2];
	int c2pPipe[2];
	int read;
	int write;
}Worker;

void setUpPipe(Worker * worker){
	if (worker->pid == 0)
	{
		if (close(worker->p2cPipe[1])!=0)
		{
			fatal("worker close p2cPipe[1] error");
		}
		if (close(worker->c2pPipe[0])!=0)
		{
			fatal("worker close c2pPipe[0] error");
		}
		worker->read = worker->p2cPipe[0];
		worker->write = worker->c2pPipe[1];

	}else{
		if (close(worker->p2cPipe[0])!=0)
		{
			fatal("manager close p2cPipe[0] error");
		}
		if (close(worker->c2pPipe[1])!=0)
		{
			fatal("manager c2pPipe[1] error");
		}
		worker->read = worker->c2pPipe[0];
		worker->write = worker->p2cPipe[1];

	}
}

Worker * createWorker(int index){
	Worker * worker = (Worker *)malloc(sizeof(Worker));
	worker->index = index;
	pipe(worker->p2cPipe);
	pipe(worker->c2pPipe);
	worker->pid = fork();
	setUpPipe(worker);
	return worker;

}

Worker * cleanWorker(Worker * worker){
	if (worker!=NULL)
	{
		close(worker->read);
		close(worker->write);
		free(worker);
	}
	return NULL;
}

// int main(int argc, char const *argv[])
int main()
{
	char text[][32] = {
		"hello world1",
		"hello world2",
		"hello world3",
		"hello world4",
		"hello world5",
		"hello world6",
		"hello world7",
		"hello world8"};
	Worker * worker[8];
	Worker * cur;
	for (int i = 0; i < 2; ++i)
	{
		cur = createWorker(i);
		worker[i] = cur;
		if (cur->pid==0)
		{
			for (int j = 0; j < i; ++j)
			{
				cleanWorker(worker[j]);
			}
			break;
		}
		if (i==2-1)
		{
			cur=NULL;
		}
	}
	if (cur==NULL)
	{
		for (int i = 0; i < 8; ++i)
		{
			int wr = write(worker[i%2]->write,text[i],strlen(text[i]));
			printf("wr:%d p write: %s\n",worker[i%2]->index, text[i]);
			fflush(stdout);
		}
		exit(0);
	}else if (cur->pid == 0)
	{
		char buff[1024];
		int i = 20;
		int rd;
		while(rd = read(cur->read,buff,12) && i-->0){
			buff[12] = '\0';
			printf("c:%d, rd:%d read: %s\n", cur->index, rd,buff);
			fflush(stdout);
		}
		exit(0);
		//printf("c read: %s\n", buff);
		//int rd =  read(cur->read,buff,1024);

	}
	return 0;
}
