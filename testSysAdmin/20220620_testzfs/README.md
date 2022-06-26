from: https://discourse.ubuntu.com/t/testing-the-self-healing-of-zfs-on-ubuntu-20-04/26189

$ sudo apt install zfsutils-linux
└> zfs --version
zfs-0.8.3-1ubuntu12.14
zfs-kmod-2.0.6-1ubuntu2.1
(base) ┌[wenchen☮wenchen-MS-7845]-(~)
└> zpool --version
zfs-0.8.3-1ubuntu12.14
zfs-kmod-2.0.6-1ubuntu2.1


testing with stripped disks
```shell
    for FAKE_DISK in disk1.img disk2.img
    do
        dd if=/dev/zero of=`pwd`/$FAKE_DISK bs=1M count=100
    done

    ZFS_TEST_DIR=`pwd`
    sudo zpool create test_pool_striped \
      `pwd`/disk1.img \
      `pwd`/disk2.img

    zpool list
    zpool status test_pool_striped
    zfs mount   ## check mount point

    sudo chown $USER /test_pool_striped
    cd /test_pool_striped
    echo "We are playing with ZFS. It is an impressive filesystem that can self-heal, but even it has limits." > text.txt

    └> sha1sum text.txt
    c1ca4def6dc5d82fa6de97d2f6d429045e4f4065  text.txt

    cd $ZFS_TEST_DIR
    dd if=/dev/zero of=$ZFS_TEST_DIR/disk1.img bs=1M count=100  ## corrupt data
    ## cd /test_pool_striped; cat test.txt; sha1sum test.txt; ## seem to be fine

    sudo zpool export test_pool_striped      ## zpool list, offline the volumn
    dd if=/dev/zero of=$ZFS_TEST_DIR/disk1.img bs=1M count=100  ## corrupt it again

	└> sudo zpool import -d $ZFS_TEST_DIR/disk2.img  ## also used when restarting
	   pool: test_pool_striped
	     id: 5923254958472573571
	  state: ONLINE
	 action: The pool can be imported using its name or numeric identifier.
	 config:
	        test_pool_striped                                                      ONLINE
	          /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing/disk1.img  ONLINE
	          /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing/disk2.img  ONLINE

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing)
	└> zpool list
	no pools available

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing)
	└> dd if=/dev/zero of=$ZFS_TEST_DIR/disk1.img bs=1M count=100
	100+0 records in
	100+0 records out
	104857600 bytes (105 MB, 100 MiB) copied, 0.22942 s, 457 MB/s

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing)
	└> sudo zpool import -d $ZFS_TEST_DIR/disk2.img
	   pool: test_pool_striped
	     id: 5923254958472573571
	  state: ONLINE
	 status: One or more devices contains corrupted data.
	 action: The pool can be imported using its name or numeric identifier.
	   see: http://zfsonlinux.org/msg/ZFS-8000-4J
	 config:

	        test_pool_striped                                                      ONLINE
	          /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing/disk1.img  UNAVAIL  corrupted data
	          /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing/disk2.img  ONLINE

     sudo zpool import test_pool_striped -d $ZFS_TEST_DIR/disk2.img  ## reimport, take a long time

```

