#! /bin/bash

## goal: remove the 20s advertisement in the end of audio file
## this is uncanny since I may need do this in the future collection
## I hate this kind of advertisement

file="test08.mp3"
of="output_test08.mp3"

# files=(`ls`)
# echo $files[0]
for f in $(ls); do
    if [[ $f == *.mp3 ]]; then
        of=out+$f
        ffmpeg -ss 00 -i $f -c copy \
            -t $(( $(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $f |cut -d\. -f1) - 20 )) \
            $of
    fi
done

# from: https://superuser.com/questions/1279481/remove-x-seconds-of-a-video-from-the-end-without-knowing-the-total-duration-of-t/1279485
# from: https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video
# ffmpeg -ss 00 -i $file -c copy \
    # -t $(( $(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $file |cut -d\. -f1) - 20 )) \
    # $of

#---some effort----------------------------------------------------------------

# line=$(ffmpeg -i $file 2>&1 | grep Duration ) # something like "Duration: 00:06:14.65, start: 0.000000, bitrate: 128 kb/s"
# duration= echo $line | sed -E "s/(.*), .*, .*/\1/"
# min= echo $duration | sed -E "s/Duration: [0-9][0-9]:([0-9][0-9]):[0-9][0-9].[0-9][0-9]/\1/"
# sec= echo $duration | sed -E "s/Duration: [0-9][0-9]:[0-9][0-9]:([0-9][0-9]).[0-9][0-9]/\1/"
# echo $line

## need sed
## this is pretty ugly
## echo "Duration: 00:06:14.65, start: 0.000000, bitrate: 128 kb/s" | sed -E "s/(.*), .*, .*/\1/" | sed -E "s/Duration: [0-9][0-9]:([0-9][0-9]):[0-9][0-9].[0-9][0-9]/\1/"

# duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $file)
# $duration_want=$(($duration-18))
# echo $duration_want
