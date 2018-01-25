when using opt standalone tool in LLVM, it would be useless to optimize the .bc file because I cann't actually see the changes that opt made.
maybe I can do it with .ll file, to look at the IR code
``` zsh
➜  chapter5IR git:(master) ✗ opt -load=fnarg.so -fnargcnt < sum.bc > /dev/null
Error opening 'fnarg.so': dlopen(fnarg.so, 9): Symbol not found: __ZN4llvm12FunctionPass17assignPassManagerERNS_7PMStackENS_15PassManagerTypeE
  Referenced from: fnarg.so
  Expected in: flat namespace
 in fnarg.so
  -load request ignored.
opt: Unknown command line argument '-fnargcnt'.  Try: 'opt -help'
opt: Did you mean '-march'?
```
