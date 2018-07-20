for now, the purpose of the learning latex is redo my resume
and to do it, I only need to know:
- [ ] using sans serif family
- [x] align of words, \hfill
- [ ] line, underline
- [ ] bold
- [ ] lists, reduce the line space
- [ ] left and right margin
- [ ]
- [ ]
- [ ]
this README is following LateX.pdf from en.wikibooks.org in June 18, 2016
# ch1 intro
# ch2 installation
# ch3 installing extra packages
# ch4 basics
```tex
    \documentclass{article}
    \begin{document}
    Hello world !
    \end{document}
```

multiply comment
```tex
    \usepackage{verbatim}

    This is another
    \begin{comment}
    rather stupid,
    but helpful
    \end{comment}
    example for embedding
    comment in your document
```

# ch5 Document Structure
at this point, leave vimtex plugin alone
not many things to record

# ch6 Text Format
## 6.1 spacing
switch command \singlespacing
environment \begin{singlespace} \end{singlespace}

here, text-alignment: https://www.sharelatex.com/learn/Text_alignment
raggedright, match left alignment

Alignment    Environment    Switch command      ragged2e environment    ragged2e switch command
Left         flushleft      \raggedright        FlushLeft               \RaggedRight
Right        flushright     \raggedleft         FlushRight              \RaggedLeft
Centre       center         \centering          Center                  \Centering
Fully justified  N/A        N/A                 justify                 \justify

\noindent % cancel the indent of this paragraph

# ch7 Paragraph Formatting
now, feeling like this is a reference, but not a tutorial

# ch8 colors
# ch9 fonts
# ch10 List structure

# ch11 special characters
\textless and \textgreater

# ch12 Internationalization
this is not in my concer

# ch13 Rotation

# ch14 tables
maybe right now I am not so interested in tables

# ch15 title creation

# ch16 Page layout
better header in ch16.7 page style

# ch17 Importing Graphics

# ch18 Floats, Figures and Captions
TODO: to be continue, at ch18.2. heading to new area, data analysis
