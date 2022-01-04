BorgBackup
--------------------------------------------------------------------------------
### so this is fast
time borg -vp create --files-cache=ctime,size --list --filter=AME --stats ./::netStore5_B_20220103 /media/wenchen/netStore00/netStore01

time borg -vp create --files-cache=ctime,size --list --filter=AME --stats ./::netStore5_B_{now:%Y%m%d} /media/wenchen/netStore00/netStore01


from: https://borgbackup.readthedocs.io/en/stable/quickstart.html

```shell
  borg init --encryption=repokey /path/to/repo
  borg -v -p create /path/to/repo::Monday ~/src ~/Documents
  borg create -v -p --stats /path/to/repo::Tuesday ~/src ~/Documents

  # initialize a repository:
  borg init /tmp/borg

  # create a "first" archive inside this repo (verbose):
  borg create --progress --stats /tmp/borg::first ~/Desktop

  # create a "second" archive (less verbose):
  borg create /tmp/borg::second ~/Desktop

  # even more verbose:
  borg create -v --stats /tmp/borg::third ~/Desktop

  # list repo / archive contents:
  borg list /tmp/borg
  borg list /tmp/borg::first

  # extract ("restore") from an archive to cwd:
  mkdir test ; cd test
  borg extract /tmp/borg::third

  # simulate extraction (good test):
  borg extract -v --dry-run /tmp/borg::third

  # check consistency of repo:
  borg check /tmp/borg

  # info about archive:
  borg info /tmp/borg::first

  # delete archive:
  borg delete /tmp/borg::first

  # delete repo:
  borg delete /tmp/borg

  # connect to remote borg via ssh:
  # remote borg needs to be compatible with local
  borg init ssh://user@host:22/mnt/backup/borg
  borg create ssh://user@host:22/mnt/backup/borg::first ~
  # also possible: using sshfs or other locally mounted
  # network filesystems,  but be careful: locks, perf.

```


#### expected backup performance:
E.g., for this setup:

- server grade machine (4C/8T 2013 Xeon, 64GB RAM, 2x good 7200RPM disks)
- local zfs filesystem (mirrored) containing the backup source data
- repository is remote (does not matter much for unchanged files)
- backup job runs while machine is otherwise idle
The observed performance is that Borg can process about 1 million unchanged files (and a few small changed ones) in 4 minutes!

