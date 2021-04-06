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
--------------------------------------------------------------------------------
```man systemctl
    systemctl enable name.service
    systemctl disable name.service
    systemctl status name.service
    systemctl list-unit-files --type service
    systemctl list-dependencies --after
    systemctl list-dependencies --before
```

a list of servicen within Kali
```shell
    UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
    accounts-daemon.service            loaded active running Accounts Service
    alsa-restore.service               loaded active exited  Save/Restore Sound Card State
    alsa-state.service                 loaded active running Manage Sound Card State (restore and store)
    binfmt-support.service             loaded active exited  Enable support for additional executable binary formats
    colord.service                     loaded active running Manage, Install and Generate Color Profiles
    console-setup.service              loaded active exited  Set console font and keymap
    cron.service                       loaded active running Regular background program processing daemon
    dbus.service                       loaded active running D-Bus System Message Bus
    gdm.service                        loaded active running GNOME Display Manager
    haveged.service                    loaded active running Entropy daemon using the HAVEGE algorithm
    ifupdown-pre.service               loaded active exited  Helper to synchronize boot up for ifupdown
    keyboard-setup.service             loaded active exited  Set the console keyboard layout
    kmod-static-nodes.service          loaded active exited  Create list of required static device nodes for the current kernel
    ModemManager.service               loaded active running Modem Manager
    networking.service                 loaded active exited  Raise network interfaces
    NetworkManager.service             loaded active running Network Manager
    polkit.service                     loaded active running Authorization Manager
    rsyslog.service                    loaded active running System Logging Service
    rtkit-daemon.service               loaded active running RealtimeKit Scheduling Policy Service
    smartd.service                     loaded failed failed  Self Monitoring and Reporting Technology (SMART) Daemon
    stunnel4.service                   loaded active exited  LSB: Start or stop stunnel 4.x (TLS tunnel for network daemons)
    systemd-journal-flush.service      loaded active exited  Flush Journal to Persistent Storage
    systemd-journald.service           loaded active running Journal Service
    systemd-logind.service             loaded active running Login Service
    systemd-modules-load.service       loaded active exited  Load Kernel Modules
    systemd-random-seed.service        loaded active exited  Load/Save Random Seed
    systemd-remount-fs.service         loaded active exited  Remount Root and Kernel File Systems
    systemd-sysctl.service             loaded active exited  Apply Kernel Variables
    systemd-sysusers.service           loaded active exited  Create System Users
    systemd-timesyncd.service          loaded active running Network Time Synchronization
    systemd-tmpfiles-setup-dev.service loaded active exited  Create Static Device Nodes in /dev
    systemd-tmpfiles-setup.service     loaded active exited  Create Volatile Files and Directories
    systemd-udev-trigger.service       loaded active exited  udev Coldplug all Devices
    systemd-udevd.service              loaded active running udev Kernel Device Manager
    systemd-update-utmp.service        loaded active exited  Update UTMP about System Boot/Shutdown
    systemd-user-sessions.service      loaded active exited  Permit User Sessions
    udisks2.service                    loaded active running Disk Manager
    upower.service                     loaded active running Daemon for power management
    user-runtime-dir@1000.service      loaded active exited  User Runtime Directory /run/user/1000
    user-runtime-dir@132.service       loaded active exited  User Runtime Directory /run/user/132
    user@1000.service                  loaded active running User Manager for UID 1000
    user@132.service                   loaded active running User Manager for UID 132
    wpa_supplicant.service             loaded active running WPA supplicant

    LOAD   = Reflects whether the unit definition was properly loaded.
    ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
    SUB    = The low-level unit activation state, values depend on unit type.

    43 loaded units listed. Pass --all to see loaded but inactive units, too.
    To show all installed unit files use 'systemctl list-unit-files'.
```
