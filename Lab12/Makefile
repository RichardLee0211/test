CXX := gcc

all: thread

thread: thread.c thread2.c thread3.c
	$(CXX) thread.c -o thread -pthread
	$(CXX) thread2.c -o thread2 -pthread
	$(CXX) thread3.c -o thread3 -pthread

clean:
	rm -rf thread thread2 thread3
