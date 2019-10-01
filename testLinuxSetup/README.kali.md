xrandr -s 2560x1600 # to change solution in terminal

I need a way to change volume, brighness, etc

download youtube-dl from lastest version, and it tells me video don't exist

<C-R> to search history

disable beep with modprobe -r pcspkr


set time in Kali because a wrong time could effect web broswer quality
timedatectl set-time '2019-09-23 15:30:00'

meeting Zathura - a document viewer

I am reading README.Ubuntu.md and do some editing and
- [x] ranger
- [x] dmenu
- [ ]
- [ ]

#### how to input fontawesome within vim
go to fontawesome cheatsheet: https://fontawesome.com/cheatsheet/free/regular
in insert mode of vim, <C-v> u <the unicode of the font>

or search in here: https://fontawesome.com/icons?d=gallery

#### about fontawesome
from: https://www.blackmoreops.com/2014/07/31/install-fonts-on-linux/
```
    apt-cache search ttf-mscorefonts-installer
    apt-get install ttf-mscorefonts-installer
    apt-get install <package-name>
        # ttf-liberation
        # fonts-liberation
        # ttf-uralic
        # fonts-uralic
        # ttf-root-installer
        # ttf-freefont
        # ttf-dustin
        # ttf-linux-libertine
        # fonts-linuxlibertine
        # fonts-dustin
        # ttf-staypuft
```

download fontawesome from website
copy fonts file into directory:

    /usr/share/fonts
    /usr/share/X11/fonts
    /usr/local/share/fonts
    ~/.fonts
```shell
    wget <url to fonts>
    fc-cache -fv /fold/to/fonts
    fc-list -v | grep family
    fc-match OpenSans
```

download cheatsheet
and using vim insert mode, <C-v> u <unicode> to edit file

#### install fonts
from: https://gist.github.com/lightonphiri/5811226a1fba0b3df3be73ff2d5b351c

some place for google font: https://fonts.google.com/
Nerd font: https://www.nerdfonts.com/font-downloads

```shell
    cd /usr/share/fonts # I would prefer ~/.fonts/ or ~/.
    sudo mkdir googlefonts
    cd googlefonts
    sudo unzip -d . ~/Downloads/Open_Sans.zip
    sudo chmod -R --reference=/usr/share/fonts/opentype /usr/share/fonts/googlefonts
    sudo fc-cache -fv /usr/share/fonts # update cache, more like a small database with links to dictionary
    fc-match OpenSans
    # or
    fc-list -v | grep "<familyName>"
```

#### fix audio problem

kali don't play audio when playing youtube

apt install alsa-utils -y # to use alsamixer

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

#### polybar
```shell
    # need to build this from source code
    ** Use GCC even if Clang is installed ----------------------------- [y/N]: y
    ** Include support for "internal/i3" (requires i3) ---------------- [y/N]: y
    ** Include support for "internal/alsa" (requires alsalib) --------- [y/N]: y
    ** Include support for "internal/pulseaudio" (requires libpulse) -- [y/N]: y
    ** Include support for "internal/network" (requires libnl/libiw) -- [y/N]: y
    ** Include support for "internal/mpd" (requires libmpdclient) ----- [y/N]: y
    ** Include support for "internal/github" (requires libcurl) ------- [y/N]: y
    ** Build "polybar-msg" used to send ipc messages ------------------ [y/N]: y
    ** Executing cmake command
```
need some lib installed
already, I think that's it. Polybar is not ready in Kali yet.

#### urxvt
using .Xresource to config it
add perl script to ~/.urxvt/ext/ and set up in .Xresource
TODO: font-size perl script refuse to operate
urxvt seem don't need compton to be transparent

I don't know, urxvt doesn't have a perl script plugin management,
guess I need to reserve these script myself

to config urxvt, first man, then archwiki

#### compton
use for gnome-terminal to get transparent


#### zsh
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

#### Wallpaper
```shell
    mkdir -p ~/Pictures/WallPaper/ && cd ~/Pictures/WallPaper/
    wget https://i.redd.it/cb12p2q4rocx.png
    # restart i3
```
it seem feh couldn't using as wallpaper setter and do slideshow at the same time

#### Chinese input method
Hey, since I can read Chinese and there are some pretty cool Chinese Community,
I would need to be type Chinese in Kali, although I don't consider bring Chinese
into my Terminal yet, as a result of not finding a pretty fonts for terminal.
I think type Chinese in the search bar is good enough for now.
Plus if I really need to type Chinese in Terminal, Gnomal-Terminal has good internal font support for Chinese.
```
    sudo apt installl ibus-pinyin
    sudo apt install ibus-sunpinyin
    ibus-setup # config to using <C-space> to change imput method
    ibus restart
    reboot
```

#### others
using selection to clipboard and mouse middle key to paste is reasonable

using mkdir /some/directory/to/somewhere/ and then cd !$
