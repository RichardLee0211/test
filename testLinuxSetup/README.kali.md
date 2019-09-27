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
    fc-cache -fv
    fc-list -v | grep family
    fc-match OpenSans
```

download cheatsheet
and using vim insert mode, <C-v> u <unicode> to edit file

#### install fonts
from: https://gist.github.com/lightonphiri/5811226a1fba0b3df3be73ff2d5b351c

some place for google font: https://fonts.google.com/

```shell
    cd /usr/share/fonts # I would prefer ~/.fonts/
    sudo mkdir googlefonts
    cd googlefonts
    sudo unzip -d . ~/Downloads/Open_Sans.zip
    sudo chmod -R --reference=/usr/share/fonts/opentype /usr/share/fonts/googlefonts
    sudo fc-cache -fv
    fc-match OpenSans
```

#### fix audio problem

kali don't play audio when playing youtube

apt install alsa-utils -y # to use alsamixer

#### ranger
apt install ranger
~/.config/ranger/rc.conf
```
    set preview_images true
    set ranger_load_default_rc false
```

ranger --copy-config=scope
TODO: rice it

#### polybar

#### urxvt
using .Xresource to config it
add perl script to ~/.urxvt/ext/ and set up in .Xresource

#### compton
use for gnome-terminal to get transparent

#### others
using selection to clipboard and mouse middle key to paste is reasonable
