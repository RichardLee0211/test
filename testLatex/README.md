learning latex

install mactex as compiler
--------------------------------------------------------------------------------
from: https://thetechsolo.wordpress.com/2016/01/28/latex-on-mac-the-easy-way/

surprisely, mactex is over 1 GB, and brew cask is needed
and since mactex is the only popular choice for mac OS

here: http://tug.org/mactex/
```bash
    brew cask install mactex
    brew cask install texmaker # latex editor
```

output: straghgy, ask for passwd and don't response any more
```bash
    wnloading https://homebrew.bintray.com/bottles/little-cms2-2.9.high_sierra.bottle.1.tar.gz
######################################################################## 100.0%
    ==> Pouring little-cms2-2.9.high_sierra.bottle.1.tar.gz
    🍺  /usr/local/Cellar/little-cms2/2.9: 18 files, 1MB
    ==> Installing ghostscript
    ==> Downloading https://homebrew.bintray.com/bottles/ghostscript-9.23.high_sierra.bottle.tar.gz
######################################################################## 100.0%
    ==> Pouring ghostscript-9.23.high_sierra.bottle.tar.gz
    🍺  /usr/local/Cellar/ghostscript/9.23: 679 files, 64.3MB
    ==> Downloading http://mirror.ctan.org/systems/mac/mactex/mactex-20170524.pkg
######################################################################## 100.0%
    ==> Verifying checksum for Cask mactex
    ==> Installing Cask mactex
    ==> Running installer for mactex; your password may be necessary.
    ==> Package installers may write to any location; options such as --appdir are ignored.
    Password:







    abcd
    ^C
    RichardLeedeMacBook-Air% brew cask install mactex
    Updating Homebrew...
    ==> Auto-updated Homebrew!
```

runing reinstall and no response again.

yes, there is response but extra slow.

when brew's script encounter a problem, it stops.

couldn't uninstall neither
```cpp
    way way to slow
    exit
    ^C==> chmod: /usr/local/texlive/2017/texmf-dist/doc/latex/concprog: No such file or directory
    Error: Command failed to execute!

    ==> Failed command:
    /usr/bin/sudo -E -- /bin/chmod -- 755 /usr/local/texlive/2017/texmf-dist/doc/latex/concprog

    ==> Standard Output of failed command:


    ==> Standard Error of failed command:
    chmod: /usr/local/texlive/2017/texmf-dist/doc/latex/concprog: No such file or directory


    ==> Exit status of failed command:
#<Process::Status: pid 509 exit 1>
```

### install Mactex via downloading the package, more than 5GB is occupied
including
 - bibdesk, the bible manager
 - latexIt, have no idea what's it for
 - tex live utility, look like the page manager for latex

!! seting PATH in bashrc file is stupid idea, install mactex will change PATH, but
bashrc set it back. using add, don't edit the original PATH

maybe sharelatex.com is good option

here, using mactex via command line, I'm lack of patient
https://tex.stackexchange.com/questions/142554/command-line-pdflatex-vs-texshop

tutorial
--------------------------------------------------------------------------------

from: http://www.tug.org.in/tutorials.html

can't visit this, the indian Tex user Group: http://sarovar.org/projects/pstricks/

one happy thing is that remote have latex installed

what happened when type "latex on remote"
```bash
    [wli100@remote06 testLatex]$ ls
    README.md  test1.tex  test2.tex
    [wli100@remote06 testLatex]$ latex test2.tex
    This is pdfTeX, Version 3.14159265-2.6-1.40.17 (TeX Live 2016/Debian) (preloaded format=latex)
     restricted \write18 enabled.
     entering extended mode
     (./test2.tex
     LaTeX2e <2017/01/01> patch level 3
     Babel <3.9r> and hyphenation patterns for 83 language(s) loaded.

     ! LaTeX Error: File `tutorial.cls' not found.

     Type X to quit or <RETURN> to proceed,
     or enter new name. (Default extension: cls)

     Enter file name:
     ! Emergency stop.
     <read *>

     l.2 \pagestyle
                   {heading}^^M
                   No pages of output.
                   Transcript written on test2.log.
```

xdvi in ssh: remote
```bash
    [wli100@remote06 testLatex]$ xdvi
    perl: warning: Setting locale failed.
    perl: warning: Please check that your locale settings:
            LANGUAGE = (unset),
            LC_ALL = (unset),
            LC_CTYPE = "zh_CN.UTF-8",
            LANG = "en_US.UTF-8"
            are supported and installed on your system.
    perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
    Error: Can't open display:
```

log
================================================================================

pdftex is a different program with pdflatex

vim-llp seems doesn't work, this plugin:
https://github.com/xuhdev/vim-latex-live-preview

but I can do
:!pdflatex test1.tex
and open manually

so cool, YCM seems to have to latex autocomplete

like HTML, why do I need to learn Latex.
for drawing UML and write design document

but it pays too much just to draw that picture, like uml2.tex.
and it requires different package from the 5 GB install of mactex

while, I find "what you see is what you get" is a good way to do art work.
just word doesn't do well in compatibility and stable in macOS.

log2
================================================================================

following the book from IndiaTexUserGroup
now, I come back again, with my new macbook pro

pdflatex: aim to ascii pdf
xelatex: aim to utf-8, language compatibility
lualatex: add lua script to system

ch3 introduction to Latex
--------------------------------------------------------------------------------
```latex
    % class: article, book, report, letter, report, article
    % options: fontSize, paperSize, pageFormat
    % 10pt, [letterpaper, legalpaper, executivepaper], one column, two column
    \documentclass[options]{class}
```

A LATEX document has broadly three parts viz., frontmatter, mainmatter and backmatter.

ch4 Lists, etc.
--------------------------------------------------------------------------------
see in the .tex file, nothing so surprise me

### 4.2 displayed text

ch5. several kinds of boxes
--------------------------------------------------------------------------------
some config have preview effect of latex, but I don't like it, I can't even see the whole code. I need it when I'm not familiar with syntax

## ch6. Floats

about vim
now, I am search through my vimrc to exam the quick fix window. feel like I am lose control of this feature
I set let g:syntastic_auto_loc_list=0 to stop automatically show up, I don't think it's doing any help
and here: https://stackoverflow.com/questions/3262037/how-to-quit-vim-quickfix
:cclose # close the quick fix window
:copen  # open the quick fix window
:cnext or :cn # next error
:cprevious or :cp # previous error
