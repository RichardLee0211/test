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

#### correct screen resolution for raspberry pi 4
xrandr -s 2560x1600 # to change solution in terminal

- on raspberry pi 4
/boot/config.txt
uncomment disable_overscan=1
http://rpf.io/configtxt

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

#### how to input fontawesome within vim
go to fontawesome cheatsheet: https://fontawesome.com/cheatsheet/free/regular
in insert mode of vim, <C-v> u <the unicode of the font>

or search in here: https://fontawesome.com/icons?d=gallery

#### vim misc
some vim build doesn't have +clipboard, it annoys me
sudo apt install vim-gtk3 # replace default build with more robust build

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

And it could tell PS4 controller and pass audio to this device, nice

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
```
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

#### add user
```
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

#### Nvidia Driver
from: https://docs.kali.org/general-use/install-nvidia-drivers-on-kali-linux

#### torrent
apt install transmission # torrent file

#### screen temperature adjust
https://github.com/jonls/redshift
http://jonls.dk/redshift/
apt install redshift
~/.config/redshift.conf

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
Plus if I really need to type Chinese in Terminal, Gnomal-Terminal has good internal font support for Chinese.
```
    sudo apt installl ibus-pinyin
    sudo apt install ibus-sunpinyin
    ibus-setup # config to using <C-space> to change imput method
    ibus restart
    reboot
```

#### fix firefox veritical tear in i3
disable hardware acceleration
from: https://forum.manjaro.org/t/firefox-screen-tearing-i3wm-compton/81794
In summary, I changed and added these options to my ~/.config/compton.conf. It seems to have fix the issue.
```
    backend = "glx";
    vsync = "true";
    glx-swap-method = 2;
```

#### firefox
vimium, vim like operation
adblock, adblock
windowed, could float youtube video

#### screenshot
apt install scrot # and bind it to PrtSc
apt install gnome-screenshot


#### others
using selection to clipboard and mouse middle key to paste is reasonable

Hey, I am happy that I don't need a driver install to make PS4 controller earphone in Kali

using mkdir /some/directory/to/somewhere/ and then cd !$

apt install speedtest-cli   # for internet speed test from remote
speedtest

apt install iperf  # for testing LAN speed
iperf -s # server
iperf -c <server-IP> # client mod
kali@kali:~$ iperf -s
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size:  128 KByte (default)
------------------------------------------------------------
[  1] local 192.168.1.35 port 5001 connected with 192.168.1.16 port 51220
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-10.1839 sec  83.9 MBytes  69.1 Mbits/sec
