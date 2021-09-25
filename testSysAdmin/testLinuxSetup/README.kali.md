#### correct screen resolution for raspberry pi 4
xrandr -s 2560x1600 # to change solution in terminal

- on raspberry pi 4
/boot/config.txt
uncomment disable_overscan=1
http://rpf.io/configtxt


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
```shell
    apt install rxvt-unicode -y
    cp ./urxvt/Xresources ~/.Xresources
    xrdb ~/.Xresources
    mkdir -p ~/.urxvt/ext/ && cp -r ./urxvt/ext/* ~/.urxvt/ext/
```
using .Xresource to config it
add perl script to ~/.urxvt/ext/ and set up in .Xresource
TODO: font-size perl script refuse to operate
urxvt seem don't need compton to be transparent

I don't know, urxvt doesn't have a perl script plugin management,
guess I need to reserve these script myself

to config urxvt, first man, then archwiki

#### compton
use for gnome-terminal to get transparent


#### add user
```shell
    adduser wenchen
    usermod -aG sudo wenchen
    groups wenchen
```

#### sc-im
Linux has something called scim: Smart Common input method

spread calculator: https://github.com/andmarti1424/sc-im
```
    sudo apt install bison
    git clone https://github.com/andmarti1424/sc-im && cd sc-im
    vim src/Makefile
    make -C src
    sudo make -C src install
```

#### Wallpaper
```shell
    apt install feh -y
    mkdir -p ~/Pictures/WallPaper/ && cd ~/Pictures/WallPaper/
    wget https://i.redd.it/cb12p2q4rocx.png
    # restart i3
```
it seem feh couldn't using as wallpaper setter and do slideshow at the same time

#### torrent
apt install transmission # torrent file

#### screen temperature adjust
https://github.com/jonls/redshift
http://jonls.dk/redshift/
apt install redshift
~/.config/redshift.conf


#### fix firefox veritical tear in i3
disable hardware acceleration
For Firefox do this:
    Type "about:config" on the address bar.
    Search for layers.acceleration.force-enabled (default is false). This forces Hardware Acceleration to turn on.
    Change it to true by double-clicking.
    Save and restart Firefox.
from: https://forum.manjaro.org/t/firefox-screen-tearing-i3wm-compton/81794
In summary, I changed and added these options to my ~/.config/compton.conf.
It seems to have fix the issue.
```
    backend = "glx";
    vsync = "true";
    glx-swap-method = 2;
```

#### others
using selection to clipboard and mouse middle key to paste is reasonable

Hey, I am happy that I don't need a driver install to make PS4 controller earphone in Kali

using mkdir /some/directory/to/somewhere/ and then cd !$

I need a way to change volume, brighness, etc

<C-R> to search history

disable beep with modprobe -r pcspkr

set time in Kali because a wrong time could effect web broswer quality
timedatectl set-time '2019-09-23 15:30:00'

meeting Zathura - a document viewer
