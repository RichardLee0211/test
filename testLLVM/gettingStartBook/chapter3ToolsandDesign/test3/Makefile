LLVM_PATH=/usr/local/llvm/llvm-3.4-apple
LLVM_BIN=$(LLVM_PATH)/bin

all: link

llvm-link:
	llvm-link main.bc sum.bc -o sum.linked.o
	llc -filetype=obj sum.linked.bc -o sum.linked.o
	clang sum.linked.o -o sum

link: bit
	$(LLVM_BIN)/llc -filetype=obj main.bc -o main.o
	$(LLVM_BIN)/llc -filetype=obj sum.bc -o sum.o
	clang main.o sum.o -o sum

bit:
	clang -emit-llvm -c main.c -o main.bc
	clang -emit-llvm -c sum.c -o sum.bc

assem:
	clang -emit-llvm -S main.c -o main.ll
	clang -emit-llvm -S sum.c -o sum.ll

one-step:
	clang main.c sum.c -o sum

clean:
	rm -rf *.bc *.ll
