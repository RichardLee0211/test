BorgBackup
--------------------------------------------------------------------------------
from: https://borgbackup.readthedocs.io/en/stable/quickstart.html
borg init --encryption=repokey /path/to/repo
borg -v -p create /path/to/repo::Monday ~/src ~/Documents
borg create --stats /path/to/repo::Tuesday ~/src ~/Documents

### use this to backup my files !!
time borg -vp create --files-cache=ctime,size --list --filter=AME --stats ./::netStore5_B_20220103 /media/wenchen/netStore00/netStore01

time borg -vp create --files-cache=ctime,size --list --filter=AME --stats ./::netStore5_B_{now:%Y%m%d} /media/wenchen/netStore00/netStore01


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