#### experiments
```shell

## 20GB test on borg on backup performance
## this is a SATAII SSD to harddrive (~130MB/s)
	(base) ╭─vislab at vislab-inwin in /media/vislab/Big3TB/20220103_testbackup 22-01-03 - 10:38:49
	╰─○ borg -vp create --stat ./::test_20220103_01 ~/Downloads/_youtube/20220103_backuptest
	Creating archive at "./::test_20220103_01"
	6.87 GB O 6.88 GB C 6.88 GB D 32 N home/vislab/Downloads/_youtube/XXXXX
	Archive name: test_20220103_01
	Archive fingerprint: 03fc80a1b4ccccfe73bf08d731878cf8c496c80fd7d582e3e00c557d269fde40
	Time (start): Mon, 2022-01-03 10:39:07
	Time (end):   Mon, 2022-01-03 10:43:29
	Duration: 4 minutes 22.72 seconds
	Number of files: 210
	Utilization of max. archive size: 0%
	------------------------------------------------------------------------------
	                       Original size      Compressed size    Deduplicated size
	This archive:               22.22 GB             22.25 GB             19.33 GB
	All archives:               22.22 GB             22.25 GB             19.33 GB

	                       Unique chunks         Total chunks
	Chunk index:                    7724                 8865
	------------------------------------------------------------------------------


## this is fast when change a file
	(base) ╭─vislab at vislab-inwin in /media/vislab/Big3TB/20220103_testbackup 22-01-03 - 10:56:04
	╰─○ borg create --list --filter=AME --stats ./::test20220103_02 ~/Downloads/_youtube/20220103_backuptest
	A /home/vislab/Downloads/_youtube/20220103_backuptest/_youtube/XXXXXXXXXXXXXXXXX
	------------------------------------------------------------------------------
	Archive name: test20220103_02
	Archive fingerprint: 8bd5c4a3edd319b4f998ea5bab213b7768466ae0c431fffbff61baf9ca8733ce
	Time (start): Mon, 2022-01-03 10:56:59
	Time (end):   Mon, 2022-01-03 10:57:05
	Duration: 6.50 seconds
	Number of files: 210
	Utilization of max. archive size: 0%
	------------------------------------------------------------------------------
	                       Original size      Compressed size    Deduplicated size
	This archive:               22.22 GB             22.25 GB            110.79 kB
	All archives:               44.44 GB             44.50 GB             19.33 GB

	                       Unique chunks         Total chunks
	Chunk index:                    7726                17730
	------------------------------------------------------------------------------

## when change a directory name, Added to the list
## mv ads ads_01
	(base) ╭─vislab at vislab-inwin in /media/vislab/Big3TB/20220103_testbackup 22-01-03 - 10:57:06
	╰─○ borg create --list --filter=AME --stats ./::test20220103_03 ~/Downloads/_youtube/20220103_backuptest
	A /home/vislab/Downloads/_youtube/20220103_backuptest/_youtube/ads_01/XXXX
	A /home/vislab/Downloads/_youtube/20220103_backuptest/_youtube/XXXXXXXXXXXX/XXXX
	------------------------------------------------------------------------------
	Archive name: test20220103_03
	Archive fingerprint: 79eefad13a37de68fca4fa222f96502ad29ba94443cdf69c834f160b3f901e5d
	Time (start): Mon, 2022-01-03 10:59:38
	Time (end):   Mon, 2022-01-03 10:59:46
	Duration: 7.82 seconds
	Number of files: 210
	Utilization of max. archive size: 0%
	------------------------------------------------------------------------------
	                       Original size      Compressed size    Deduplicated size
	This archive:               22.22 GB             22.25 GB            314.59 kB
	All archives:               66.65 GB             66.76 GB             19.33 GB

	                       Unique chunks         Total chunks
	Chunk index:                    7728                26595
	------------------------------------------------------------------------------



## turns out, backup to SSD is not good, the backup time is longer ?
	(base) ╭─vislab at vislab-inwin in ~/Downloads/_youtube/ssd_backup 22-01-03 - 10:47:16
	╰─○ borg create --list --stats ./::test20220103_01 ../20220103_backuptest
	A ../20220103_backuptest/_youtube/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXX.csv
	A ../20220103_backuptest/_youtube/XXXXXXXXX/XXXX
	d ../20220103_backuptest
	------------------------------------------------------------------------------
	Archive name: test20220103_01
	Archive fingerprint: 66d96d2e8547993a5c75e2f05b78766ab975cafa254c7206e4e18e811e9fb271
	Time (start): Mon, 2022-01-03 10:47:29
	Time (end):   Mon, 2022-01-03 10:52:41
	Duration: 5 minutes 12.36 seconds
	Number of files: 210
	Utilization of max. archive size: 0%
	------------------------------------------------------------------------------
	                       Original size      Compressed size    Deduplicated size
	This archive:               22.22 GB             22.25 GB             19.33 GB
	All archives:               22.22 GB             22.25 GB             19.33 GB

	                       Unique chunks         Total chunks
	Chunk index:                    7651                 8804
	------------------------------------------------------------------------------


```


```bash
	#!/bin/sh

	# Setting this, so the repo does not need to be given on the commandline:
	export BORG_REPO=ssh://username@example.com:2022/~/backup/main

	# See the section "Passphrase notes" for more infos.
	export BORG_PASSPHRASE='XYZl0ngandsecurepa_55_phrasea&&123'

	# some helpers and error handling:
	info() { printf "\n%s %s\n\n" "$( date )" "$*" >&2; }
	trap 'echo $( date ) Backup interrupted >&2; exit 2' INT TERM

	info "Starting backup"

	# Backup the most important directories into an archive named after
	# the machine this script is currently running on:

	borg create                         \
	    --verbose                       \
	    --filter AME                    \
	    --list                          \
	    --stats                         \
	    --show-rc                       \
	    --compression lz4               \
	    --exclude-caches                \
	    --exclude '/home/*/.cache/*'    \
	    --exclude '/var/tmp/*'          \
	                                    \
	    ::'{hostname}-{now}'            \
	    /etc                            \
	    /home                           \
	    /root                           \
	    /var                            \

	backup_exit=$?

	info "Pruning repository"

	# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
	# archives of THIS machine. The '{hostname}-' prefix is very important to
	# limit prune's operation to this machine's archives and not apply to
	# other machines' archives also:

	borg prune                          \
	    --list                          \
	    --prefix '{hostname}-'          \
	    --show-rc                       \
	    --keep-daily    7               \
	    --keep-weekly   4               \
	    --keep-monthly  6               \

	prune_exit=$?

	# use highest exit code as global exit code
	global_exit=$(( backup_exit > prune_exit ? backup_exit : prune_exit ))

	if [ ${global_exit} -eq 0 ]; then
	    info "Backup and Prune finished successfully"
	elif [ ${global_exit} -eq 1 ]; then
	    info "Backup and/or Prune finished with warnings"
	else
	    info "Backup and/or Prune finished with errors"
	fi

	exit ${global_exit}
```

