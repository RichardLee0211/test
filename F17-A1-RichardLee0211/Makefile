# project name and intro
TARGET = Main.out
OBJS =  main.o functions.o
CC = gcc
DEBUG = -g
CFLAGS = -Wall -std=c89 $(DEBUG)
LFLAGS = -Wall -std=c89 $(DEBUG)
# -Wall show warming massage

# Specifiy the target
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(LFLAGS) $(OBJS) -o $(TARGET)

main: main.c
	$(CC) $(CFLAGS) main.c -o main

functions: functions.c function.h
	$(CC) $(CFLAGS) functions.c


clean:
	rm -f *.o $(TARGET)
	# rm -f *.tar.gz


# Rule to build a test executable
# DO NOT MODIFY
test: test.c functions.c
	$(CC) $(CFLAGS) $^ -o $@

# Rule to run a testing script and produce an output file
# DO NOT MODIFY
.PHONY: test-run
test-run: test test.py
	python3 test.py
