This is raspberry pi 3 Pen journey

get kali-pi image from: https://re4son-kernel.com/
using balenaEtcher to burn to SD card. I think dd would do the same thing, untested.
The image only leave my 300MB free space. Usually it is enough for hacking info.
Yet I can upgrade my system since upgrade would take 1GB space. (I would not need to do that)

bind a battery bank with RPi making it portable
for my feelings, don't use wired keyboard or mouse or HDMI.
the mount of cables on desktop would be massive

I write some notes on RPi and it died. Has to reburn the SD card.
Don't know if it's the partition resize or apt upgrade?: this is upgrade, re4son-kernel, do not do kernel upgrade
from: https://null-byte.wonderhowto.com/how-to/build-beginner-hacking-kit-with-raspberry-pi-3-model-b-0184144/

using kalipi-config to config kalipi
and you could use it to set up wifi

see, I wanna to ethernet cable for communication between my macbook and RPi
and use wifi card for some PenTest

TODO: to run RPi Headless(without a monitor, keyboard and mouse)
- using macOS Sharing setting
- Yet, without internet, say your are travelling in a plane where there is no internet access
- eduroam wifi forbit internet sharing

and nmap -n -sP 192.168.2.1/24 does not work on kalipi

MBP15 charger issue is bothering me

#### network
I wanna run Kalipi headless, which means two ways
##### 1. share internet with macOS
connect raspberry pi from ethernet cable
enable ethernet sharing in Apple->preference->sharing
nmap -n -sP 192.168.2.2/24 # scan the point to point network
ssh root@192.168.2.2
I tried ssh RPi via bluetooth, here: https://hacks.mozilla.org/2017/02/headless-raspberry-pi-configuration-over-bluetooth/
it should be feasible yet masOS2020 refuse to connect to RPi. It disconnect automatically

##### 2. don't share internet
TODO: Kalipi and macOS using its own connection



setting up ethernet
vim /etc/network/interfaces
```
    auto eth0
    iface eth0 inet static
    address 192.168.2.100/24
    gateway 192.168.2.1
```

echo "nameserver 8.8.8.8" > /etc/resolv.conf
ping google.com # didn't work in Kalipi

apt install zsh

from: https://null-byte.wonderhowto.com/how-to/top-10-things-do-after-installing-kali-linux-0186450/
TODO: maybe check out sync: https://github.com/syncthing/syncthing
TODO: change SSH keys
```
    cd /etc/ssh/
    dpkg-reconfigure openssh-server
```
apt

#### Hacking Wi-Fi in Seconds with Airgeddon & Parrot Security OS
from: https://www.youtube.com/watch?v=ejTPWPGP0GA
WPA WPA2

#### Use Nmap for Tactical Network Reconnaissance [Tutorial]
from: https://www.youtube.com/watch?v=ltEFbi_I2KY
TODO: macOS ifconfig explain
