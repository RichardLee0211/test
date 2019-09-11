profermance profile
================================================================================

this is a well write blog
from: http://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/

this would be a important analysis tool for HPC

```shell
#!/bin/bash

# build the program with profiling support (-gp)
g++ -std=c++11 -pg cpuload.cpp -o cpuload

# run the program; generates the profiling data file (gmon.out)
./cpuload

# print the callgraph
gprof cpuload
```

```shell
#!/bin/bash

# build the program (no special flags are needed)
g++ -std=c++11 cpuload.cpp -o cpuload

# run the program with callgrind; generates a file callgrind.out.12345 that can be viewed with kcachegrind
valgrind --tool=callgrind ./cpuload

# open profile.callgrind with kcachegrind
kcachegrind profile.callgrind
```
