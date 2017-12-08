#include "hellosh_defines.h"

int main() {
    char line[CMD_MAX_LEN], line1[CMD_MAX_LEN], line2[CMD_MAX_LEN], templine[CMD_MAX_LEN];
    int pid, pid2, argsnum, argsnum1, argsnum2;
    char **args, **args1, **args2;
    char indire_filename[CMD_MAX_LEN], outdire_filename[CMD_MAX_LEN],
        cmd[CMD_MAX_LEN], cmd1[CMD_MAX_LEN], cmd2[CMD_MAX_LEN];

    while (1) {
        printf("Hello!!>");
        memset(indire_filename, 0, sizeof(indire_filename));
        memset(outdire_filename, 0, sizeof(outdire_filename));
        memset(cmd, 0, sizeof(cmd));
        cmd_type_t cmd_type;
        if (!fgets(line, CMD_MAX_LEN - 1, stdin)) {
            break;
        }

        if (strcmp(line, "exit\n") == 0) {
            break;
        }
        line[strlen(line) - 1] = '\0';
        cmd_type = get_cmd_type(line);
        if (cmd_type != mypipe) {
            argsnum = count_argnum_nopipe(line);
            args = (char **)malloc(CMD_MAX_LEN * (sizeof(char *)));
            for (int i = 0; i <= argsnum - 1; i++) {
                args[i] = (char *)malloc(CMD_MAX_LEN * sizeof(char));
                memset(args[i], 0, CMD_MAX_LEN);
            }
            if (cmd_type == in_redir) {
                getFileName(line, indire_filename, '<');
            } else if (cmd_type == out_redir) {
                getFileName(line, outdire_filename, '>');
            } else if (cmd_type == both_in_redir) {
                getFileName(line, indire_filename, '<');
                getFileName(line, outdire_filename, '>');
            }
            parse_cmd_nopipe(args, line);
            strcpy(cmd, args[0]);
        } else {
            strcpy(templine, line);
            count_argnum_pipe(templine, &argsnum1, &argsnum2);
            args1 = (char **)malloc(CMD_MAX_LEN * (sizeof(char *)));
            for (int i = 0; i <= argsnum1 - 1; i++) {
                args1[i] = (char *)malloc(CMD_MAX_LEN * sizeof(char));
                memset(args1[i], 0, CMD_MAX_LEN);
            }
            args2 = (char **)malloc(CMD_MAX_LEN * (sizeof(char *)));
            for (int i = 0; i <= argsnum2 - 1; i++) {
                args2[i] = (char *)malloc(CMD_MAX_LEN * sizeof(char));
                memset(args2[i], 0, CMD_MAX_LEN);
            }
            parse_cmd_pipe(args1, args2, line);
            strcpy(cmd1, args1[0]);
            strcpy(cmd2, args2[0]);
        }

        pid = fork();

        if (pid == 0) {
            int fd1, fd2;
            /* This is the child */
            if (cmd_type == normal) {
                execvp(cmd, args);
            } else if (cmd_type == out_redir) {
                fd1 = open(outdire_filename, O_WRONLY | O_CREAT | O_TRUNC, 0666);
                dup2(fd1, STDOUT_FILENO);
                execvp(cmd, args);
                close(fd1);
            } else if (cmd_type == in_redir) {
                fd2 = open(indire_filename, O_RDONLY);
                dup2(fd2, STDIN_FILENO);
                execvp(cmd, args);
                close(fd2);
            } else if (cmd_type == both_in_redir) {
                fd1 = open(outdire_filename, O_WRONLY | O_CREAT | O_TRUNC, 0666);
                fd2 = open(indire_filename, O_RDONLY);
                dup2(fd1, STDOUT_FILENO);
                dup2(fd2, STDIN_FILENO);
                execvp(cmd, args);
                close(fd1);
                close(fd2);
            } else if (cmd_type == mypipe) {
                pid2 = fork();
                if (pid2 == 0) {
                    fd2 = open("tempfile", O_WRONLY | O_CREAT | O_TRUNC, 0600);
                    dup2(fd2, STDOUT_FILENO);
                    execvp(cmd1, args1);
                } else {
                    waitpid(pid2, NULL, 0);
                    fd1 = open("tempfile", O_RDONLY);
                    dup2(fd1, STDIN_FILENO);
                    execvp(cmd2, args2);
                }
                close(fd1);
                close(fd2);
                break;
            }
            fprintf(stderr, "Hello!!: %s\n", strerror(errno));
            exit(errno);
        } else {
            /* This is the parent */
            wait(NULL);
        }
    }
    return 0;
}