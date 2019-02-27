Using LaTeX to write a PhD Thesis
================================================================================

first impression, this is experience LaTeX writer

ch01 Introduction
--------------------------------------------------------------------------------

ENGLISH: Ancient buggy code that's 20 years out-of-date festers in university departments refusing to die.

ENGLISH: let's LaTeX our documents

ch02 Getting started
--------------------------------------------------------------------------------

ENGLISH: for very little effort it can produce a document serveral pages long,
which can give you a sense of achievement that can help give you suffient momentum to get started

```latex
\documentclass[oneside, 12pt,parskip=full]{scrbook}
% a blank line between paragraphs and no paragraph indentation
\usepackage[margin=1in]{geometry}

```

ch02 Formatting
--------------------------------------------------------------------------------

```latex
\usepackage{scrpage2}
\pagestyle{scrheadings}
\newcommand{\myregnum}{123456789}% registration number
\ihead{}
\chead{}
\ohead[]{\headmark}
\ifoot[\myregnum]{\myregnum}% registration number
\cfoot[]{}
\ofoot[\pagemark]{\pagemark}
```

where to put \ihead{} etc ?: put them in the preamble

ENGLISH:
Despite the current digital age, many people still use hand-written annotations on
manuscripts. It’s unlikely that your examiners have pens that are incompatible with your paper.

ENGLISH:
It is not usually appropriate to have reams of listings in your thesis. It can
annoy an examiner if you have included every single piece of code you have written
during your PhD, as it comes across as padding to make it look as though your
thesis is a lot larger than it really is. (Examiners are not easily fooled, and
it’s best not to irritate them as it is likely to make them less sympathetic towards
you.) If you want to include listings in your thesis, check with your supervisor
rst to  nd out whether or not it is appropriate.

ch03 Generating a Bibliography
--------------------------------------------------------------------------------
using bibtex now, problem solved

ch04 Generating Indexes and Glossaries
--------------------------------------------------------------------------------

this is like the end of writing work, save for later

the only way to get things done is to get started.
