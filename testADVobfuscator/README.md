# this is note of ADVobfucator

example/DetectDebugger
when debugger with mac, string disappear
```cpp
    OBFUSCATED_CALL_P0(DetectDebugger, ImportantFunctionInTheApplication);
```

example/ObfuscatedCalls
no surprise, but what this do to the original code??
```cpp
    OBFUSCATED_CALL0(FunctionToProtect);
    auto result = OBFUSCATED_CALL_RET(int, FunctionToProtectWithParameters, OBFUSCATED("did"), OBFUSCATED("again"));
```

example/ObfuscatedStrings
what does this code do ??

TODO: ??using objdump -disassemble <objectname>
