#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>

pthread_mutex_t mutex;	// ���廥������ȫ�ֱ���


void *client_process(void *arg)
{
	int recv_len = 0;
	char recv_buf[1024] = "";	// ���ջ�����
	int connfd = *(int *)arg; // ���������������׽���

	// ������pthread_mutex_lock()���ѣ�������
	pthread_mutex_unlock(&mutex);

	// ��������
	while((recv_len = recv(connfd, recv_buf, sizeof(recv_buf), 0)) > 0)
	{
		printf("recv_buf: %s\n", recv_buf); // ��ӡ����
		send(connfd, recv_buf, recv_len, 0); // ���ͻ��˻�����
	}

	printf("client closed!\n");
	close(connfd);	//�ر��������׽���

	return 	NULL;
}

int main(int argc, char *argv[])
{
	int sockfd = 0;				// �׽���
	int connfd = 0;
	int err_log = 0;
	struct sockaddr_in my_addr;	// ��������ַ�ṹ��
	unsigned short port = 8080; // �����˿�
	pthread_t thread_id;

	pthread_mutex_init(&mutex, NULL); // ��ʼ����������������Ĭ���Ǵ򿪵�

	printf("TCP Server Started at port %d!\n", port);

	sockfd = socket(AF_INET, SOCK_STREAM, 0);   // ����TCP�׽���
	if(sockfd < 0)
	{
		perror("socket error");
		exit(-1);
	}

	bzero(&my_addr, sizeof(my_addr));	   // ��ʼ����������ַ
	my_addr.sin_family = AF_INET;
	my_addr.sin_port   = htons(port);
	my_addr.sin_addr.s_addr = htonl(INADDR_ANY);


	printf("Binding server to port %d\n", port);

	// ��
	err_log = bind(sockfd, (struct sockaddr*)&my_addr, sizeof(my_addr));
	if(err_log != 0)
	{
		perror("bind");
		close(sockfd);
		exit(-1);
	}

	// �������׽��ֱ䱻��
	err_log = listen(sockfd, 10);
	if( err_log != 0)
	{
		perror("listen");
		close(sockfd);
		exit(-1);
	}
	printf("Waiting client...\n");

	while(1)
	{
		char cli_ip[INET_ADDRSTRLEN] = "";	   // ���ڱ���ͻ���IP��ַ
		struct sockaddr_in client_addr;		   // ���ڱ���ͻ��˵�ַ
		socklen_t cliaddr_len = sizeof(client_addr);

		// ��������û�н���֮ǰ��pthread_mutex_lock()������
		pthread_mutex_lock(&mutex);

		//���һ���Ѿ�����������
		connfd = accept(sockfd, (struct sockaddr*)&client_addr, &cliaddr_len);
		if(connfd < 0)
		{
			perror("accept this time");
			continue;
		}

		// ��ӡ�ͻ��˵� ip �Ͷ˿�
		inet_ntop(AF_INET, &client_addr.sin_addr, cli_ip, INET_ADDRSTRLEN);
		printf("----------------------------------------------\n");
		printf("client ip=%s,port=%d\n", cli_ip,ntohs(client_addr.sin_port));

		if(connfd > 0)
		{
			//���ص��������Ĳ�����&connfd����ַ����
			pthread_create(&thread_id, NULL, (void *)client_process, (void *)&connfd);  //�����߳�
			pthread_detach(thread_id); // �̷߳��룬����ʱ�Զ�������Դ
		}
	}

	close(sockfd);

	return 0;
}
