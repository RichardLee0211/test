#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
int main(int argc, char *argv[])
{
	unsigned short port = 8080;        		// �������Ķ˿ں�
	char *server_ip = "10.221.20.24";    	// ������ip��ַ
	
	if( argc > 1 )		//�������Σ����Ը��ķ�������ip��ַ									
	{		
		server_ip = argv[1];
	}	
	if( argc > 2 )	   //�������Σ����Ը��ķ������Ķ˿ں�									
	{
		port = atoi(argv[2]);
	}

	int sockfd;
	sockfd = socket(AF_INET, SOCK_STREAM, 0);// ����ͨ�Ŷ˵㣺�׽���
	if(sockfd < 0)
	{
		perror("socket");
		exit(-1);
	}
	
	// ���÷�������ַ�ṹ��
	struct sockaddr_in server_addr;
	bzero(&server_addr,sizeof(server_addr)); // ��ʼ����������ַ
	server_addr.sin_family = AF_INET;	// IPv4
	server_addr.sin_port = htons(port);	// �˿�
	//inet_pton(AF_INET, server_ip, &server_addr.sin_addr);	// ip
	server_addr.sin_addr.s_addr = inet_addr(server_ip);//��inet_pton�ȼ�
	
	 // �������ӷ�����
	int err_log = connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr));     
	if(err_log != 0)
	{
		perror("connect");
		close(sockfd);
		exit(-1);
	}
	
	
	printf("send data to %s:%d\n",server_ip,port);
	
	char send_buf[512] = "this is send data";
	printf("send data \"%s \" to %s:%d\n",send_buf,server_ip,port);
	send(sockfd, send_buf, strlen(send_buf), 0);   // �������������Ϣ
	
	char recv_buf[512] = {0};
	recv(sockfd, recv_buf, sizeof(send_buf), 0); // ��������
	printf("%s\n", recv_buf);

	close(sockfd);
	
	return 0;
}
