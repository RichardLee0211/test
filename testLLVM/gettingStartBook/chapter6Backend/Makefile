## ===========================================
## set variable to LLVM directory
## ========================================
## Mac LLVM_SRC_PATH
LLVM_SRC_PATH := /usr/local/llvm/llvm-3.4-apple
# LLVM_SRC_PATH := /usr/local/llvm/llvm-3.4
LLVM_BIN_PATH := $(LLVM_SRC_PATH)/bin

## ==========================================
## set varible for compiler and its flags
## =========================================
# CXX := g++
CXX := clang++
CXXFLAGS := -fno-rtti -O0 -g

LLVM_INCLUDES := \
	-I$(LLVM_SRC_PATH)/include

# LLVM_CXXFLAGS := `$(LLVM_BIN_PATH)/llvm-config --cxxflags`
# LLVM_LDFLAGS := `$(LLVM_BIN_PATH)/llvm-config --ldflags --libs --system-libs`
LLVM_CXXFLAGS := `$(LLVM_BIN_PATH)/llvm-config --libs bitwriter core support`
LLVM_LDFLAGS := `$(LLVM_BIN_PATH)/llvm-config --ldflags --libs `

all: test

test: IRGenerator.cpp.edit
	$(CXX) $(CXXFLAGS) $(LLVM_CXXFLAGS) $^ $(LLVM_LDFLAGS) -o $@

## ========================================
## standalone of LLVM command
## ========================================
standalone:
	clang sum.c -emit-llvm -c -o sum.bc
	clang sum.c -emit-llvm -S -c -o sum.ll
	llvm-as sum.ll -o sum.bc
	llvm-dis sum.bc -o sum.ll
	llc -march=cpp sum.bc -o sum.cpp
	llc sum.bc -o sum.s
	llc sum.bc -filetype=obj -o sum.o
	llc -march=mips -filetype=obj sum.bc -o sum.o
	llvm-talgen -print-records insns.td
