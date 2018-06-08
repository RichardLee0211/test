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


#### try spaceVim
exec this command: curl -sLf https://spacevim.org/install.sh | bash
install spaceVim, here https://github.com/SpaceVim/SpaceVim
brew install lua
somehow, maybe I deleted it, install python3
well, need python3 enabled and lua enable to use SpaceVim. I don't wanna risk my vim in Mac
space is just a configuration of vim, I need java auto complete

#### get javacomplete2
install with vundle
add configuration in ~/.vimrc
this one only private little functions

#### Eclim
after all, I still go back to Eclim, since eclipse is the best for java
download and install eclim_2.7.2.bin, it's like a standalone software
has eclipse install in ~/eclipse and Eclim install via Vundle
Eclim install manually via the download pakage and give it position of vim and eclipse
install Eclim according offical website, log here:
```bash
    ➜  Downloads ./eclim_2.7.2.bin
    Welcome to the installer for eclim 2.7.2.

    Please specify the path to your Eclipse.app directory.
    Ex: /Applications/Eclipse.app
    ~/Applications/Eclipse.app
    > /Users/richardlee/eclipse/java-oxygen/
    /Users/richardlee/eclipse/java-oxygen/Eclipse.app/
    > /Users/richardlee/eclipse/java-oxygen/Eclipse.app

    Please specify the directory where you would like the eclim vimfiles installed.
    If you do not want to install the vimfiles (eg: emacs-eclim users), then type: skip
    Ex: ~/.vim
    ~/.vim/bundle/eclim
    > /Users/richardlee/.vim/bundle/eclim_mannual
    No such directory: /Users/richardlee/.vim/bundle/eclim_mannual
    > /Users/richardlee/.vim/bundle/eclim_manual/

    Choose which eclim features you would like to install.
    Type the number for each feature you want to install:
    Ex (Java and Python): 0 5
    Ex (Java and Python): 0,5
    Ex (Java, Web, and C/C++): 0-2
    0) Java Development
    1) Web Development
    2) C/C++ Development
    3) Ruby Development
    4) Php Development
    5) Python Development
    6) Scala Development
    7) Groovy Development
    8) Android Development
    > 0,2
    Eclim plugins to install:
    Java Development
    C/C++ Development
    Is this correct? (y/n): y
    running: ['java', '-Djava.net.useSystemProxies=true', '-jar', '/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar', '-initialize', '-debug'] ... done
    running: ['java', '-Djava.net.useSystemProxies=true', '-jar', '/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar', '-clean', '-refresh', '-application', 'org.eclipse.equinox.p2.garbagecollector.application'] ... done
    Checking for required eclipse dependencies...
    running: ['java', '-Djava.net.useSystemProxies=true', '-jar', '/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar', '-application', 'org.eclipse.equinox.p2.director', '-repository', u'http://download.eclipse.org/releases/oxygen/', '-list'] ... done

    [*] Install org.eclipse.cdt (9.4.0)
    Install/Upgrade dependencies? (y/n): y
    running: ['java', '-Djava.net.useSystemProxies=true', '-jar', '/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar', '-application', 'org.eclipse.equinox.p2.director', '-repository', u'http://download.eclipse.org/releases/oxygen/', '-installIU', u'org.eclipse.cdt.feature.group'] ... done

    Installing eclim...
    running: ['java', '-Djava.net.useSystemProxies=true', '-jar', '/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar', '-application', 'org.eclipse.equinox.p2.director', '-repository', 'file:///var/folders/w7/zbk6mkxd10n55kqbspqnd9rc0000gn/T/eclim-installer.XXXX.rKU0gOAP/update-site', '-installIU', 'org.eclim.feature.group'] ... done
    running: ['/Users/richardlee/.p2/pool/plugins/org.eclim_2.7.2/nailgun/configure'] ... rm: conftest.dSYM: is a directory
    done
    running: ['make'] ... ld: warning: option -s is obsolete and being ignored
    warning: no debug symbols in executable (-arch x86_64)
    done

    -----------------------------------------
    The eclim install completed successfully.
    You can now start the eclimd server by executing the script:
    /Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/eclimd

    For more information please see the eclimd server documentation:
    http://eclim.org/eclimd.html
    For information on using eclim, please visit the getting started guide:
    http://eclim.org/gettingstarted.html
    ➜  Downloads
```
to lanch an eclim manually, this will hold one shell, here's the log:
```bash
    ➜  bundle ls -al ~/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/eclimd
    lrwxr-xr-x  1 richardlee  staff  61  5 19 13:04 /Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/eclimd -> /Users/richardlee/.p2/pool/plugins/org.eclim_2.7.2/bin/eclimd
    ➜  bundle ./../../../richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/eclimd
    /usr/bin/java -version
    java version "1.8.0_121"
    Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
    Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
    JAVA_VERSION=8

    /usr/bin/java -d64 -Dosgi.requiredJavaVersion=1.8 -Dosgi.instance.area.default=@user.home/eclipse-workspace -XX:+UseG1GC -XstartOnFirstThread -Dorg.eclipse.swt.internal.carbon.smallFonts -Xms256m -Xmx1024m -Declipse.p2.max.threads=10 -XstartOnFirstThread -jar /Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/plugins/org.eclipse.equinox.launcher_1.4.0.v20161219-1356.jar --launcher.suppressErrors -debug -clean -refresh -application org.eclim.application
    Install location:
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/
    Configuration file:
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/configuration/config.ini loaded
    Configuration location:
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/configuration/
    Framework located:
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/../../../../../.p2/pool/plugins/org.eclipse.osgi_3.12.100.v20180210-1608.jar
    Loading extension: reference:file:org.eclipse.osgi.compatibility.state_1.1.0.v20170516-1513.jar
    eclipse.properties not found
    Framework classpath:
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/../../../../../.p2/pool/plugins/org.eclipse.osgi_3.12.100.v20180210-1608.jar
    file:/Users/richardlee/.p2/pool/plugins/
    file:/Users/richardlee/eclipse/java-oxygen/Eclipse.app/Contents/Eclipse/../../../../../.p2/pool/plugins/org.eclipse.osgi.compatibility.state_1.1.0.v20170516-1513.jar
    Debug options:
    file:/Users/richardlee/.vim/bundle/.options not found
    Time to load bundles: 106
    org.eclipse.m2e.logback.configuration: The org.eclipse.m2e.logback.configuration bundle was activated before the state location was initialized.  Will retry after the state location is initialized.
    Starting application: 9601
    org.eclipse.m2e.logback.configuration: Logback config file: /Users/richardlee/eclipse-workspace/.metadata/.plugins/org.eclipse.m2e.logback.configuration/logback.1.8.3.20180227-2137.xml
    SLF4J: Class path contains multiple SLF4J bindings.
    SLF4J: Found binding in [bundleresource://539.fwk1501587365:1/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: Found binding in [bundleresource://539.fwk1501587365:2/org/slf4j/impl/StaticLoggerBinder.class]
    SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
    SLF4J: Actual binding is of type [ch.qos.logback.classic.util.ContextSelectorStaticBinder]
    org.eclipse.m2e.logback.configuration: Initializing logback
    Application Started: 16817
    2018-05-19 13:17:08,893 INFO  [org.eclim.eclipse.EclimDaemon] Workspace: /Users/richardlee/eclipse-workspace
    2018-05-19 13:17:08,900 INFO  [org.eclim.eclipse.EclimDaemon] Home: /Users/richardlee/.p2/pool/plugins/org.eclim_2.7.2/
    2018-05-19 13:17:08,901 INFO  [org.eclim.eclipse.EclimDaemon] Starting eclim...
    2018-05-19 13:17:08,914 INFO  [org.eclim.eclipse.EclimDaemon] Loading plugin org.eclim
    2018-05-19 13:17:08,918 INFO  [org.eclim.eclipse.EclimDaemon] Loading plugin org.eclim.core
    2018-05-19 13:17:09,198 INFO  [org.eclim.plugin.core.CorePlugin] Loading eclim plugins...
    2018-05-19 13:17:09,204 INFO  [org.eclim.plugin.core.CorePlugin] Loading plugin org.eclim.jdt
    2018-05-19 13:17:09,221 INFO  [org.eclim.plugin.core.CorePlugin] Loading plugin org.eclim.cdt
    2018-05-19 13:17:09,226 INFO  [org.eclim.plugin.core.CorePlugin] Plugins loaded.
    2018-05-19 13:17:09,227 INFO  [org.eclim.eclipse.EclimDaemon] Loaded plugin org.eclim.core
    2018-05-19 13:17:09,229 INFO  [org.eclim.eclipse.EclimDaemon] Waiting on running jobs before starting eclimd...
    2018-05-19 13:17:19,244 INFO  [org.eclim.eclipse.EclimDaemon] Jobs finished.
    2018-05-19 13:17:19,245 INFO  [org.eclim.eclipse.EclimDaemon] Eclim Server Started on: 127.0.0.1:9091
```
TODO: may include a command to start Eclipse Server
to exam the connection, do :PingEclim in vim
auto complete success in System.out.println

TODO: and need build tool
TODO: need config zsh

following the getting start tutorial here: http://eclim.org/gettingstarted.html
and create my first java project
```vim
    :ProjectCreate /path/to/my_project -n java
    :ProjectList
    :NewSrcEntry # ?? it doesn't exist
    # add package and source file, and run the program with :Java, handy
    :Java #
```
eclipse could be a very helpful vim back end using eclim
but I have to let eclipse manage the project
plus, java is way slow in my air, pool machine

YCM java auto complete seems to work, but didn't get a properiate .ycm_extra_conf.py


## others
does java have shared library??
here, read latter: https://www.ibm.com/support/knowledgecenter/en/SSMKHH_10.0.0/com.ibm.etools.mft.doc/bc23072_.htm
and the magic GNI to link .so and java, not sure it's a good idea
