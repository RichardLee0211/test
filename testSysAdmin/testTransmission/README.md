use it in Linux and MacOS
```shell
brew install transmission
transmission-daemon --download-dir "YOUR-DOWNLOAD-PATH"
transmission-daemon --dump-setttings
transmission-daemon
transmission-remote -a "http://*.com/*.torrent"
transmission-remote -a "magnet:?xt=urn:btih:9f9165d9a281a9b8e782cd5176bbcc8256fd1871&dn=Ubuntu+16.04.1+LTS+Desktop+64-bit&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
transmission-remote -l
transmission-remote --exit
# or pkill -3 transmission-daemon
```


sudo add-apt-repository ppa:transmissionbt/ppa
sudo apt update
sudo apt install transmission-gtk transmission-cli transmission-common transmission-daemon
transmission-gtk --version
systemctl status transmission-daemon.service
sudo apt remove transmission*

vim ~/.config/transmission/settings.json
pkill -HUP transmission-da

from: https://github.com/transmission/transmission/wiki/Configuration-Files
from: https://help.ubuntu.com/community/TransmissionHowTo

man transmission-remote
```
    EXAMPLES
    List all torrents:
        $ transmission-remote -l

    remove torrent with ID
        $ transmission-remote -t2 -r

    List all active torrents:
        $ transmission-remote -tactive -l

    Set download and upload limits to 400 kB/sec and 60 kB/sec:
        $ transmission-remote -d400 -u60
        $ transmission-remote --downlimit=400 --uplimit=60

    Set alternate download and upload limits to 100 kB/sec and 20 kB/sec:
        $ transmission-remote -asd100 -asu20
        $ transmission-remote --alt-speed-downlimit=100 --alt-speed-uplimit=20

    Set the scheduler to use the alternate speed limits on weekdays between 10AM and 11PM
        $ transmission-remote --alt-speed-time-begin=1000
        $ transmission-remote --alt-speed-time-end=2300
        $ transmission-remote --alt-speed-days=1-5
        $ transmission-remote --alt-speed-scheduler

    List all torrents' IDs and states:
        $ transmission-remote -l

    List all torrents from a remote session that requires authentication:
        $ transmission-remote host:9091 --auth=username:password -l

    Start all torrents:
        $ transmission-remote -tall --start

    Add two torrents:
        $ transmission-remote -a one.torrent two.torrent

    Add all torrents in ~/Desktop:
        $ transmission-remote -a ~/Desktop/*torrent

    Get detailed information on the torrent whose ID is '1':
        $ transmission-remote -t1 -i

    Get a list of a torrent's files:
        $ transmission-remote -t1 -f

    Download only its second and fourth files:
        $ transmission-remote -t1 -Gall -g2,4

    Set all torrents' first two files' priorities to high:
        $ transmission-remote -tall -ph1,2

    Set all torrents' files' priorities to normal:
        $ transmission-remote -tall -pnall
```

learn more from: https://wiki.archlinux.org/index.php/Transmission
https://github.com/transmission/transmission/wiki
