#include "hellosh_defines.h"

void split_cmd(char *cmd, char **cmd1, char **cmd2) {
    char *p;
    *cmd2 = strchr(cmd, '|') + 1;
    while (**cmd2 == ' ') {
        (*cmd2)++;
    }
    p = strchr(cmd, '|') - 1;
    while (*p == ' ') {
        p--;
    }
    p++;
    *p = '\0';
    *cmd1 = cmd;
}

int count_argnum_nopipe(char *cmd) {
    int cnt;
    state_t state;
    char *p = cmd;
    while (*p == ' ') {
        p++;
    }
    state = inWord;
    cnt = 1;
    while (*p != '\0') {
        if (*p == '>' || *p == '<' || *p == '|') {
            break;
        }
        if (*p == ' ' && state == inWord) {
            state = inSpace;
        } else if (*p != ' ' && state == inSpace) {
            state = inWord;
            cnt++;
        }
        p++;
    }
    return cnt;
}

void count_argnum_pipe(char *cmd, int *argnum1, int *argnum2) {
    char *cmd1, *cmd2;
    split_cmd(cmd, &cmd1, &cmd2);
    *argnum1 = count_argnum_nopipe(cmd1);
    *argnum2 = count_argnum_nopipe(cmd2);
}

cmd_type_t get_cmd_type(char *line) {
    char *p = line;
    cmd_type_t cmd_type = normal;
    while (*p != '\0') {
        if (*p == '>' && cmd_type == in_redir) {
            cmd_type = both_in_redir;
        } else if (*p == '>' && cmd_type == normal) {
            cmd_type = out_redir;
        } else if (*p == '<' && cmd_type == out_redir) {
            cmd_type = both_in_redir;
        } else if (*p == '<' && cmd_type == normal) {
            cmd_type = in_redir;
        } else if (*p == '|') {
            cmd_type = mypipe;
        }
        p++;
    }
    return cmd_type;
}

void getFileName(char *line, char *filename, char type) {
    char *p1 = line;
    p1 = strchr(line, type) + 1;
    while (*p1 == ' ') {
        p1++;
    }
    char *p2 = p1;
    p2 = strchr(p1, ' ');
    int i = 0;
    for (char *c = p1; c != p2 && *c != '\0'; c++, i++) {
        filename[i] = *c;
    }
    filename[i] = '\0';
}

void parse_cmd_nopipe(char **args, char *cmd) {
    char *p1, *p2;
    int cur_argsnum = 0;
    p1 = cmd;
    while (*p1 == ' ') {
        p1++;
    }
    while (1) {
        p2 = strchr(p1, ' ');
        if (p2 == NULL || *p2 == '\0') {
            break;
        }
        int i = 0;
        char *c;
        for (c = p1, i = 0; c != p2; i++, c++) {
            args[cur_argsnum][i] = *c;
        }
        cur_argsnum++;
        p1 = p2 + 1;
        while (*p1 == ' ') {
            p1++;
        }
        if (*p1 == '>' || *p1 == '<' || *p1 == '|') {
            break;
        }
    }
    int i;
    char *c;
    if (*p1 != ' ' && *p1 != '>' && *p1 != '<' && *p1 != '|') {
        for (c = p1, i = 0; *c != '\0'; i++, c++) {
            args[cur_argsnum][i] = *c;
        }
    }
    cur_argsnum++;
    args[cur_argsnum] = NULL;
}

void parse_cmd_pipe(char **args1, char **args2, char *cmd) {
    char *cmd1, *cmd2;
    split_cmd(cmd, &cmd1, &cmd2);
    parse_cmd_nopipe(args1, cmd1);
    parse_cmd_nopipe(args2, cmd2);
}
