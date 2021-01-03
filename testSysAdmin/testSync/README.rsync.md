I need to learn this problem since I have large photo and video to backup
rsync
here's what I think
- one hot working folder on my laptop, 2021XXXX_actName
- one hot back on my dailly harddrive
- once project is complete, one cold backup folder on my 5mystore harddrive (maybe I need more cold harddrive)
- and cold project fold could be offload from my daily harddrive and my laptop

I accidentally delete my 20150000 and 20160000 photo backup folder, shoot
rsync -delete
hope I have backup files at homeland

```shell
## I don't know why this command doesn't work on some folders
rsync -avu "/Volumes/SSD_1TB/iPhoto" "/Volumes/Wenchen_bak/wenchen_bak_20200427/Iphoto"

## tree output on files
```
