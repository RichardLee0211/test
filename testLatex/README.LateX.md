log
================================================================================
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

#### using Nerd Font in LaTeX
in LaTeX, mainly use Nerd Font for icons
1. search, download and install a Nerd Font of choice from: nerdfonts.com
    MacOS: font book is convinient
    Debian: fc-cache, fc-list, fc-match
2. Nerd Font Cheat sheet from: https://www.nerdfonts.com/cheat-sheet
    or use Font Book like program to show icons
3. in main.tex
like fontawesome.sty from: http://fortawesome.github.com/Font-Awesome/
```LaTeX
    \newfontfamily{\Term}{TerminessTTF Nerd Font} %
    % then use like this
    {\Term\symbol{"F50E}} %   , if it shows up, Nerd Font is installed, otherwise, it isn't.
```

some interesting icons:
nf-fa-space_shuttle     F197    
nf-fa-terminal          F120    
nf-fae-biohazard        E286    
nf-fae-radioactive      E238    
nf-fae-virus            E214    

nf-weather-alien        E36E    
nf-weather-aliens       E345    
nf-fa-user_secret       F21B    
nf-oct-gist_secret      F46C    
nf-mdi-robot            FBA7    ﮧ
nf-linux-redhat         F316    
nf-mdi-clippy           F64E    
nf-mdi-cow              F699    
nf-mdi-incognite        FAF8    﫸
nf-mdi-language_go      FCD1    ﳑ
nf-mdi-minecraft        F872    
nf-mdi-ninja            FC72    ﱲ
nf-mdi-owl              F8D1    
nf-mdi-panda            F8D9    
nf-mdi-skull            FB8A    ﮊ
nf-dev-gun              E779    
nf-dev-grunt            E74C    
nf-dev-prolog           E7A1    

nf-mdi-webhook          FB2E    אַ
nf-dev-atom             E764    
nf-dev-codeigniter      E780    

nf-mdi-power_socket     F926    臘
nf-mdi-power_socket_eu  FCE5    ﳥ
nf-mdi-power_socket_uk  FCE6    ﳦ
nf-mdi-power_socket_us  FCE7    ﳧ

something weird
nf-mdi-delta            F6C1    
nf-mdi-details          F6C5    


LateX.pdf from en.wikibooks.org in June 18, 2016
================================================================================

God, I need to thanks wikibook, this is a nice document

PART I Getting Started
--------------------------------------------------------------------------------

ch1 intro
--------------------------------------------------------------------------------

ch2 installation
--------------------------------------------------------------------------------

ch3 installing extra packages
--------------------------------------------------------------------------------

ch4 basics
--------------------------------------------------------------------------------

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

PART II Common Elements
--------------------------------------------------------------------------------

ch5 Document Structure
--------------------------------------------------------------------------------

at this point, leave vimtex plugin alone, because not many things to record

ch6 Text Format
--------------------------------------------------------------------------------

### 6.1 spacing
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

ch7 Paragraph Formatting
--------------------------------------------------------------------------------

now, feeling like this is a reference, but not a tutorial

ch8 colors
--------------------------------------------------------------------------------

ch9 fonts
--------------------------------------------------------------------------------

ch10 List structure
--------------------------------------------------------------------------------

ch11 special characters
--------------------------------------------------------------------------------

\textless and \textgreater
preserve characters: & % $ # _ { } ~ ^ \
```latex
    \documentclass{article}
    \begin{document}

        \& \% \$ \# \_ \{ \}
        \textasciitilde % ~
        \textasciicircum % ^
        \textbackslash % \

    \end{document}
```

ch12 Internationalization
--------------------------------------------------------------------------------
this is not in my concern

ch13 Rotation
--------------------------------------------------------------------------------

ch14 tables
--------------------------------------------------------------------------------
maybe right now I am not so interested in tables

ch15 title creation
--------------------------------------------------------------------------------

ch16 Page layout
--------------------------------------------------------------------------------
better header in ch16.7 page style

ch17 Importing Graphics
--------------------------------------------------------------------------------

ch18 Floats, Figures and Captions
--------------------------------------------------------------------------------
TODO: to be continue, at ch18.2. heading to new area, data analysis

PART III Mechanics
--------------------------------------------------------------------------------

ch22 Errors and warning
--------------------------------------------------------------------------------
feel like I need to know more about latex to make my assignment perfect

PART IV Technical Texts
--------------------------------------------------------------------------------

ch27 Mathematics
--------------------------------------------------------------------------------
I am doing homework on algorithm class, and I would like to convert it into a latex document, so I jump to math chapter here

ch28 Advanced Mathematics
--------------------------------------------------------------------------------

ch29 Theorems
--------------------------------------------------------------------------------

ch30 chemical graphics
--------------------------------------------------------------------------------

ch31 algorithm
--------------------------------------------------------------------------------

ch32 source code Listings
--------------------------------------------------------------------------------

ch38 Bibliography Management
--------------------------------------------------------------------------------

ENGLISH: If it were totally manual, then adding or removing a reference would be a real chore, as you would have to

ch55 Modular Document
--------------------------------------------------------------------------------
writing a book, .sty file

### 38.3 BibTeX

Good tool

@article{greenwade93,
    author = "George D. Greenwade",
    title = "The {C}omprehensive {T}ex {A}rchive {N}etwork ({CTAN})",
    year = "1993",
    journal = "TUGBoat",
    volume  = "14",
    number  = "3",
    pages   = "342--351"
}

TODO: vim-LaTeX plugin
