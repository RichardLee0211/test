use ffmpeg for quick video and audio process
- vlc convert is not so good, it misses audio sometimes
- using soundflower system extension for macOS to direct an process's audio to quicktime record
- reboot after install a system extension

from: https://ostechnix.com/20-ffmpeg-commands-beginners/
```shell
    # 01 detailed info
    ffmpeg -i video.mp4

    # 02 convert format, compress .mov file
    ffmpeg -i video.mov video.mp3

    # 03 convert format but don't loss quaility
    ffmpeg -i video.mov -qscale 0 video.mp3

    # 04 Converting video files to audio files
    ffmpeg -i input.mp4 -vn output.mp3

    # more control
    ffmpeg -i input.mp4 -vn -ar 44100 -ac 2 -ab 320 -f mp3 output.mp3
    # -vn - Indicates that we have disabled video recording in the output file.
    # -ar - Set the audio frequency of the output file. The common values used are  22050, 44100, 48000 Hz.
    # -ac - Set the number of audio channels.
    # -ab - Indicates the audio bitrate.
    # -f - Output file format. In our case, it's mp3 format.

    # 05 Change the volume of audio files
    ffmpeg -i input.mp3 -af 'volume=0.5' output.mp3

    #  -filter: video scale=XXX:XXX -codec: audio copy
    ffmpeg -i input.mp4 -filter:v scale=1280:720 -c:a copy output.mp4
    ffmpeg -i input.mp4 -vf scale=1920:1080 smaller.mp4  # my 13MBP cannot play 4k video well, :(

    # 06 Compressing video files
    ffmpeg -i input.mp4 -vf scale=1280:-1 -c:v libx264 -preset veryslow -crf 24 output.mp4
    # audio -ac 2 -c:a aac -strict -2 -b:a 128k

    # 07 Compressing Audio files
    ffmpeg -i input.mp3 -ab 128 output.mp3
    # 96kbps
    # 112kbps
    # 128kbps
    # 160kbps
    # 192kbps
    # 256kbps
    # 320kbps

    # 08 Removing audio stream from a video file
    ffmpeg -i input.mp4 -an output.mp4

    # 09 Removing video stream from a media file
    ffmpeg -i input.mp4 -vn output.mp3
    ffmpeg -i input.mp4 -vn -ab 320 output.mp3

    # 10 Extracting images from the video
    ffmpeg -i input.mp4 -r 1 -f image2 image-%2d.png

    -r - Set the frame rate. I.e the number of frames to be extracted into images per second. The default value is 25.
    -f - Indicates the output format i.e image format in our case.
    image-%2d.png - Indicates how we want to name the extracted images.

    # 11 Cropping videos
    ffmpeg -i input.mp4 -filter:v "crop=w:h:x:y" output.mp4

    # 12 Convert a specific portion of a video
    ffmpeg -i input.mp4 -t 10 output.avi

    # 13 Set the aspect ratio to video
    ffmpeg -i input.mp4 -aspect 16:9 output.mp4

    # 14 Adding poster image to audio files
    ffmpeg -loop 1 -i inputimage.jpg -i inputaudio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest output.mp4

    # 15 Trim a media file using start and stop times
    ffmpeg -i input.mp4 -ss 00:00:50 -codec copy -t 50 output.mp4
    ffmpeg -i audio.mp3 -ss 00:01:54 -to 00:06:53 -c copy output.mp3

    # 16 Split audio/video files into multiple parts
    ffmpeg -i input.mp4 -t 00:00:30 -c copy part1.mp4 -ss 00:00:30 -codec copy part2.mp4

    # 17 Joining or merging multiple audio/video parts into one
    ffmpeg -f concat -safe 0 -i join.txt -c copy output.mp4
    ffmpeg -i "concat:audio1.mp3|audio2.mp3|audio3.mp3" -c copy output.mp3
    cat join.txt
    file /home/sk/myvideos/part1.mp4
    file /home/sk/myvideos/part2.mp4
    file /home/sk/myvideos/part3.mp4
    file /home/sk/myvideos/part4.mp4

    # 18 Add subtitles to a video file
    fmpeg -i input.mp4 -i subtitle.srt -map 0 -map 1 -c copy -c:v libx264 -crf 23 -preset veryfast output.mp4

    # 19 Preview or test video or audio files
    ffplay video.mp4
    ffplay audio.mp3

    # 20 Increase video playback speed
    ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" output.mp4
```

find
================================================================================
find ./ -type d -iregex ".*verbal.*" \
           -and -iregex ".*advan.*"
find -iname <filename>
find -iname *wordIremember*
