rice my Linux
================================================================================

this is for the rise Linux

a very cool [time line](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg)

reading [GNU/Linux ricing](https://wiki.installgentoo.com/index.php/GNU/Linux_ricing)

[i3-gaps](https://github.com/Airblader/i3)

Log
================================================================================

well, I gonna try it anyway.

search download and install VirtualBox
search download and install Arch Linux

[arch wiki](https://wiki.archlinux.org/index.php/Frequently_asked_questions)

[general recommendations](https://wiki.archlinux.org/index.php/General_recommendations)

followed this wiki to build my ArchLinux and fall, the login interface display gabage

the default pdf view in Ubuntu is "evince", which support hjkl vim move key-map

#### 2019/09/23

Top 10 Linux Job Interview Questions
From youtube tutorialLinux
Q1: Kernel Version Checking
uname -a

Q2: IP address checking
Ifconfig
Ip adds show eth0

Q3: Free disk space checking
df -ah
Disk free

Q4: Manage services on a system
new: systemd
Systemctl status udev

old:
Service dev status

Q5: check fold’s size
Du -sh ~/Code
Disk usage

Q6: check for open ports
Netstat -tulpn

Q7: CPU usage of a process
Ps aux | grep nginx
Top

Q8: Dealing with Mounts
Ls /mnt
Mount /dev/sda2 /mnt
More /etc/fsfile

Q9: help list
Man <command>
<Command> —help
Google.com

#### Some notes on youtube DistroTube First Rice

For any terminal using Xresource
Xrdb -merge ~/.Xresource

Alsamixer
GIMP, the photo editing software
Powerline
Cmus, a terminal music player
Unicode character with fontawesome, or other font
Just search unicode music
 vi mode in bash and zsh
mpd ncmpcpp mpc
Pandoc

#### logout using commnand line
Logout with ‘pkill x’, OMG
Pkill - u ${USERNAME}
Or
Gnome-session-quit

Use stow to place dot in  ~/.config

#### Linux from scratch

here: http://www.linuxfromscratch.org/
what could help more to build a Linux from scratch

Here: http://www.linuxfromscratch.org/blfs/view/svn/index.html
A good list of Linux package and utility

BLFS
================================================================================
http://www.linuxfromscratch.org/blfs/
http://www.linuxfromscratch.org/blfs/view/9.0/

I mainly use this manual to check my knowledge about Linux Utility

Ch04 Security
--------------------------------------------------------------------------------

TODO:

Ch05 File system and Disk Management
--------------------------------------------------------------------------------

most of tools are to handle filesystem, not very useful for my case

Ch06 Editors
--------------------------------------------------------------------------------

I have vim, which is enough as editor

Ch07 shells
--------------------------------------------------------------------------------

most likely use Bash and Zsh

Ch08 Virtualization
--------------------------------------------------------------------------------

TODO: this is a tool I have never integrated into my system, since I use Linux in VMware

III. General Libraries and Utilities
--------------------------------------------------------------------------------

Ch09 General Libraries
--------------------------------------------------------------------------------
Ch10 Graphics and Font Libraries
--------------------------------------------------------------------------------
Ch11 General Utilities
--------------------------------------------------------------------------------
Ch12 System Utilities
--------------------------------------------------------------------------------
Ch13 Programming
--------------------------------------------------------------------------------

IV. Networking
--------------------------------------------------------------------------------
Ch14 Connecting to a Network
--------------------------------------------------------------------------------
Ch15 Networking Programs
--------------------------------------------------------------------------------
Ch16 Networking Utiliteis
--------------------------------------------------------------------------------
Ch17 Networking Libraries
--------------------------------------------------------------------------------
Ch18 Text Web Browers
--------------------------------------------------------------------------------
Ch19 Mail/News Clients
--------------------------------------------------------------------------------

V. Servers
--------------------------------------------------------------------------------

Ch20 Major Servers
--------------------------------------------------------------------------------
Apache-2.4.41
BIND-9.14.5
ProFTPD-1.3.6
vsftpd-3.0.3
Ch21 Mail Server Software
--------------------------------------------------------------------------------
Dovecot-2.3.7.2
Exim-4.92.1
Postfix-3.4.6
sendmail-8.15.2
Ch22 Databases
--------------------------------------------------------------------------------
Berkeley DB-5.3.28
lmdb-0.9.24
MariaDB-10.4.7
PostgreSQL-11.5
SQLite-3.29.0
Ch23 Other Server Software
--------------------------------------------------------------------------------
OpenLDAP-2.4.48
Unbound-1.9.2

 VI. X + Window and Display Managers
--------------------------------------------------------------------------------

     24. X Window System Environment
     25. X Libraries
     26. Display Managers
     27. Window Managers
     28. Icons

 VII. KDE
     29. Introduction to KDE
     30. KDE Frameworks 5
     31. KDE Frameworks 5 Based Applications
     32. KDE Plasma 5

 VIII. GNOME
--------------------------------------------------------------------------------
     33. GNOME Libraries and Desktop
     34. GNOME Applications

 IX. Xfce
     35. Xfce Desktop
     36. Xfce Applications
 X. LXDE
     37. LXDE Desktop
     38. LXDE Applications

 XI. X Software
--------------------------------------------------------------------------------

Ch39. Office Programs
--------------------------------------------------------------------------------
     LibreOffice
     ...

Ch40. Graphical Web Browsers
--------------------------------------------------------------------------------
     Firefox
     ...
Ch41. Other X-based Programs
--------------------------------------------------------------------------------
     feh
     rxvt
     ...

 XII. Multimedia
--------------------------------------------------------------------------------
Ch42. Multimedia Libraries and Drivers
--------------------------------------------------------------------------------
     alsa
     ...
Ch43. Audio Utilities
--------------------------------------------------------------------------------
Ch44 Video Utilities
--------------------------------------------------------------------------------
     FFmpeg
     MPlayer
     VLC
Ch45. CD/DVD-Writing Utilities
--------------------------------------------------------------------------------
XIII. Printing, Scanning and Typesetting
--------------------------------------------------------------------------------

System Administrator's Guild from redhat.com
================================================================================

Ch10 Managing Services with systemd
