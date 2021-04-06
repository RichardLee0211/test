cmake_minimum_required(VERSION 3.8)
SET(cmake_install_prefix /tmp/t2/usr)

project(HELLO)
add_subdirectory(src bin)
# add_subdirectory(src)

install(FILES COPYRIGHT README DESTINATION share/doc/cmake/t2)
install(PROGRAMS runhello.sh DESTINATION bin)
install(DIRECTORY doc/ DESTINATION share/doc/cmake/t2)





# SET(SRC_LIST main.c)
# MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})
# MESSAGE(STATUS "This is SOURCE dir " ${HELLO_SOURCE_DIR})
# compile and like main.c into the executable file
# ADD_EXECUTABLE(hello ${SRC_LIST})


# the most easy version
# PROJECT (HELLO)
# ADD_EXECUTABLE(hello main.c)