testing with mirrored disks
```shell
	for FAKE_DISK in disk1.img disk2.img
	do
	    dd if=/dev/zero of=`pwd`/$FAKE_DISK bs=1M count=100
	done

	sudo zpool create test_pool_with_mirror mirror \
	  `pwd`/disk1.img \
	  `pwd`/disk2.img

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing02)
	└> zpool list
	NAME                    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
	test_pool_with_mirror    80M   114K  79.9M        -         -     5%     0%  1.00x    ONLINE  -

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing02)
	└> zpool status test_pool_with_mirror
	  pool: test_pool_with_mirror
	 state: ONLINE
	  scan: none requested
	config:

	        NAME                                                                       STATE     READ WRITE CKSUM
	        test_pool_with_mirror                                                      ONLINE       0     0     0
	          mirror-0                                                                 ONLINE       0     0     0
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk1.img  ONLINE       0     0     0
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk2.img  ONLINE       0     0     0

	errors: No known data errors

	└> dd if=/dev/zero of=$ZFS_TEST_DIR/disk1.img bs=1M count=100     ## corruption
	100+0 records in
	100+0 records out
	104857600 bytes (105 MB, 100 MiB) copied, 0.22982 s, 456 MB/s

	└> sudo zpool import -d $ZFS_TEST_DIR/disk2.img
	   pool: test_pool_with_mirror
	     id: 11827935519407400985
	  state: ONLINE
	 status: One or more devices contains corrupted data.
	 action: The pool can be imported using its name or numeric identifier.
	   see: http://zfsonlinux.org/msg/ZFS-8000-4J
	 config:

	        test_pool_with_mirror                                                      ONLINE
	          mirror-0                                                                 ONLINE
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk1.img  UNAVAIL  corrupted data
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk2.img  ONLINE

	└> sudo zpool import test_pool_with_mirror -d $ZFS_TEST_DIR/disk2.img
	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing02)
	└> zpool status test_pool_with_mirror
	  pool: test_pool_with_mirror
	 state: ONLINE
	status: One or more devices could not be used because the label is missing or
	        invalid.  Sufficient replicas exist for the pool to continue
	        functioning in a degraded state.
	action: Replace the device using 'zpool replace'.
	   see: http://zfsonlinux.org/msg/ZFS-8000-4J
	  scan: none requested
	config:

	        NAME                                                                       STATE     READ WRITE CKSUM
	        test_pool_with_mirror                                                      ONLINE       0     0     0
	          mirror-0                                                                 ONLINE       0     0     0
	            15652149542584519820                                                   UNAVAIL      0     0     0  was /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk1.img
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk2.img  ONLINE       0     0     0

	errors: No known data errors

	cd $ZFS_TEST_DIR
	dd if=/dev/zero of=`pwd`/disk3.img bs=1M count=100

	sudo zpool replace test_pool_with_mirror $ZFS_TEST_DIR/disk1.img $ZFS_TEST_DIR/disk3.img

	(base) ┌[wenchen☮wenchen-MS-7845]-(~/Downloads/20220620_testZFS/test_zfs_healing02)
	└> zpool status test_pool_with_mirror
	  pool: test_pool_with_mirror
	 state: ONLINE
	  scan: resilvered 274K in 0 days 00:00:00 with 0 errors on Mon Jun 20 18:12:53 2022
	config:

	        NAME                                                                       STATE     READ WRITE CKSUM
	        test_pool_with_mirror                                                      ONLINE       0     0     0
	          mirror-0                                                                 ONLINE       0     0     0
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk3.img  ONLINE       0     0     0
	            /home/wenchen/Downloads/20220620_testZFS/test_zfs_healing02/disk2.img  ONLINE       0     0     0

	errors: No known data errors

```

#### benchmark
have a base line operation
2 mirrored disks: 200 MB/s write
2x2 striped and mirrored disks: 350 MB/s write
this is so cool

```shell
(base) ➜  _Music
rsync -ha --progress '/Volumes/SSD_1TB/_Music/Daft Punk - Discography (1996-2007) [Flac][WwW.LoKoTorrents.CoM]' wenchen@192.168.1.39:/media/wenchen/work4/
	building file list ...
	293 files to consider
	...
	sent 5.45G bytes  received 6.08K bytes  39.07M bytes/sec
	total size is 5.45G  speedup is 1.00

$ rsync ...  ## when do with a ZFS two disks mirror pool
    ...
	8K bytes  42.41M bytes/sec
	total size is 5.45G  speedup is 1.00
	rsync -ha --progress  wenchen@192.168.1.39:~/zfs_tank/  30.73s user 36.34s system 52% cpu 2:08.88 total

## I guess network is the issue
$ rsync ... ## when do with a ZFS with 2x2 striped mirror pool
...
sent 5.45G bytes  received 6.08K bytes  33.13M bytes/sec
total size is 5.45G  speedup is 1.00

```

####
from: https://timor.site/2021/11/creating-fully-encrypted-zfs-pool/
title: Creating fully encrypted ZFS pool
this blog style is so good

from: https://gist.github.com/dlangille/ac4fe6a1422b346a7196d2b996daa363
title: dlangille/Samsung SSD 860 EVO 1TB S59VNJ0N631973D

smartctl output

# zpool to create pool
# zfs for dataset/foldr on the pool
zfs create -o encryption=on -o keylocation=prompt -o keyformat=passphrase banshee/encrypted

from: https://arstechnica.com/gadgets/2021/06/a-quick-start-guide-to-openzfs-native-encryption/
title: A quick-start guide to OpenZFS native encryption
a good one

