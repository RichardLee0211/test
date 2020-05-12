add_executable(main main.c)

INCLUDE_DIRECTORIES(/tmp/test/include/hello)

LINK_DIRECTORIES(/tmp/test/lib)
TARGET_LINK_LIBRARIES(main libhello.so)
