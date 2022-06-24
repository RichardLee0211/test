####
some other convenient tools

- rclone
from: https://it.stonybrook.edu/help/kb/using-rclone-to-backup-data
from: https://github.com/rclone/rclone
using cloud storage for project backup ?, this is so cool of a project

- vpn
from: https://it.stonybrook.edu/services/vpn
why use VPN when I can use Teamviwer?
I don't have great understanding of VPN program on my mac Machine
Don't know how to control it

- sshfs
from: https://it.stonybrook.edu/help/kb/using-sshfs
from: https://osxfuse.github.io/
```shell
  ## this is more convenient than ssh, scp, rsync, sftp(and sftp GUI)
  sshfs vislab@130.245.4.102:/home/vislab/ ~/vislab_mnt  ## or with some opnion
  sshfs -o auto_cache,reconnect vislab@130.245.4.102:/home/vislab/ ~/vislab_mnt
  fusermount -u /Volumes/vislab  ## or use umount
  sudo umount /Volumes/vislab
```

from: https://github.com/osxfuse/osxfuse/issues/828
title: macOS 11.5 - The system extension required for mounting macFUSE volumes could not be loaded.

disable SIP and
clear /Library/Caches and /System/Library/Caches works
works for me

in vislab environment
it's weird, copy file to SSHFS (upload) using rsync -ah --progress at 20MB/s, respectable
However, copy file from SSHFS using the same command at 1~2MB/s, prrrr
playing 1080P video is choppy

in home environment, try sshfs at my apartment with harddrive attached

```shell
## defer_permissions let me read other hardware on ssh target
sshfs -o auto_cache,reconnect,defer_permissions  wenchen@192.168.1.39:/ ~/mnt_vislab
```

upload at 45MB/s using rsync
download at 2MB/s using rsync

- try nfs

```shell
  ## Ubuntu nfs server
  sudo apt update
  sudo apt install nfs-kernel-server
  sudo cat << EOF >> /etc/exports
  /home/vislab/NFS_Share          *(rw,sync,no_root_squash,no_subtree_check)
  EOF
  sudo systemctl restart nfs-server.service
  sudo ufw status

  ## macOS client

  (base) ➜  Report git:(master) ✗ showmount -e 130.245.4.102
  Exports list on 130.245.4.102:
  /home/vislab/NFS_Share              *

  (base) ➜  Report git:(master) ✗
  sudo mount -t nfs -o resvport 130.245.4.102:/home/vislab/NFS_Share ~/NFS_mnt
  ## reserved port

  (base) ➜  Report git:(master) ✗ df -h
  Filesystem                                            Size   Used  Avail Capacity iused      ifree %iused  Mounted on
  ...
  /dev/disk3s1                                         931Gi  870Gi   61Gi    94%  244914 9765332526    0%   /Volumes/SSD_1TB
  vislab@130.245.4.102:/home/vislab/                   219Gi   54Gi  154Gi    26%  623060   13999660    4%   /Users/wenchen/vislab_mnt
  130.245.4.102:/home/vislab/NFS_Share                 219Gi   54Gi  154Gi    26%  623060   13999660    4%   /Users/wenchen/NFS_mnt

  ## speed is good, can hit 100MB/sec
  (base) ➜  Report git:(master) ✗ rsync -ah --progress /Users/wenchen/NFS_mnt/test001.mkv  ./test001.mkv
  building file list ...
  1 file to consider
  test001.mkv
       917.11M 100%   51.09MB/s    0:00:17 (xfer#1, to-check=0/1)

  sent 917.22M bytes  received 42 bytes  52.41M bytes/sec
  total size is 917.11M  speedup is 1.00

  sudo umount ~/NFS_mnt
```

- try nfs at home


(base) ➜  Report git:(master) ✗ sudo mount -t nfs -o resvport 192.168.1.39:/home/wenchen ~/mnt_NFS
download at 25MB/s with rsync
upload   at 30MB/s with sudo rsync

