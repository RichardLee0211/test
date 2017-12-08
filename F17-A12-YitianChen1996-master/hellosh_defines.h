#ifndef header
#define header

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
//#include <sys/types.h>
//#include <sys/wait.h>
#include <dirent.h>
#include <fcntl.h>

#define CMD_MAX_LEN 1024

typedef enum state_t_ {
    inWord,
    inSpace
} state_t;

typedef enum cmd_type_t_ {
    normal,
    in_redir,
    out_redir,
    both_in_redir,
    mypipe
} cmd_type_t;

void split_cmd(char *cmd, char **cmd1, char **cmd2);

void parse_cmd_nopipe(char **args, char *cmd);

void parse_cmd_pipe(char **args1, char **args2, char *cmd);

int count_argnum_nopipe(char *cmd);

void count_argnum_pipe(char *cmd, int *argnum1, int *argnum2);

cmd_type_t get_cmd_type(char *cmd);

void getFileName(char *line, char *filename, char type);

#endif