#### use the right disks
```shell
	fdisk -l  ## find disk with label liks /dev/sda, not fix between reboots

	└> ls /dev/disk/by-id
	...
	ata-Samsung_SSD_840_EVO_1TB_S1D9NSAF768927A
	ata-WDC_WD40EZAZ-00SF3B0_WD-WXXXXXXXTPF4
	ata-WDC_WD40EZAZ-00SF3B0_WD-WXXXXXXXFDVX
	ata-WDC_WD40EZAZ-00SF3B0_WD-WXXXXXXXA6Z7
	ata-WDC_WD40EZAZ-00SF3B0_WD-WXXXXXXX7E38


	└> lsblk -o NAME,SIZE,SERIAL,LABEL,FSTYPE
	NAME          SIZE SERIAL               LABEL      FSTYPE
	loop0           4K                                 squashfs
	sda           3.7T WD-WXXXXXXXTPF4
	├─sda1         16M
	└─sda2        3.7T                      myStore4B  exfat
	sdb           3.7T WD-WXXXXXXX7E38
	sdc           3.7T WD-WXXXXXXXFDVX
	└─sdc1        3.7T                      work4      exfat
	sdd           3.7T WD-WXXXXXXXA6Z7
	└─sdd1        3.7T                      netStore4B exfat

	sde         931.5G S1D9NXXXXXX927A
	├─sde1        200M                      EFI        vfat
	├─sde2         16M
	├─sde3      589.5G                                 ntfs
	└─sde4      341.8G                                 ext4
	nvme0n1     953.9G TPBF2XXXXXXXXXXX1528
	├─nvme0n1p1     1M
	├─nvme0n1p2   513M                                 vfat
	└─nvme0n1p3 953.4G                                 ext4


```

on my own machine
```shell
# mkdir -p /media/wenchen/zfs_tank
mkdir -p $HOME/zfs_tank
sudo zpool create -m $HOME/zfs_tank  \
		-o feature@encryption=enabled \
		-O encryption=on \
		-O keyformat=passphrase \
		tank \
		mirror \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxx7E38 \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxFDVX

└> df -h
Filesystem      Size  Used Avail Use% Mounted on
...
tmpfs           3.2G   20K  3.2G   1% /run/user/125
tmpfs           3.2G   32K  3.2G   1% /run/user/1000
/dev/sda2       3.7T  844G  2.9T  23% /media/wenchen/myStore4B
/dev/sdd1       3.7T  2.2T  1.5T  60% /media/wenchen/netStore4B
/dev/nvme0n1p3  938G  482G  409G  55% /media/wenchen/78d2b7e9-eae2-4e62-afec-4fe762f2f9ce
tank            3.6T  256K  3.6T   1% /home/wenchen/zfs_tank

└> zpool list
NAME   SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
tank  3.62T  5.09G  3.62T        -         -     0%     0%  1.00x    ONLINE  -

└> zfs list
NAME   USED  AVAIL     REFER  MOUNTPOINT
tank  5.09G  3.51T     5.09G  /home/wenchen/zfs_tank

└> zpool status
  pool: tank
 state: ONLINE
  scan: none requested
config:

        NAME                                          STATE     READ WRITE CKSUM
        tank                                          ONLINE       0     0     0
          mirror-0                                    ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxx7E38  ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxFDVX  ONLINE       0     0     0

errors: No known data errors

└> sudo zpool events tank -v
TIME                           CLASS
Jun 21 2022 00:34:57.990432377 sysevent.fs.zfs.history_event
        version = 0x0
        class = "sysevent.fs.zfs.history_event"
        pool = "tank"
        pool_guid = 0xf9b7XXXXXXXXXXXX
        pool_state = 0x0
        pool_context = 0x0
        history_hostname = "wenchen-MS-7845"
        history_internal_str = "pool version 5000; software version zfs-0.7.0-XXXXXXXXXXXXXXX-dist; uts wenchen-MS-7845 XXXXXXXXX-gener


$ sudo zfs set mountpoint=<path> <pool_name>

$ zfs create poolname/datasetname
$ chown –R username:groupName /poolname/datasetname

└> zpool iostat
              capacity     operations     bandwidth
pool        alloc   free   read  write   read  write
----------  -----  -----  -----  -----  -----  -----
tank        5.09G  3.62T      0      8     16  3.61M

└> zpool iostat -v 15   			## every 15 seconds, or
└> watch -n 15 zpool iostat -v      ## maybe this is better
                                                capacity     operations     bandwidth
pool                                          alloc   free   read  write   read  write
--------------------------------------------  -----  -----  -----  -----  -----  -----
tank                                          5.09G  3.62T      0      8     16  3.50M
  mirror                                      5.09G  3.62T      0      8     16  3.50M
    ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxx7E38      -      -      0      4      8  1.75M
    ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxFDVX      -      -      0      4      8  1.75M
--------------------------------------------  -----  -----  -----  -----  -----  -----

zpool destroy poolname





# sudo zpool create NAME mirror VDEV1 VDEV2 mirror VDEV3 VDEV4
## or
# sudo zpool create NAME mirror VDEV1 VDEV2
# sudo zpool add NAME mirror VDEV3 VDEV4

sudo zpool add tank \
		mirror \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxTPF4 \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxA6Z7


$ zpool list
NAME   SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
tank  7.25T  5.09G  7.25T        -         -     0%     0%  1.00x    ONLINE  -

└> zpool status
  pool: tank
 state: ONLINE
  scan: none requested
config:
        NAME                                          STATE     READ WRITE CKSUM
        tank                                          ONLINE       0     0     0
          mirror-0                                    ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxx7E38  ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxFDVX  ONLINE       0     0     0
          mirror-1                                    ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxTPF4  ONLINE       0     0     0
            ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxA6Z7  ONLINE       0     0     0




## or use this
sudo zpool create -m $HOME/zfs_tank  \
		-o feature@encryption=enabled \
		-O encryption=on \
		-O keyformat=passphrase \
		tank \
		mirror \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxx7E38 \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxFDVX \
		mirror \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxTPF4 \
		/dev/disk/by-id/ata-WDC_WD40EZAZ-00SF3B0_WD-WXxxxxxxA6Z7

$ sudo zfs create -o encryption=on -o keylocation=prompt -o keyformat=passphrase test-pool/encrypted

$ sudo zfs mount -l test-pool/encrypted

```

