ubuntu flovar Linux set up
================================================================================

TODO: definately have soemthing to add
ubuntu setup script
```bash
sudo apt update
### app tools
sudo apt install -y terminator
sudo apt install -y vim-gtk3     # for +clipboard and +python3
sudo apt install -y tmux
sudo apt install -y zsh
sudo apt install -y git
sudo apt install -y ranger
sudo apt install -y cmatrix
sudo apt install -y tldr
sudo apt install -y pandoc

### system tools
sudo apt install -y i3
sudo apt install -y net-tools # ifconfig
sudo apt install -y htop

sudo apt install -y g++
sudo apt install -y valgrind
sudo apt install -y ctags

# ??
# sudo apt-get install -y python-opencv

# git setup
git config --global user.name wenchen
git config --global user.email richardlee0211er@gmail.com
```

this seem to be a good ubuntu set up script
[here](https://github.com/sojharo/mangi-script/blob/master/my_ubuntu_setup.sh)

using mac keyboard but windows way to copy and paste is painful

maybe I just need a simple laptop setup to focus on coding problem

[this](https://dev.to/brpaz/my-linux-development-environment-of-2018-ch7)
contains a lot ubuntu tools

so restart the VM, and in the login options, I can i3 as my VM(window manage)

this is exciting, and this is a choice. i3, tmux, transparent terminal and backgroud picture

and I will need a remap to vim keystrick


#### map cap locks to ctrl as I am so used to it
- change the keyboard layout
setxkbmap -layout us

- xmodmap utility
utility for modifying keymaps and pointer button mappings in X
mainly from: https://wiki.archlinux.org/title/xmodmap
some conceptions:
keycode: the code that keyboard sent to motherboard
keysym:  the symbols that computer see when receive keycode
keymap table: the map between keycode and keysym

warming: Due to a limitation of Xorg, xmodmap settings are not applied to
hotplugged devices automatically.

- xmodmap -pke
...
keycode 57 = n N
...

 1. Key
 2. Shift+Key
 3. Mode_switch+Key
 4. Mode_switch+Shift+Key
 5. ISO_Level3_Shift+Key
 6. ISO_Level3_Shift+Shift+Key

- map caplock to ctrl
```~/.Xmodmap
    ! Simplest example of changeing CapsLock into Control
    ! from: https://wiki.archlinux.org/title/xmodmap
    ! need to clear modifier key involved
    clear lock
    clear control
    ! assign new keysym to keycode
    keycode 66 = Control_L
    ! add back the modifier key
    add control = Control_L Control_R
```
then xmodmap ~/.Xmodmap

following example modifies CapsLock to Control, and Shift+CapsLock to CapsLock
I perfer this solution
```~/.Xmodmap
	clear lock
	clear control
	add control = Caps_Lock Control_L Control_R
	keycode 66 = Control_L Caps_Lock NoSymbol NoSymbol
```
- see the changed modifier key
xmodmap -pm
```shell
	┌──(kali㉿kali)-[~]
	└─$ xmodmap -pm                                                                                                 1 ⚙
	xmodmap:  up to 4 keys per modifier, (keycodes in parentheses):

	shift       Shift_L (0x32),  Shift_R (0x3e)
	lock
	control     Control_L (0x25),  Control_L (0x42),  Control_R (0x69)
	mod1        Alt_L (0x40),  Alt_R (0x6c),  Meta_L (0xcd)
	mod2        Num_Lock (0x4d)
	mod3
	mod4        Super_L (0x85),  Super_R (0x86),  Super_L (0xce),  Hyper_L (0xcf)
	mod5        ISO_Level3_Shift (0x5c),  Mode_switch (0xcb)
```

- to see the keycode and keysym
```shell
xev | awk -F'[ )]+' '/^KeyPress/ { a[NR+2] } NR in a { printf "%-3s %s\n", $5, $8 }'

showkey --keycodes # in console
```

- Turn CapsLock into Control, and LeftControl into Hyper
This is new idea for me.
Laptop users may prefer having CapsLock as Control.
The Left Control key can be used as a Hyper modifier
(an additional modifier for emacs or openbox or i3).

```~/.Xmodmap
	clear      lock
	clear   control
	clear      mod1
	clear      mod2
	clear      mod3
	clear      mod4
	clear      mod5
	keycode      37 = Hyper_L
	keycode      66 = Control_L
	add     control = Control_L Control_R
	add        mod1 = Alt_L Alt_R Meta_L
	add        mod2 = Num_Lock
	add        mod3 = Hyper_L
	add        mod4 = Super_L Super_R
	add        mod5 = Mode_switch ISO_Level3_Shift
```

- using super+tab to switch window focus
- disable super+l to lock the screen

#### zsh and oh-my-zsh
a tutorial: https://computingforgeeks.com/installingconfiguring-and-customizing-zsh-on-linux/
```shell
    apt install zsh

    ## config
    usermod username -s /usr/bin/zsh
    # or
    chsh -s /usr/bin/zsh username

    # install Oh My Zsh
    sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

```~/.zshrc
    ## wenchen
    ## inside ~/.bash_profile
    ## xmodmap ~/.Xmodmap
    ## ~/.bash_profile is for login shells(GUI login or ssh)
    ## while ~/.bashrc is for interactive non-login shells
    bindkey -v
    bindkey "^A" vi-beginning-of-line
    bindkey "^E" vi-end-of-line

    ## from: https://unix.stackexchange.com/questions/97843/how-can-i-search-history-with-text-already-entered-at-the-prompt-in-zsh/280845
    autoload -U up-line-or-beginning-search
    autoload -U down-line-or-beginning-search
    zle -N up-line-or-beginning-search
    zle -N down-line-or-beginning-search
    bindkey "^[[A" up-line-or-beginning-search # Up
    bindkey "^[[B" down-line-or-beginning-search # Down
```

#### ranger
apt install ranger
~/.config/ranger/rc.conf
```
    set preview_images true
    set preview_images_method urxvt
    set draw_borders true
    set ranger_load_default_rc false
```

ranger --copy-config=scope
TODO: couldn't get image preview, could be since Kali distro

#### Chinese input method
from: http://yingshaoxo.blogspot.com/2017/12/install-chinese-input-method-on-kali.html
not work for i3
```
    # 0. Set ibus
    `sudo apt install ibus`
    `sudo im-config`

    1. Install RIME
    `sudo apt-get install ibus-rime`
    https://github.com/rime/home/wiki/RimeWithIBus#ubuntu

    2. Select Input Language
    `reboot`
    System Setting — Region&Language — input Source, then click ‘+’ button, choose Chinese

    3. Ready to use
    Press Super + space to switch input method.
    Press F4 to switch schema(simple or complex).
```

from: https://ultra-technology.org/linux_for_beginners/how-to-write-in-japanese-or-chinese-under-linux-on-any-window-manager-using-fcitx/
from: https://askubuntu.com/questions/1060130/using-ibus-japanese-input-with-ubuntu-mate-and-i3
using fcitx, take some patient to make it running
```
    sudo apt install fcitx fcitx-googlepinyin fcitx-mozc im-config
    sudo apt install xfonts-intl-chinese

    echo " \
    export XMODIFIERS=@im=fcitx \
    export GTK_IM_MODULE=fcitx \
    export QT_IM_MODULE=fcitx \
    export XIM=fcitx \
    fcitx " >> ~/.xinitrc

    im-config -c # using im-config to select fcitx

    fcitx
    fcitx-configtool # using fcitx-config-gtk3 to add language/shortcuts
```

#### Chinese input method 2
now I understand how encoding and font work.
Hey, since I can read Chinese and there are some pretty cool Chinese Community,
I would need to be type Chinese in Kali, although I don't consider bring Chinese
into my Terminal yet, as a result of not finding a pretty fonts for terminal.
I think type Chinese in the search bar is good enough for now.
Plus if I really need to type Chinese in Terminal,
Gnomal-Terminal has good internal font support for Chinese.
```
    sudo apt install ibus-pinyin
    sudo apt install ibus-sunpinyin
    ibus-setup # config to using <C-space> to change imput method
    ibus restart
    reboot
```

#### firefox plugin
vimium, vim like operation
adblock, adblock
windowed, could float youtube video
dark reader, for late night read

#### screenshot
apt install scrot # and bind it to PrtSc
apt install gnome-screenshot

#### nvidia driver
from: https://docs.kali.org/general-use/install-nvidia-drivers-on-kali-linux
sudo apt install nvidia-driver-455

#### use terminator
as it support "copy on select"
would be faster when with terminal and broswer work flow
apt install terminator



#### unattended-upgr take too long
from: https://askubuntu.com/questions/934807/unattended-upgrades-status
check
```shell
	systemctl list-timers apt-daily.timer
	ls -l /var/lib/apt/periodic/
	less /var/log/unattended-upgrades/unattended-upgrades.log
	apt list --upgradeable | wc -l
```
for this time, it would take 10 hours to download all the packages it needs
abort this job

from: https://unix.stackexchange.com/questions/374748/ubuntu-update-error-waiting-for-unattended-upgr-to-exit
    1. Stop the automatic updater.
    `sudo dpkg-reconfigure -plow unattended-upgrades`
    At the first prompt, choose not to download and install updates.
    Make a reboot.

    2. Make sure any packages in an unclean state are installed correctly.
    `sudo dpkg --configure -a`

    3. Get your system up-top-date.
    `sudo apt update && sudo apt -f install && sudo apt full-upgrade`

    4. Turn the automatic updater back on, now that the blockage is cleared.
    `sudo dpkg-reconfigure -plow unattended-upgrades`
    Select the package unattended-upgrades again.

log:
system crashed, try to save it,
guess what, donot move the case when the computer is working


#### fix audio problem

kali don't play audio when playing youtube
apt install alsa-utils -y # to use alsamixer
And it could tell PS4 controller and pass audio to this device, nice

#### fix firefox veritical tear
disable hardware acceleration
For Firefox do this:
    Type "about:config" on the address bar.
    Search for layers.acceleration.force-enabled (default is false). This forces Hardware Acceleration to turn on.
    Change it to true by double-clicking.
    Save and restart Firefox.

#### firefox tab appearance

I can hard see the tabs, change its appearence
from: https://superuser.com/questions/1653533/how-to-switch-back-to-firefox-old-style-of-tabs
n Firefox 91, restore the old tab style as follows:

```shell
    Open about:config.

    Search for toolkit.legacyUserProfileCustomizations.stylesheets.

    Double-click the value to set it to true.

    Open about:support.

    Search for Profile Directory (or Profile Folder).

    Click Open Directory (or Open Folder).

    Create a directory named chrome.

    Navigate into the chrome directory.

    Create a new file inside chrome named userChrome.css.

    Copy and paste the following code into userChrome.css:

     .tab-background {
       border-radius: 0px 0px !important;
       margin-bottom: 0px !important;
     }

     .tabbrowser-tab:not([selected=true]):not([multiselected=true]) .tab-background {
       background-color: color-mix(in srgb, currentColor 5%, transparent);
     }

     menupopup>menu,
     menupopup>menuitem {
       padding-block: 2px !important;
     }

     :root {
       --arrowpanel-menuitem-padding: 2px !important;
     }

    Save the file.

    Restart Firefox.

	The old tab style is restored.
```


#### vim copy and paste x11
apt install vim-gtk3
vim --version # look for xterm_clipboard
set clipboard+=unnamedplus

#### build vim with X11 copy and paste support
from vim.git/src/INTSALL
```shell
To build Vim on Ubuntu from scratch on a clean system using git:
	Install tools required to be able to get and build Vim:
	% sudo apt install git
	% sudo apt install make
	% sudo apt install clang

	Build Vim with default features:
	% git clone https://github.com/vim/vim.git
	% cd vim/src
	% make

	Run tests to check there are no problems:
	% make test

	Install Vim in /usr/local:
	% sudo make install

	Add X windows clipboard support (also needed for GUI):
	% sudo apt install libxt-dev
	% make reconfig

	Add GUI support:
	% sudo apt install libgtk-3-dev
	% make reconfig

	Add Python 3 support:
	% sudo apt install libpython3-dev
	Uncomment this line in Makefile:
		"CONF_OPT_PYTHON3 = --enable-python3interp"
	% make reconfig
```

apt vim is in /user/bin while this build should be in /user/local/bin/vim
only ubuntu using Ctrl+Shift+c or +v to copy and paste


#### pip3 and internet speed test
sudo apt install -y python3-pip
pip3 install speedtest-cli
export PATH="/home/wenchen/.local/bin/:$PATH" # ~/.zshrc

Gigbit internet in the lab
```shell
    pip3 install speedtest-cli
    ➜  testLinuxSetup git:(master) ✗ ~/.local/bin/speedtest
    Retrieving speedtest.net configuration...
    Testing from SUNY at Stony Brook (XXXXXXXXXXXXX)...
    Retrieving speedtest.net server list...
    Selecting best server based on ping...
    Hosted by Optimum Online (New York, NY) [76.79 km]: 7.726 ms
    Testing download speed................................................................................
    Download: 774.94 Mbit/s
    Testing upload speed......................................................................................................
    Upload: 677.55 Mbit/s
```

#### youtube-dl
sudo wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+x /usr/local/bin/youtube-dl
sudo apt install python-dev
rehash

#### dolphin
using dolphin as it provides better img preview
sudo apt install dolphin
feels like this apt build is limited

- setting default filemanager to dolphin
failed after some twinking
maybe reboot??
https://help.ubuntu.com/community/DefaultFileManager

#### cuda
sudo apt install nvidia-cuda-toolkit
nvcc --version

#### stress test
nice, the new heat sink works, stress cpu top temp 65 degrees,
stress gpu top temp 71 degrees
```shell
    sudo apt-get install -y stress htop iotop lm-sensors
    # Run a stress test with `nproc` CPU workers (sqrt)
    #                        `nproc` Virtual Memory workers (malloc / free)
    #                        `nproc` workers calling (sync)
    #                        `nproc` workers writing to disk (write / unlink)
    # For a total of 60 seconds.
    stress --cpu `nproc` --vm `nproc` --vm-bytes 1GB --io `nproc` --hdd `nproc` --hdd-bytes 1GB --timeout 60s

    git clone https://github.com/wilicc/gpu-burn
    cd gpu-burn
    make
    ./gpu_burn 60 # will run gpu_burn for 60 seconds

    sudo apt install s-tui
    s-tui

    htop
    sudo iotop
    watch sudo sensors
    watch nvidia-smi
```

log 20210924 lab machine
--------------------------------------------------------------------------------
python3 unattended-upgrade # 100% CPU core usage

okay, it made sence, the CPU thermal throttled pretty easily


using i3
================================================================================

if I don't use i3 for a while, I would forget the keybound

does it matter to optimise my workflow and windower manager?:
yes, of course, I use it at a daily basis and it's like optimise code that runs every time

i3 could help to manage the brower and pdf viewer

vim and tmux is using leading key to revoke the command

basic tools I will need:
- file system brower(try ranger)
- web brower(with vim plug in)
- terminal, a nice shell and some nice tools(vim )
- pdf-viewer and picture viewer

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

weird thought: using Esc+num to do something?: no for now

TODO: When dealing with pictures, how to working with i3?
using ranger as recommanded by LuckSmith??

yes, but i3 using alt or win key as mod key.
I would using the key next to space for convinience thumb operation.
That means this is command on a mac keyboard, Alt on a windows keyboard

I would open 2~4 windows in a workspace, then only using $mod+j and $mod+k to move focus around?:
Yes, using $mod+j and $mod+k is move focus to next or previous windows
TODO: how to do that, next or previous window??

DONE: I need background pictures, how to do that ?: hef

well, because I am using VM in Mac or Windows,
using command key or win key easely cause key conflicts.
like command+f in broswer is usually find function but not full screen shortcut for i3

Hahaha, nowadays, shortcut is far more less then the requirement

actually I like "modes" concept in vim

DONE: I will have some more questions:
- what about image viewers, I will do openCV project ?: ranger
- what about open command, I will using webbroswer to preview my markdown file ?: mimeopen

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

what's my goal, my goal is to build a highly costumised system

how much time will you save with i3 ?:
Just go through it as soon as possible

things I wanna do within Linux machine, build a custome OS for me
- code
- fancy back ground
- Firefox
- PDF viewer

considering that I might build an applications similar, I would check these open source code first

install i3-gaps on ubuntu 18.04
--------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------
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

following this tutorial:
[UnixPorn](https://www.reddit.com/r/unixporn/wiki/index)
--------------------------------------------------------------------------------

I don't really care how system fonts set up, but I need to use
[fronts](https://github.com/Tecate/bitmap-fonts)

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

!!a good rice start article: https://www.reddit.com/r/unixporn/wiki/ricerous_info

following this video: https://www.youtube.com/watch?v=ARKIwOlazKI
--------------------------------------------------------------------------------

#### change fonts

interesting, ~/.fonts and
sudo apt install lxappearance

two places to config gtk application fonts:
~/.gtkrc-2.0
~/.config/gtk-3.0/

change GTK theme: Arc theme
```shell
    sudo apt install Arc theme
```
and use "lxappearance" to change theme, great

using gtk arc theme
could also change firefox theme to arc theme, just search firefox add-on arc theme

using moka icon by search

#### thunar, the file explorer GUI choosed by the author
sudo apt install thunar
# sudo apt install gnome-icon-theme-??
# fix missing icon in "thunar" by edit gtk-icon-theme-name="gnome" in ~/.gtkrc-2.0

using rofi
--------------------------------------------------------------------------------

sudo apt install rofi

I could understand demu_run as a CLI(command line interface)

bindsym $mod+semicolon exec dmenu_run -some-arguments
bindsym $mod+d exec rofi -show run \
    -lines 3 -eh 2 -width 100 -padding 800 -opacity "85" \
    -bw 0 -bc "$bg-color" -bg "$bg-color" -fg "$text-color" \
    -hlbg "$bg-color" -hlfg "#9575cd" \
    -font "System San Francisco Display 18"

sudo apt install compton # a compositor for X11

i3status is also a CLI, and we can write our own shell script to replace it

https://fontawesome.com/cheatsheet
TODO: it seems this emulate can't handle unicode icon

sudo apt install i3blocks

install playerctl by search, download and install
sudo dpkg -i playerctl-0.4.2_amd64.deb

load rhythmbox load with i3
--------------------------------------------------------------------------------

exec rhythmbox # load everytime you login to a X session
exec_always rhythmbox # load everytime you restart i3 $mod+shift+r

sudo apt install feh

configure monitor
--------------------------------------------------------------------------------

sudo apt-get install arandr
config file save in .screenlayout/foo.sh
internally, it use xrandr and arguments

rename workspaces
--------------------------------------------------------------------------------

```config
    set $workspace1 "1. Editor"
    set $workspace1 "2. something"
    set $workspace1 "3. Editor"
    set $workspace1 "4. Editor"

    # switch to workspace
    bindsym $mod+1 workspace $workspace1
    bindsym $mod+2 workspace $workspace2
    bindsym $mod+3 workspace $workspace3
    bindsym $mod+4 workspace $workspace4

    # move focused container to workspace
    bindsym $mod+Shift+1 move container to workspace $workspace1
    bindsym $mod+Shift+2 move container to workspace $workspace2
    bindsym $mod+Shift+3 move container to workspace $workspace3
    bindsym $mod+Shift+4 move container to workspace $workspace4
```

force windows to open on certain workspaces
--------------------------------------------------------------------------------

CLI: xprop
and then click on one window to get VM_CLASS, need the second argument


in ~/.config/i3/config
assign [class="Rhythmbox"] $workspace2

how to associate Font Awesome icons with your workspace
--------------------------------------------------------------------------------

https://github.com/FortAwesome/Font-Awesome
```shell
download the zip file and cp *.ttf file into ~/.font
```

search "Awesome Fonts cheatsheet"

```config
    # floating
    for_window [class="qTox"] floating enable
    for_window [class="Pavucontrol"] floating enable
    for_window [class="Skype"] floating enable

    # Keys
    exec_always xmodmap -e "clear lock" #disable caps lock switch
    exec_always xmodmap -e "keysym Caps_Lock = Escape" #set caps_lock as escape
```

using terminal transparence and back background, save colors for vim and other application
don't use theme color in terminal

using URXVT
--------------------------------------------------------------------------------
in .Xresources
```shell
    URxvt.font: xft:monospace:size=16
    URxvt.scrollBar: false
```
and load into urxvt
```shell
    xrdb ~/.Xresources
```

urxvt --help 2>&1 | grep scroll
Arch wiki

while, URXVT extension is perl script

another package manager:
yaourt -S urxvt-fullscreen

finding urxvt extension, others/dotfile, Arch wiki, extension github repository, reddit UnixPorn

take a break here, I did well. to be continue

others
================================================================================

change $PS1 \w to \W
to only show this current directory name in prompt

so windows could be in the surface of this workspace, or in the background,
or in the other workspace. Basically that nothing is hiding from the user's point of "view"

it seems to be immature to install i3-gap in Ubuntu 18.04.
plus I don't wanna keep google things for rise my LinuxOS(set-up)

it turns out install i3 in Ubuntu 18.04 is a pain.
try other Linux distro, I would need a well documented one


format disk to exfat for backup use
--------------------------------------------------------------------------------

well, disk format should really use a GUI, as I do not format disk every week
I properly do it every two year
- low-level format: done by manufactures
- Partitioning: disk into sections
    partition editor: fdisk, GNU Parted or Disk Uitlity
- High-level formatting: file system, cluster size, partition label

use GUID for bigger than 2TB harddrive
use exfat to make it readable and writable for all mac, win and Linux
NTFS for windows
Ext4 for Linux

```shell
    ## didn't learn it completely
    sudo apt install exfat-fuse exfat-utils
    sudo fdisk -l
    sudo wipefs -a /dev/sdb
    sudo fdisk /dev/sdb
    sudo mkfs.exfat -n myStore4B /dev/sdb
```

BorgBackup
--------------------------------------------------------------------------------
from: https://borgbackup.readthedocs.io/en/stable/quickstart.html
borg init --encryption=repokey /path/to/repo
borg -v -p create /path/to/repo::Monday ~/src ~/Documents
borg create --stats /path/to/repo::Tuesday ~/src ~/Documents

```bash
	#!/bin/sh

	# Setting this, so the repo does not need to be given on the commandline:
	export BORG_REPO=ssh://username@example.com:2022/~/backup/main

	# See the section "Passphrase notes" for more infos.
	export BORG_PASSPHRASE='XYZl0ngandsecurepa_55_phrasea&&123'

	# some helpers and error handling:
	info() { printf "\n%s %s\n\n" "$( date )" "$*" >&2; }
	trap 'echo $( date ) Backup interrupted >&2; exit 2' INT TERM

	info "Starting backup"

	# Backup the most important directories into an archive named after
	# the machine this script is currently running on:

	borg create                         \
	    --verbose                       \
	    --filter AME                    \
	    --list                          \
	    --stats                         \
	    --show-rc                       \
	    --compression lz4               \
	    --exclude-caches                \
	    --exclude '/home/*/.cache/*'    \
	    --exclude '/var/tmp/*'          \
	                                    \
	    ::'{hostname}-{now}'            \
	    /etc                            \
	    /home                           \
	    /root                           \
	    /var                            \

	backup_exit=$?

	info "Pruning repository"

	# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
	# archives of THIS machine. The '{hostname}-' prefix is very important to
	# limit prune's operation to this machine's archives and not apply to
	# other machines' archives also:

	borg prune                          \
	    --list                          \
	    --prefix '{hostname}-'          \
	    --show-rc                       \
	    --keep-daily    7               \
	    --keep-weekly   4               \
	    --keep-monthly  6               \

	prune_exit=$?

	# use highest exit code as global exit code
	global_exit=$(( backup_exit > prune_exit ? backup_exit : prune_exit ))

	if [ ${global_exit} -eq 0 ]; then
	    info "Backup and Prune finished successfully"
	elif [ ${global_exit} -eq 1 ]; then
	    info "Backup and/or Prune finished with warnings"
	else
	    info "Backup and/or Prune finished with errors"
	fi

	exit ${global_exit}
```
