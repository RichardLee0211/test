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
