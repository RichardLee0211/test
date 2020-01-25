Beej's Guide to Unix IPC
================================================================================

code: http://beej.us/guide/bgipc/examples/

use wget to download a directory
```shell
    wget --recursive --no-parent -R "index.html*" http://...
```

2. A fork() Primer
--------------------------------------------------------------------------------
the author likes to talk

3. Signal
--------------------------------------------------------------------------------

ENGLISH: The burning question remains: how do you catch a speeding SIGTERM?

ENGLISH: excusable use of goto

TODO: async-safe, thread-safe, type-safe

4. Pipes
--------------------------------------------------------------------------------

ENGLISH: File descriptors are simply ints that are analogous to FILE*'s in stdio.h.

ENGLISH: Not very glamorous, but no one ever said computer science would be the X-Files, Mulder.

ENGLISH: well, you're probably right. The other forms of IPC are generally more useful and are often more exotic.

5. FIFOs
--------------------------------------------------------------------------------

TODO:
- errno.h
- fcntl.h
- sys/types.h
- sys/stat.h
- unistd.h

6. File Locking
--------------------------------------------------------------------------------

ENGLISH: whence

ENGLISH: Practically, though, you will probably mostly be using write locks to guarantee exclusive access to a file for a short amount of time while it's being updated;

ENGLISH: This document describes the usage and functionality of the extremely groovy System V Message Queues!

I think I got the essential