```shell
## weird trick to generate key file
└> hexdump ~/.zfs-encrypt.key
0000000 0a14 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0000010 b80d XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0000020
└> sudo dd if=/dev/random of=$HOME/.zfs-encrypt.key bs=1 count=32
```

this is probably a right way to manage zfs folder permission
```shell
	GRP_NAME=<groupanem>
	ZFS_P=<zfs_path>
	sudo groupadd $GRP_NAME
	sudo usermod -a -G $GRP_NAME  $USER
	sudo mkdir $ZFS_P/data1
	sudo chgrp $GRP_NAME $ZFS_P/data1
	sudo chmod g+rwsx $ZFS_P/data1/
```

####
zfs snapshot zpoolname@snapshotname
zfs list -t snapshot
zfs rollback poolname@snapshotname
zfs destroy poolname@snapshotname

#### samba share
```shell
	mkdir /home/<username>/sambashare/

cat << EOF > /etc/samba/smb.conf
[homes]
   comment = Home Directories
   browseable = yes
   read only = no
   create mask = 0700
   directory mask = 0700
   valid users = %S

[MyShare]
   comment = nocomments
   path = /media/wenchen/
   browsable =yes
   read only = no
   writable = yes
   create mask = 0660
   directory mask = 0771
EOF

systemctl status smbd
systemctl enable smbd

```

####
some steps to mount zfs after reboots

└> zfs list
NAME   USED  AVAIL     REFER  MOUNTPOINT
tank   844G  6.30T      844G  /home/wenchen/zfs_tank

└> sudo zfs set mountpoint=/home/wenchen/zfs_tank tank

└> zfs get mountpoint,mounted tank
NAME  PROPERTY    VALUE                   SOURCE
tank  mountpoint  /home/wenchen/zfs_tank  local
tank  mounted     no                      -

zfs
└> sudo zfs load-key tank
Enter passphrase for 'tank':

└> sudo zfs mount tank

####
rclone

from: https://console.cloud.google.com/
from: https://rclone.org/drive/

