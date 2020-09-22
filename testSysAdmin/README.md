reading "Essential System Administration"

interesting command:
write wli100
talk

File ownership:

ch02 Essential Administrative Tools and Techniques
--------------------------------------------------------------------------------

### Getting the Most from Common Commands

find is about mate-data of the file
grep is about contant of the file

before make install, preview it by make -n install

TODO: to be continue

others
--------------------------------------------------------------------------------
#### for backup
to encrypt whole partition would take different tools in different system
```
    zip -er name_date.zip folder_to_compress # -e for encryption
    mv name_date.zip USB_sticker # for storage
```

take date
date "+%Y%m%d"

#### test disk write/read speed
```bash
    #!/bin/bash
    echo "---------------------"
    echo "Write Test Running. Please Wait..."
    write=$(dd if=/dev/zero bs=2048k of=tstfile count=1024 2>&1 | grep sec | awk '{print $1 / 1024 / 1024 / $5, "MB/sec" }')
    purge
    echo ""
    echo "Read Test Running. Please Wait..."
    read=$(dd if=tstfile bs=2048k of=/dev/null count=1024 2>&1 | grep sec | awk '{print $1 / 1024 / 1024 / $5, "MB/sec" }')
    clear
    echo ""
    echo "Read Speed is: $read"
    echo "Write Speed is: $write"
    echo "---------------------"
    echo "Cleaning up. Please Wait..."
    purge
    rm tstfile
    echo ""
    exit 0
```
