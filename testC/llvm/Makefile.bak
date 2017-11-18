LLVM_CONFIG?=llvm-config

ifndef VERBOSE
	QUIET:=@
endif

CXX:=g++
SRC_DIR?=$(PWD)

LDFLAGS+=$(shell $(LLVM_CONFIG) --ldflags)
COMMON_FLAGS=-Wall -Wextra
CXXFLAGS+=$(COMMON_FLAGS) $(shell $(LLVM_CONFIG) --cxxflags)
CPPFLAGS+=$(shell $(LLVM_CONFIG) --cppflags) -I$(SRC_DIR)

TARGET:=helloworld
OBJ:=hello.o mysource.o

# TODO: g++ -I/usr/local/llvm/llvm-5.0/include/ -L/usr/local/llvm/llvm-5.0/lib -lLLVMBitWriter mysource.cpp
# report error
# include "llvm/Bitcode/ReaderWriter.h"

all: $(TARGET)

%.o : $(SRC_DIR)/%.cpp
	@echo Compiling $*.cpp
	$(QUIET)$(CXX) -c $(CPPFLAGS) $(CXXFLAGS) $<

$(TARGET) : $(OBJ)
	@echo Linking $@
	$(QUIET)$(CXX) -o $@ $(CXXFLAGS) $^ `$(LLVM_CONFIG) --libs bitreader core support` $(LDFLAGS)

clean:
	@echo deleteing ...
	$(QUIET)rm -f $(TARGET) $(OBJ)
	@echo deleted

Others:
	clang -c -emit-llvm mysource.c -o mysource.bc
	helloworld mysouce.bc
