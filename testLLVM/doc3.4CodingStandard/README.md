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
