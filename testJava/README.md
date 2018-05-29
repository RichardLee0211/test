here, I started with C++, and have a stronge flavor of C++ programming
but I will take design pattern and architecture, so learn a little bit of java

trying to build working environment, using command line and vim
not a big fan of eclipse

from http://www.codejava.net/java-core/tools/using-javac-command
javac:
- Use the flag -classpath (or -cp) to tell the compiler where to look for external libraries
        by default, the compiler is looking in bootstrap classpath and in CLASSPATH environment variable
- Use the -d directory option to specify where the compiler puts the generated .class files.
- We can tell the compiler where to search for the source files by using the -sourcepath directory option.
- We can tell the compiler which Java version applied for the source file, by using the -source release option.
- The compiler can generate the .class files for a specific VM version. Using the -target release option we can do this
- The compiler can compile source files which are related to the specified one, and it does that silently. So using the -verbose option can tell us what the compiler is doing
```bash
    javac -cp lib1.jar;lib2.jar;lib3.jar MyProgram.java
    javac -d classes MyProgram.java
    javac -sourcepath src MyProgram.java
    javac -source 1.5 MyProgram.java
    javac -target 1.6 -source 1.5 MyProgram.java
    javac -verbose MyProgram.java
```

useful java sites: http://www.javapractices.com/topic/TopicAction.do?Id=243

code java with vim:
- [x] NerdTree - A file explorer sidebar
- [x] Taglist - tag (symbol) navigation sidebar. This allows you to jump to methods, classes, and member variables.
        using with vim command Tlist...
- [x] Ctags - I'm guessing that this is a dependency for taglist.
- [ ] Eclim - It enables Eclipse to run in headless mode which makes it act like a server. Vim will then connect to this server to query it for completions and refactorings. If you're going to use this, you don't need a separate build tool. Otherwise, use ant.
        curious about it, but worried about disk usage

clear my mac disk and find my system resourse is 50G, and some cache file like
like macTex, useless valgrind-on mac, and useless Haskel platform after CS571
this software is handy
here: https://www.omnigroup.com/more/
I'm real consider remove xcode, I don't do the macOS app coding right now

it's so annoying that install java eclipse, along with git client, although I
could use git command line... speekless

what do I need for my working space?
- auto-complete
- syntax static check
- one move build tool

TODO: here, this blog may do the work: https://spacevim.org/use-vim-as-a-java-ide/

## others
does java have shared library??
here, read latter: https://www.ibm.com/support/knowledgecenter/en/SSMKHH_10.0.0/com.ibm.etools.mft.doc/bc23072_.htm
and the magic GNI to link .so and java, not sure it's a good idea
