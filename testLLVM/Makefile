# Mac LLVM_SRC_PATH
LLVM_SRC_PATH := /usr/local/llvm/llvm-3.4-apple
# LLVM_SRC_PATH := /usr/local/llvm/llvm-3.4
LLVM_BIN_PATH := $(LLVM_SRC_PATH)/bin

# CXX := g++
CXX := clang++
CXXFLAGS := -fno-rtti -O0 -g

LLVM_INCLUDES := \
	-I$(LLVM_SRC_PATH)/include

LLVM_CXXFLAGS := `$(LLVM_BIN_PATH)/llvm-config --cxxflags`
# LLVM_LDFLAGS := `$(LLVM_BIN_PATH)/llvm-config --ldflags --libs --system-libs`
LLVM_LDFLAGS := `$(LLVM_BIN_PATH)/llvm-config --ldflags --libs `

all: test

test: test.cpp
	$(CXX) $(CXXFLAGS) $(LLVM_CXXFLAGS) $^ $(LLVM_LDFLAGS) -o $@