NFS needs Kerberos for authorization, which I don't wanna set up

- SMB Samba server

from: https://linuxconfig.org/how-to-configure-samba-server-share-on-ubuntu-22-04-jammy-jellyfish-linux
```shell
  $ sudo apt update
  $ sudo apt install tasksel
  $ sudo tasksel install samba-server

  $ sudo smbpasswd -a wenchen   ## creat smb user the same name as Linux user

  $ sudo cp /etc/samba/smb.conf /etc/samba/smb.conf_backup
  $ sudo bash -c 'grep -v -E "^#|^;" /etc/samba/smb.conf_backup | grep . > /etc/samba/smb.conf'

  # sudo mkdir /var/samba
  # sudo chmod 777 /var/samba/

  $ sudo vim  /etc/samba/smb.conf
  $ sudo systemctl restart smbd
```

```/etc/samba/smb.conf
[homes]
   comment = Home Directories
   browseable = yes
   read only = no
   create mask = 0700
   directory mask = 0700
   valid users = %S
# [public]
#   comment = public anonymous access
#   path = /var/samba/
#   browsable =yes
#   create mask = 0660
#   directory mask = 0771
#   writable = yes
#   guest ok = yes
```


download at 40MB/sec
upload   at 25MB/sec

My objective:
a remote file system I can access files, because laptop storage have some limits
edit them using local or remote machine,
upload and download files, and hold large project folders(100GB to start with, go to a few TB)
so that everyfile is in one place (a single harddirve?? )

if I just using normal harddrives to store projects file, then files are tied to
one drive and its backup drive


- openmediavault

- freeNAS?? for separated storage server??
from: https://www.truenas.com/truenas-scale/
based on debian

- unraid and ZFS
cost money
unraid OS can run VM and container, this is so cool
from: https://www.youtube.com/watch?v=7h0JVS0en3U&ab_channel=HardwareHaven
title: Convert an Old Gaming PC to a Home Server using Unraid - (SMB, Terraria, Home Assistant, Jellyfin)
Unraid really provides some features like Container and VM
but do I need another metal box in my office ?

from: https://www.youtube.com/watch?v=LuJYMCbIbPk&ab_channel=LinusTechTips
title: 2 Gaming Rigs, 1 Tower - Virtualized Gaming Build Log
and linus used unraidOS to do this job

- VM layer
kvm and qemu
to virtualize server hardware ?

from: https://www.youtube.com/watch?v=BgZHbCDFODk&ab_channel=VeronicaExplains
title: QEMU/KVM for absolute beginners
I like this style, so good, a lot of jokes
but this is using KVM in Linux, just like using VMware

from: https://www.youtube.com/watch?v=_JTEsQufSx4&ab_channel=Coodos
title: Don't Dual Boot, Do this instead | MacOS Big Sur and Windows 10 KVM SINGLE GPU OVMF Passthrough
tricky to get GPU passthrough into KVM and QEMU

Virtual Mechine Host
```shell
  egrep -c '(vmx|svm)' /proc/cpuinfo   ## check cpu virtualization cap

  ## duckduckgo install instruction for ubuntu
  # qemu-kvm: the emulator itself
  # libvirt-daemon: runs virtualization in background
  # bridge-utils: important networking dependencies
  # virt-manager: the graphical program, by Red Hat

  ##
  sudo usermod -aG libvirt vkc
  sudo usermod -aG kvm vkc

  sudo systemctl start libvirtd
  sudo systemctl enable libvirtd

  # virt-manager(GUI) and virsh -h (CLI)
  #
  # KVM (Linux Kernel, Free)
  # VirtualBox (from Oracle)
  # VMware (from VMware)
  # Hyper-V (from Microsoft)
```

- TrueNAS on Proxmox
from: https://www.youtube.com/watch?v=M3pKprTdNqQ&ab_channel=TheDigitalLife
title: How to run TrueNAS on Proxmox?

from: https://www.proxmox.com/en/