```~/.config/rclone/rclone.conf
  [googletest001]
  type = drive
  scope = drive.appfolder
  root_folder_id = appDataFolder
  token = {"access_token":"yaXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","token_type":"Bearer","refresh_token":"1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXc","expiry":"2022-06-24T19:57:51.193352847-04:00"}
  team_drive =

  [gdrive_mount_crypt]
  type = crypt
  remote = googletest001:
  filename_encryption = standard
  directory_name_encryption = false
  password = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

 $ rclone about googletest001:
 Used:    23.533 GiB
 Trashed: 717.297 MiB
 Other:   955.929 MiB

 $ rclone copy --update --verbose --transfers 30 --checkers 8 \
 --contimeout 60s --timeout 300s --retries 3 --low-level-retries 10 --stats 1s \
 "/home/dave/Documents" "google-drive:LinuxDocs"


####
do zfs in the lab

 $ ls -alh /dev/disk/by-id
 total 0
 drwxr-xr-x 2 root root 280 Jun 24 10:38 .
 drwxr-xr-x 6 root root 120 Jun 24 10:38 ..
 lrwxrwxrwx 1 root root   9 Jun 24 10:38 ata-TOSHIBA-TR150_566B43XRKBZU -> ../../sdc
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 ata-TOSHIBA-TR150_566B43XRKBZU-part1 -> ../../sdc1
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 ata-TOSHIBA-TR150_566B43XRKBZU-part2 -> ../../sdc2
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 ata-TOSHIBA-TR150_566B43XRKBZU-part5 -> ../../sdc5
 lrwxrwxrwx 1 root root   9 Jun 24 10:38 ata-WDC_WD1002FBYS-02A6B0_WD-WMATV7489288 -> ../../sda
 lrwxrwxrwx 1 root root   9 Jun 24 10:38 ata-WDC_WD1002FBYS-02A6B0_WD-WMATV7650967 -> ../../sdb

 lrwxrwxrwx 1 root root   9 Jun 24 10:38 wwn-0x50014ee00244392b -> ../../sda
 lrwxrwxrwx 1 root root   9 Jun 24 10:38 wwn-0x50014ee057997a6c -> ../../sdb
 lrwxrwxrwx 1 root root   9 Jun 24 10:38 wwn-0x5e83a972004710a9 -> ../../sdc
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 wwn-0x5e83a972004710a9-part1 -> ../../sdc1
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 wwn-0x5e83a972004710a9-part2 -> ../../sdc2
 lrwxrwxrwx 1 root root  10 Jun 24 10:38 wwn-0x5e83a972004710a9-part5 -> ../../sdc5

 # one harddrive is broken, failed to assemble raid on vislab, shoot
 # new drive

sudo zpool create -m $HOME/zfs_tank  \
		-o feature@encryption=enabled \
		-O encryption=on \
		-O keyformat=passphrase \
		tank \
		mirror \
 /dev/disk/by-id/ata-WDC_WD1001FALS-00Y6A0_WD-WCATR9549724 \
 /dev/disk/by-id/ata-WDC_WD1002FBYS-02A6B0_WD-WMATV7650967
 ...

rsync ... ## backup a project folder

sent 27.12G bytes  received 30.18M bytes  16.73M bytes/sec
total size is 27.02G  speedup is 1.00
rsync -ah --progress ../20220127test vislab@130.245.4.102:~/zfs_tank/
293.64s user 769.92s system 63% cpu 27:44.53 total



####
ssh access machine behind firewall

server$ ssh -R 9091:localhost:22 client.example.egg
client$ ssh -p 9091 localhost

<ip1> vislab-MS-7845
<ip2> kali


step 1: vislab >>> || >>> kali
step 2: vislab <<< || <<< kali
step 3: vislab <<< || <<< kali <<< laptop via internet

-R [bind_addr:]port:host:hostport
   <remote port  > :<local side >

vislab $ ssh -R 9091:localhost:22 kali@<ip2>   ## connect from vislab to kali
kali   $ ssh -p 9091 vislab@localhost                  ## connect from kali to vislab
kali   $ netstat nr | less
  Active Internet connections (w/o servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State
  tcp        0      0 <kali_ip2>:ssh       <laptop_ip>:60379    ESTABLISHED   ## connection with laptop
  tcp        0      0 <kali_ip2>:ssh       <vislab_ip1>:37332     ESTABLISHED   ## connection with vislab
  tcp6       0      0 localhost:50440         localhost:9091          ESTABLISHED
  tcp6       0      0 localhost:9091          localhost:50440         ESTABLISHED

- with one command
ssh -o ProxyCommand="ssh -W localhost:9091" kali-server-onInternet ## not so much luck with this one

ssh -J kali@<kali_ip2> vislab@localhost -p 9091
  kali@<kali_ip2>'s password:
  vislab@localhost's password:

```~/.ssh/config
  Host AWS_VM
    HostName <public_ip>
    Port 22
    User ubuntu
    IdentityFile <key_fullpath>

  Host vislab
    HostName <vislab_ip1>
    Port 22
    User vislab

  Host vislab_p
    HostName localhost
    Port 9091
    User vislab
    ProxyJump AWS_VM