### back up slow with little changed file
(base) ┌[wenchen☮wenchen-MS-7845]-(/media/wenchen/netStore4B/netStore5_B)
└> borg create --list --filter=AME --stats ./::netStore5_B_20220103 /media/wenchen/netStore00/netStore01
M /media/wenchen/netStore00/netStore01/XXX
^CKeyboard interrupt

M status, found in file cache, but the metadata did not match

it might have something to do with cache that store files' metadata
export BORG_FILES_CACHE_TTL=500

default cache location is ~/.cache/borg
du -hd2 ~/.cache/borg
300M, weird, this should be enough to store all meta of my 2.2TB data

time borg -vp create --list --filter=AME --stats ./::netStore5_B_20220103 /media/wenchen/netStore00/netStore01



### unstable inode number
--filter=AME, A for add, M for modified, E for error
--files-cache=ctime,size  ## default ctime,size,inode and inode would be bad for external drives
--files-cache=mtime,size  ## ctime is the change time(metadata and file content)
--comment COMMENT
--checkpoint-interval SECONDS

--progress
Original, compredded and Dedeplicated, the number of files
(O, C, D, N)


the reduced to 15 min, bottle neck could be the SMR external drive I am using
```shell
	------------------------------------------------------------------------------
	Archive name: netStore5_B_20220103
	Archive fingerprint: 123f96c5da3c96327205bf42db70cfb4ba7ec2654bd4ed41e1197414f5b5d770
	Time (start): Tue, 2022-01-04 13:06:17
	Time (end):   Tue, 2022-01-04 13:19:41
	Duration: 13 minutes 23.07 seconds
	Number of files: 117540
	Utilization of max. archive size: 0%
	------------------------------------------------------------------------------
	                       Original size      Compressed size    Deduplicated size
	This archive:                2.31 TB              2.28 TB             48.12 MB
	All archives:                7.21 TB              7.11 TB              2.25 TB

	                       Unique chunks         Total chunks
	Chunk index:                  972578              3107441
	------------------------------------------------------------------------------
	borg -vp create --files-cache=ctime,size --list --filter=AME --stats    43.29s user 11.79s system 6% cpu 13:26.69 total
```



read more about borg
--------------------------------------------------------------------------------

#### recommended way for two back up
borg init repo1
borg init repo2
client machine —borg create—> repo1
client machine —borg create—> repo2

#### borg info

borg info ./
Repository ID: da92cef93c13fd4c1006a821f17c81dc02bc90408c22b1b3a6407a3e09bf04cf
Location: /media/wenchen/netStore4B/netStore5_B
Encrypted: Yes (repokey)
Cache: /home/wenchen/.cache/borg/da92cef93c13fd4c1006a821f17c81dc02bc90408c22b1b3a6407a3e09bf04cf
Security dir: /home/wenchen/.config/borg/security/da92cef93c13fd4c1006a821f17c81dc02bc90408c22b1b3a6407a3e09bf04cf
------------------------------------------------------------------------------
                       Original size      Compressed size    Deduplicated size
All archives:                4.90 TB              4.83 TB              2.25 TB

                       Unique chunks         Total chunks
Chunk index:                  972086              2107244

#### SMR harddrives

Some Linux kernel versions between 3.19 and 4.5 had various bugs handling
device-managed SMR drives, leading to IO errors, unresponsive drives and
unreliable operation in general.Some Linux kernel versions between 3.19 and 4.5
had various bugs handling device-managed SMR drives, leading to IO errors,
unresponsive drives and unreliable operation in general.

#### borg advise against using database like software on FAT file system

#### later

memtest86+ to test RAM ?
smartmontools for harddrive, smartctl -a /dev/sdSomething


format disk to exfat for backup use
--------------------------------------------------------------------------------

well, disk format should really use a GUI, as I do not format disk every week
I properly do it every two year
- low-level format: done by manufactures
- Partitioning: disk into sections
    partition editor: fdisk, GNU Parted or Disk Uitlity
- High-level formatting: file system, cluster size, partition label

use GUID for bigger than 2TB harddrive
use exfat to make it readable and writable for all mac, win and Linux
NTFS for windows
Ext4 for Linux

```shell
    ## didn't learn it completely
    sudo apt install exfat-fuse exfat-utils
    sudo fdisk -l
    sudo wipefs -a /dev/sdb
    sudo fdisk /dev/sdb
    sudo mkfs.exfat -n myStore4B /dev/sdb
```
