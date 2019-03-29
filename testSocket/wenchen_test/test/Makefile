all:
	g++ testServer.cpp -o testServer
	g++ testClient.cpp -o testClient

server:
	./testServer 8888

client:
	./testClient 10.0.5.18 8888 "the message to travel"
