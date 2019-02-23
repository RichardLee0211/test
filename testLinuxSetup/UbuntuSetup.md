using this new ubuntu VM now
================================================================================

TODO: definately have soemthing to add
ubuntu setup script
```bash
sudo apt update
sudo apt install -y vim
sudo apt install -y tmux
sudo apt install -y i3
sudo apt install -y git
sudo apt install -y g++
# ?? sudo apt install -y python3
```

this seem to be a good ubuntu set up script
[here](https://github.com/sojharo/mangi-script/blob/master/my_ubuntu_setup.sh)

using mac keyboard but windows way to copy and paste is painful

maybe I just need a simple laptop setup to focus on coding problem

[this](https://dev.to/brpaz/my-linux-development-environment-of-2018-ch7)
contains a lot ubuntu tools

so restart the VM, and in the login options, I can i3 as my VM(window manage)

this is excited, and this is a choice. i3, tmux, transparent terminal and backgroud picture

and I will need a remap to vim keystrick

using i3
================================================================================

if I don't use i3 for a while, I would forget the keybound

does it matter to optimise my workflow and windower manager?
yes, of course, I use it at a daily basis and it's like optimise code that runs every time

trying to adopt i3 into my system as its famousness, let see what I can do

i3 could help to manage the brower and pdf viewer

so far, don't quit tmux

using command key as Modkey

vim and tmux is using leading key to revoke the command

basic tools I will need:
- file system brower(try ranger)
- web brower(with vim plug in)
- terminal, a nice shell and some nice tools(vim )
- pdf-viewer and picture viewer

I will need to replace caps-lock key to Ctrl, because so many command line shortcut,
vim window manage shortcut and tmux shortcut using Ctrl

it is annoying when using VM, part of shortcuts are captured by the host OS

shortcut management:
a layer beyond common apps
(system wise or window manager wise, WM is still an app that run on top of sys):
	i3:
	- $mod+Num to move to speicified workspace
	- do I really need to move windows between workspaces? or I just close one in workspace A and then open a new one in workspace B
	- $mod+j and $mod+k, to move focus about windows is a so frequent operation
	- $mod+Shift+c to reload config file
	- $mod+d to trigger dmenu(a application launcher)


	macOS:
	- Ctrl+Direction to move between workspaces
	- super+shift+4 to trigger screen print
	- super+tab to switch appliactions
	- super+space to trigger spotlight
	- Ctrl+space to toggle input method

	windows:
	- Alt+tab to switch applications

shell:
	- Ctrl+a to move to beginning of line,
	- Ctrl+e to move to end of line,
	- Ctrl+r to search bash history
	- Ctrl+c to terminal process
	- Ctrl+z to put process in the background

vim:
	- Ctrl+w to trigger windows mode
	- Ctrl+v to trigger visual block mode

tmux:
	- Ctrl+b to trigger tmux operations

broswer with vimium plug in:
	- using single key strick to do things
	- o to open a new url in current tab
	- O to open a new url in a new tab
    - yy to copy the current URL to the clipboard
    - p  to open the clipboard's URL in the current tab
    - P  to open the clipboard's URL in the new tab

TODO: weird thought: using Esc+num to do something??

TODO: When dealing with pictures, how to working with i3?
using ranger as recommanded by LuckSmith??

Yes, the number keys could do something important.
e.g. in vim, ^ is move to the beginning of line, $ is move to end of line

yes, but i3 using alt or win key as mod key.
I would using the key next to space for convinience thumb operation.
That means this is command on a mac keyboard, Alt on a windows keyboard

I would open 2~4 windows in a workspace, then only using $mod+j and $mod+k to move focus around?:
Yes, using $mod+j and $mod+k is move focus to next or previous windows
TODO: how to do that, next or previous window??

what about I using terminal on a float window and the terminal is transparent
while other windows on the back.

I would open at most 4 windows.
If I only use 2 windows, one in left and one in right,
what differece it make to using Command+tab to switch between these applications?
And Ctrl+tab to switch tabs in web broswer

TODO: I need background pictures, how to do that??

well, because I am using VM in Mac or Windows,
using command key or win key usingeasely cause key conflicts.
like command+f in broswer is usually find function but not full screen shortcut for i3

Hahaha, nowadays, shortcut is far more less then the requirement

actually I like "modes"

TODO: I will have some more questions:
- what about image viewers, I will do openCV project
- what about open command, I will using webbroswer to preview my markdown file??

what I will most do with i3 is about move focus around, open applications and then close them

and tmux is valuable in both macOS and Linux system, basic every shell problem.
while i3 is only for system that installed them, Yes, system that could install i3.
what about public server setup, I would use ssh anyway, so I will need tmux

every applications is using
Ctrl+Char, Ctrl+Shift+Char, Ctrl+Alt+Char(app-wise)
Super+Char, Super+Shift+Char, Super+Alt+Char(system-wise)
it would cost some time to do compromise between the System setup and applications
for shortcuts to working together

I gonna to disable some shortcut in Fusion software, as I don't really need them.
like in Fusion8, Command+h is for hide. I would using mouse when need to hide a application

this is weird that I need to copy the url in a broswer
- command+l in macOS
- ctrl+l in windows
but once I get into the url bar in broswer, I need to using mouse to get the focus back



read some bloggers:
GTK app

- [an experience i3 user](https://leotindall.com/post/modding-vim-i3-and-efficiency/)
- [GTK wiki](https://en.wikipedia.org/wiki/GTK)

i3 user mannual is one part, but note completed for me

what's my goal, my goal is to build a highly costumal system

how much time will you save with i3 ?:
Just go through it as soon as possible

things I wanna do within Linux machine, build a custome OS for me
- code
- fancy back ground
- Firefox
- PDF viewer

considering that I might build an applications similar, I would check these open source code first

ranger
================================================================================

https://github.com/ranger/ranger

```cpp
    sudo apt install python-pip
    pip install ranger-fm # didn't work out on ubuntu
    sudo apt install ranger # works on ubuntu
```

ranger is mainly for PDF review and picture preview

set up https://wiki.archlinux.org/index.php/Ranger#PDF_file_preview

install openCV-python
================================================================================

sudo apt-get install -y python-opencv

install i3-gaps on ubuntu 18.04
================================================================================
```bash
#!/bin/bash
    sudo apt install -y \
    libxcb1-dev \
    libxcb-keysyms1-dev \
    libpango1.0-dev \
    libxcb-util0-dev \
    libxcb-icccm4-dev \
    libyajl-dev \
    libstartup-notification0-dev \
    libxcb-randr0-dev \
    libev-dev \
    libxcb-cursor-dev \
    libxcb-xinerama0-dev \
    libxcb-xkb-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    autoconf \
    libxcb-xrm0 \
    libxcb-xrm-dev \
    automake

    cd /tmp

# clone the repository
    git clone https://www.github.com/Airblader/i3 i3-gaps
    cd i3-gaps

# compile & install
    autoreconf --force --install
    rm -rf build/
    mkdir -p build && cd build/

# Disabling sanitizers is important for release versions!
# The prefix and sysconfdir are, obviously, dependent on the distribution.
    ../configure --prefix=/usr --sysconfdir=/etc --disable-sanitizers
    make
    sudo make install
```

install [i3blocks]
(https://github.com/vivien/i3blocks)

install polybar
================================================================================
it seems to work
```shell

    sudo apt-get install -y \
    cmake \
    cmake-data \
    libcairo2-dev \
    libxcb1-dev \
    libxcb-ewmh-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-randr0-dev \
    libxcb-util0-dev \
    libxcb-xkb-dev \
    pkg-config \
    python-xcbgen \
    xcb-proto \
    libxcb-xrm-dev \
    i3-wm \
    libasound2-dev \
    libmpdclient-dev \
    libiw-dev \
    libcurl4-openssl-dev \
    libpulse-dev \
    libxcb-composite0-dev \
    xcb \
    libxcb-ewmh2

    git clone https://github.com/jaagr/polybar.git

    cd polybar && ./build.sh

```

I don't know if I install polybar right, when I launch it, it show errors

log
================================================================================

so windows could be in the surface of this workspace, or in the background,
or in the other workspace. Basically that nothing is hiding from the user's point of "view"

it seems to be immature to install i3-gap in Ubuntu 18.04.
plus I don't wanna keep google things for rise my LinuxOS(set-up)

it turns out install i3 in Ubuntu 18.04 is a pain.
try other Linux distro, I would need a well documented one

well, troggle full screen could use space or ` in wenchen_mode

following this tutorial:
[UnixPorn](https://www.reddit.com/r/unixporn/wiki/index)
--------------------------------------------------------------------------------

I don't really care how system fonts set up, but I need to use
[fronts](https://github.com/Tecate/bitmap-fonts)

using i3

GTK themes are fine
icon themes are fine

organize your Xresource
```
    ! ~/.Xresources
    #define mybg #222222
    #define myfg #cccccc
    #define myfont Inconsolata
    #define myfontsize 7
    #define mypadding 20
    ! #include "~/.xres/rofi"
    ! #include "~/.xres/urxvt"
    ! #include "~/.xres/xterm"


    ! ~/.xres/rofi
    rofi.bg: mybg
    rofi.fg: myfg
    rofi.hlfg: mybg
    rofi.hlbg: myfg
    rofi.padding: mypadding
    rofi.font: myfont myfontsize


    ! ~/.xres/urxvt
    URxvt*background: mybg
    URxvt*foreground: myfg
    URxvt*highlightColor: myfg
    URxvt*highlightTextColor: mybg
    URxvt*cursorColor: myfg
    URxvt*cursorColor2: mybg
    URxvt*font: xft:myfont:medium:size=myfontsize
    URxvt*boldFont: xft:myfont:size=myfontsize
    URxvt*italicFont: xft:myfont:italic:size=myfontsize
    URxvt*boldItalicFont: xft:myfont:bold:italic:size=myfontsize
    ! URxvt*internalBorder mypadding

    ! ~/.xres/xterm
    xterm*faceName: myfont:style=Medium:size=myfontsize
    xterm*background: mybg
    xterm*foreground: myfg
```

```shell
sudo apt-get install htop\
                cmatrix

```

this is a good rice start article: https://www.reddit.com/r/unixporn/wiki/ricerous_info

following this video: https://www.youtube.com/watch?v=ARKIwOlazKI