```
ssh vislab_p


- can I transfer files over ssh reverse proxy, sure I can
limited by 1GB Internet connnection

```~/.ssh/config
Host B
  HostName <proxy_ip>
  Port 22
  ForwardAgent yes
  User ubuntu
  IdentityFile <key_path>

Host C
  HostName localhost
  Port 9091
  User vislab
  # ProxyJump AWS_VM
  ProxyCommand ssh B -W %h:%p

```

```shell
(base) ➜  20220625_awstest sshfs C:/ ~/mnt_vislab
  vislab@localhost's password:
(base) ➜  20220625_awstest rsync --progress -ah file1 proxy_remote_file
  202.48M 100%   23.25MB/s    0:00:08 (xfer#1, to-check=0/1)
  sent 202.50M bytes  received 42 bytes  21.32M bytes/sec
  total size is 202.48M  speedup is 1.00
```

####
benchmart internet speed
from: https://www.speedtest.net/apps/cli

```shell
ubuntu@ip-172-31-31-124:~$ ./speedtest
     Speedtest by Ookla

       Server: Misaka Network, Inc. - Ashburn, VA (id = 30561)
          ISP: Amazon.com
      Latency:     0.71 ms   (0.04 ms jitter)
     Download:   892.08 Mbps (data used: 433.7 MB )
       Upload:   887.93 Mbps (data used: 398.5 MB )
  Packet Loss:     0.0%
   Result URL: https://www.speedtest.net/result/c/90d5c1e7-c4a9-4730-8116-31d09e2d072a
```

####
set up vnc

from: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-22-04
from: https://bytexd.com/how-to-install-configure-vnc-server-on-ubuntu/

VNC for Linux only,
not share the X-server,
Like X11 forwarding
with realVNC client on mac

```shell
  $ sudo apt install xfce4 xfce4-goodies
  $ sudo apt install tightvncserver
  $ vncserver   ## start new server

  You will require a password to access your desktops.

  Password:
  Warning: password truncated to the length of 8.
  Verify:
  Would you like to enter a view-only password (y/n)? n

  Warning: vislab-MS-7845:1 is taken because of /tmp/.X11-unix/X1
  Remove this file if there is no X server vislab-MS-7845:1

  New 'X' desktop is vislab-MS-7845:2

  Creating default startup script /home/vislab/.vnc/xstartup
  Starting applications specified in /home/vislab/.vnc/xstartup
  Log file is /home/vislab/.vnc/vislab-MS-7845:2.log

  $ vncpasswd
  $ vncserver -kill
  $ cat ~/.vnc/*.pid ## list vnc server
  $ ps aux | grep vnc
  $ netstat -plnt

  # vnc://<vislab_ip1>:5901    ## X server 1
  # vnc://<vislab_ip1>:5902    ## X server 2

  $ vncserver -localhost
  $ sudo netstat -plnt  | grep vnc
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
  tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      10125/Xtightvnc


  New 'X' desktop is vislab-MS-7845:1

  Starting applications specified in /home/vislab/.vnc/xstartup
  Log file is /home/vislab/.vnc/vislab-MS-7845:1.log

  client $ ssh -L 59000:localhost:5901 -C -N -l sammy your_server_ip   ## channel via ssh
  # ssh -L 59000:localhost:5901 -C -N -l vislab <vislab_ip1>
  # -L <local:port>: <remote: port>
  # remote server: 5901 is local only, and ssh into server:22 and then tunnel to 5901
```



####
figure what Parent Process, am I in a subprocess of what?

 $ echo $PPID; # the parent ID of current shell
   6558
 $ ps aux | grep $(echo $PPID)
   vislab      6558  0.0  0.0  20744  4824 ?        Ss   11:28   0:02 tmux
   vislab     30146  0.0  0.0  17864  2428 pts/5    S+   14:42   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox 6558
 $ echo $$ ## current id of the shell
 $ ps aux | grep $(echo $$)
   vislab     27553  0.0  0.0  22528  7216 pts/5    Ss   14:27   0:00 -zsh
   vislab     30340  0.0  0.0  17864  2296 pts/5    S+   14:44   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox 27553
