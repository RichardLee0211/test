2019/09/09 Tues
--------------------------------------------------------------------------------

don't really remember how I get this vm file
the root password is in description part of VM file

iwconfig: interface wireless config
ifconfig: interface config

route -n

last night, Hu's macOS misbehaved.
MacOS user manager is not account for the Linux way to manage user

apt-get in kali
I have nothing to complain about apt
GNOME desktop environment
I really don't care about Desktop Environment, I wanna do it in Terminal

some cool devices:
https://docs.kali.org/kali-on-arm/

2019/09/10 Wed
--------------------------------------------------------------------------------

some setting up needs reboot

#### user management
on this Kali OS
root:toor, yeah, spell root backward

adduser wenchen
passwd wenchen
visudo # to add wenchen to sudo group

userdel
users

#### how to take screenshot on Kali
just PrtSc key save to ~/Picture

#### need a better PDF reader

#### others
xdg-open
terminal.sexy is good tool to export .Xresources file

#### using i3-gaps
from https://gist.github.com/audrummer15/c33688b5a148179214c08b0518f18ac3
```
    sudo apt-get update
    sudo apt-get install -y git build-essential autoconf pkg-config # fresh systems only
    sudo apt-get install -y i3 # to get dependencies
    git clone https://www.github.com/Airblader/i3 i3-gaps
    cd i3-gaps
    autoreconf --force --install
    rm -rf build/
    mkdir -p build && cd build/
    # Disabling sanitizers is important for release versions!
    # The prefix and sysconfdir are, obviously, dependent on the distribution.

    sudo apt-get install -y libxcb-shape0-dev libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev xcb libxcb1-dev libxcb-icccm4-dev libyajl-dev libev-dev libxcb-xkb-dev libxcb-cursor-dev libxkbcommon-dev libxcb-xinerama0-dev libxkbcommon-x11-dev libstartup-notification0-dev libxcb-randr0-dev libxcb-xrm0 libxcb-xrm-dev

    ../configure --prefix=/usr --sysconfdir=/etc --disable-sanitizers
    make -j8 && make install
```


#### xdg-open
https://wiki.archlinux.org/index.php/Xdg-utils
