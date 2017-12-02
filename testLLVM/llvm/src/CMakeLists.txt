SET(SRC_LIST mysource.cpp)

# set complier and flags
# SET(CMAKE_CXX_COMPILER "clang++")
# SET(CMAKE_CXX_FLAGS "-std=c++11 -stdlib=libc++ -Werror -Weverything -Wno-deprecated-declarations -Wno-disabled-macro-expansion -Wno-float-equal -Wno-c++98-compat -Wno-c++98-compat-pedantic -Wno-global-constructors -Wno-exit-time-destructors -Wno-missing-prototypes -Wno-padded -Wno-old-style-cast")
# SET(CMAKE_EXE_LINKER_FLAGS "-lc++ -lc++abi")
SET(CMAKE_BUILD_TYPE Debug)
# INCLUDE_DIRECTORIES(/usr/local/llvm/llvm-3.4-apple/include)
# TARGET_LINK_LIBRARIES(main )

# code from https://releases.llvm.org/3.2/docs/CMake.html
find_package(LLVM)

if( NOT LLVM_FOUND )
  message(FATAL_ERROR "LLVM package can't be found. Set CMAKE_PREFIX_PATH variable to LLVM's installation prefix.")
endif()

include_directories( ${LLVM_INCLUDE_DIRS} )
link_directories( ${LLVM_LIBRARY_DIRS} )

llvm_map_components_to_libraries(REQ_LLVM_LIBRARIES jit native)

target_link_libraries(mycompiler ${REQ_LLVM_LIBRARIES})

ADD_EXECUTABLE(main ${SRC_LIST})
