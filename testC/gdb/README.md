from the 100-gdb-tips
## chx debug running process
where is sleep define in GNU C and LLVM C
pthread_create have issue on remote.cs.binghamton.edu
```bash
    [wli100@remote02 gdb]$ gcc test.c
    test.c: In function 'thread_func':
    test.c:7:9: warning: implicit declaration of function 'sleep'
    [-Wimplicit-function-declaration]
    sleep(10);
    ^~~~~
    /tmp/ccwv8nV1.o: In function `main':
    test.c:(.text+0x48): undefined reference to `pthread_create'
    test.c:(.text+0x63): undefined reference to `pthread_create'
    collect2: error: ld returned 1 exit status
```
gdb program <processID>
gdb program -p <processID>

if don't like looking for PID each time, using
```shell
    # save as sgdb.sh
    # use: xgdb.sh a
    prog_bin=$1
    running_name=$(basename $prog_bin)
    pid=$(/sbin/pidof $running_name)
    gdb attach $pid
```

debug running process
```gdb
    gdb -q a.out
    attach <pid>
    bt
    detach <pid>
```

debug child process
```gdb
set follow-fork-mode child
set detach-on-fork off
# meanding debug two process at the same, when debug one,
# the other suspend
```
