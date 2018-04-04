this is form xv6-book-rev6, learning about system programming
learning GNU C system programming, system call

## ch0 operating system interfaces
### process and memory
    fork()
    exit()
    wait()
### file descriptors
    read(...)
    wirte(...)
    open(...)
    close(...)
### pipes
    int p[2];
    pipe(p);
    // by default, p[0] is the read end, p[1] is the write end
    dup(...)
### file system
    chdir(...)
```C
    chdir("/a");
    chdir("b");
    open("c", O_RDONLY);
    open("/a/b/c", O_RDONLY);

    mkdir("/dir");
    fd = open("/dir/file", O_CREATE|O_WRONLY);
    close(fd);
    mknod("/console", 1, 1); // device file

    open("a", O_CREATE|O_WRONLY);
    link("a", "b"); // link system call
    unlink("a");

    fd = open("/tmp/xyz", O_CREATE|O_RDWR);
    unlink("/tmp/xyz"); // idiomatic way to create a temporary inode
```

## ch1 the first process

## ch2 traps, interrupts, and dirvers

## ch3 locking
     Typically, an operation’s correct behavior depends on the invariants being true
     when the operation begins. The operation may temporarily violate the invariants
     but must reestablish them before finishing.
```c
    struct list{
        int data;
        struct list *next;
    };
    struct list *list = 0;
    void
    insert(int data){
        struct list *l;

        l = malloc(sizeof *l);
        l->data = data;
        l->next = list;
        list = l;
    }
```
