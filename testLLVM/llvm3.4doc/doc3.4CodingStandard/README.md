note come from 3.4 doc, coding stand

```c++
//===-- llvm/Instruction.h - Instruction class definition -------*- C++ -*-===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
///
/// \file
/// \brief This file contains the declaration of the Instruction class, which is
/// the base class for all of the VM instructions.
///
//===----------------------------------------------------------------------===//
```

```
/// \brief Does foo and bar.
///
/// Does not do foo the usual way if \p Baz is true.
///
/// Typical usage:
/// \code
///   fooBar(false, "quux", Res);
/// \endcode
///
/// \param Quux kind of foo to do.
/// \param [out] Result filled with bar sequence on foo success.
///
/// \returns true on success.
bool fooBar(bool Baz, StringRef Quux, std::vector<int> &Result);

// In Something.h:

/// \brief An abstraction for some complicated thing.
class Something {
    public:
    /// \brief Does foo and bar.
    void fooBar();
};

// In Something.cpp:

// Builds a B-tree in order to do foo.  See paper by...
void Something::fooBar() { ... }
```

## Use Early Exits and continue to Simplify Code

## Assert Liberally
```cpp
inline Value *getOperand(unsigned I) {
    assert(I < Operands.size() && "getOperand() out of range!");
    return Operands[I];
}

```

With C++11, we can mark methods that won’t be implemented with = delete.

We prefer to put a space before an open parenthesis only in control flowstatements,
but not in normal function call expressions and function-likemacros.
For example, this is good:
```cpp
if (X) ...
for (I = 0; I != 100; ++I) ...
while (LLVMRocks) ...

somefunc(42);
assert(3 != 4 && "laws of math are failing me");
A = foo(42, 92) + bar(X);
```
