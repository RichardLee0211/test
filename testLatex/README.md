learning latex

## install mactex as compiler
from: https://thetechsolo.wordpress.com/2016/01/28/latex-on-mac-the-easy-way/
surprisely, mactex is over 1 GB, and brew cask is needed
and since mactex is the only popular choice for mac OS
here: http://tug.org/mactex/
```bash
    brew cask install mactex
    brew cask install texmaker # latex editor
```
output: straigy, ask for passwd and don't response any more
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
runing reinstall and no response again
yes, there is response but extra slow
when brew's script encounter a problem, it stops
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

##
from: http://www.tug.org.in/tutorials.html

one happy thing is that remote have latex installed
