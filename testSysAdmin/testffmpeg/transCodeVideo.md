need to have faith in this portable harddrive, ai
  142 directories scanned
   1116 image files read
   exiftool -progress -ext mp4 -ext mkv -ext webm -ext mov -json -r ./ >   13.81s user 2.77s system 15% cpu 1:45.59 total

#### use rsync for this folder
don't trust github for this data

## maybe do this, but transcode in my laptop is slow
## ffmpeg -i input.webm -vf scale=1920:1080 input.mp4
I am glad that it is two times faster on desktop CPU, but it still take half hour to transcode a one hour video

I need computation power for transcoding video, save storage
rsync -a dir1/ dir2
(base) ➜  20220103_process git:(master) ✗ rsync -avP --delete ../20220103_process/ vislab@130.245.4.102:~/Downloads/20220103_process      # push
(base) ➜  20220103_process git:(master) ✗ rsync -avP --delete vislab@130.245.4.102:~/Downloads/20220103_process/ ../20220103_process      # pull


I guess if a storage is not connected to computers, it is not active storage
filter rules:
- large file inspection
- storage vs. duration
- storage vs. rating
- storage vs. tags
- a ML decision making ?? for delete files, 233333, or for transcode large files




DONE: vim python code some useless warming
Syntastic vim plugin from: https://github.com/vim-syntastic/syntastic
glad there are some rules about python style, but if the code works, manage style should be an software problem, not programmer's problem
from: https://www.flake8rules.com/
nice vim ycm tutorial: https://vimawesome.com/plugin/youcompleteme-thing-itself

## ffmpeg GPU transcode
time ffmpeg -i Spider.webm -vf scale=1920:1080 output01.mp4 # speed: 0.87
time ffmpeg -hwaccel auto -i Spider.webm -vf scale=1920:1080 output01.mp4 # no
time ffmpeg -hwaccel cuda -i Spider.webm -vf scale=1920:1080 output01.mp4 # no

from: https://developer.nvidia.com/nvidia-video-codec-sdk
from: https://www.cyberciti.biz/faq/how-to-install-ffmpeg-with-nvidia-gpu-acceleration-on-linux/
```shell
    sudo apt install -y nvidia-cuda-toolkit
    mkdir ~/nvidia/ && cd ~/nvidia/
    git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
    cd nv-codec-headers && sudo make install
    cd ~/nvidia/
    git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg/
    sudo apt install -y build-essential yasm cmake libtool libc6 libc6-dev unzip wget libnuma1 libnuma-dev
    cd ~/nvidia/ffmpeg/
	./configure --enable-nonfree --enable-cuda-nvcc --enable-libnpp \
		--extra-cflags=-I/usr/local/cuda/include \
		--extra-ldflags=-L/usr/local/cuda/lib64
    make -j $(nproc)     # a few minutes
    ls -l ~/nvidia/ffmpeg/ffmpeg
```

default ffmpeg install on Ubuntu
```shell
	╰─⠠⠵ ffmpeg
	ffmpeg version 4.2.4-1ubuntu0.1 Copyright (c) 2000-2020 the FFmpeg developers
	  built with gcc 9 (Ubuntu 9.3.0-10ubuntu2)
	  configuration: --prefix=/usr --extra-version=1ubuntu0.1 --toolchain=hardened
		--libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu
		--arch=amd64 --enable-gpl --disable-stripping --enable-avresample
		--disable-filter=resample --enable-avisynth --enable-gnutls --enable-ladspa
		--enable-libaom --enable-libass --enable-libbluray --enable-libbs2b
		--enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libflite
		--enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme
		--enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa
		--enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse
		--enable-librsvg --enable-librubberband --enable-libshine --enable-libsnappy
		--enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora
		--enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx
		--enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2
		--enable-libxvid --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx
		--enable-openal --enable-opencl --enable-opengl --enable-sdl2
		--enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-nvenc
		--enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared
	  libavutil      56. 31.100 / 56. 31.100
	  libavcodec     58. 54.100 / 58. 54.100
	  libavformat    58. 29.100 / 58. 29.100
	  libavdevice    58.  8.100 / 58.  8.100
	  libavfilter     7. 57.100 /  7. 57.100
	  libavresample   4.  0.  0 /  4.  0.  0
	  libswscale      5.  5.100 /  5.  5.100
	  libswresample   3.  5.100 /  3.  5.100
	  libpostproc    55.  5.100 / 55.  5.100
	Hyper fast Audio and Video encoder
	usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```

## config and compile ffmpeg to support better
```shell
./configure \
--pkg-config-flags="--static" \
--extra-cflags=-I/usr/local/cuda/include                                   \
--extra-ldflags=-L/usr/local/cuda/lib64                             \
--extra-libs="-lpthread -lm" \
--ld="g++" \
--enable-cuda-nvcc --enable-libnpp                \
--enable-gpl \
--enable-gnutls \
--enable-libass \
--enable-libfdk-aac \
--enable-libfreetype \
--enable-libmp3lame \
--enable-libopus \
--enable-libvorbis \
--enable-libvpx \
--enable-libx264 \
--enable-libx265 \
--enable-nonfree
```
## good video codec
~/nvidia/ffmpeg/ffmpeg -y -hwaccel cuda -i input.mkv -vf scale=1920:1080 -vcodec libx265 -crf 24 output.mp4
## higher crf more compression
## control the bit rate at 200MB / 10 min
## meaning 2.6 Mb/s


## use a shorter sample
ffmpeg -i Spider.webm -ss 00:00:00 -codec copy -t 120 shorter.webm ## this is fast

~/nvidia/ffmpeg/ffmpeg -y -hwaccel cuda -i Spider.webm -vf scale=1920:1080 output01.mp4
## faster, but only speed=2.04x, not that significant
## but relieved CPU temperature problem
## and this video quality is bad, use -qscale 0
~/nvidia/ffmpeg/ffmpeg -y -hwaccel cuda -i shorter.webm -vf scale=1920:1080 -qscale 0 output01.mp4
## reduced 1/5 fileSize, from 4K to 1080P, it is not only about pixel counts, right?

ffmpeg -y -i input.kmv -vf scale=1920:1080 -vcodec libx265 -crf 24 output.mp4
ffmpeg -y -i input.kmv -vf scale=1920:1080 -vcodec h264_nvenc -preset slow -pixel_format yuv444p output.mp4
ffmpeg -y -i input.kmv -vf scale=1920:1080 -vcodec hevc_nvenc -preset slow -pixel_format yuv420p -profile:v main output.mp4

target="path/to/file";
ffmpeg -y -i $target -vf scale=1920:1080 -vcodec hevc_nvenc -preset slow -pixel_format yuv420p -profile:v main $target.mp4

```bash
#!bash

targets=('/media/wenchen/file asdf 202020.mp4' '/media/wenchen/file2 asdf 23sdf.mp4' )
for target in "${targets[@]}"; do
    echo "$target"
    ffmpeg -y -i "$target" -vf scale=1920:1080 -vcodec hevc_nvenc -preset slow -pixel_format yuv420p -profile:v main "$target.mp4"
    # rm "$target"
    # mv "$target.mp4"  something
done

## or
for file in *.webm; do
    echo $file "==============started"
    ffmpeg -y -i "$file" -vf scale=1920:1080 -vcodec hevc_nvenc -preset slow -pixel_format yuv420p -profile:v main "$file.mp4"
    ls -alh "$file*"
done
```
TODO: we would need a FIFO queue with pause/stop function?

ffmpeg -h encoder=h264_nvenc
https://superuser.com/questions/1296374/best-settings-for-ffmpeg-with-nvenc
https://trac.ffmpeg.org/wiki/Encode/H.265
https://trac.ffmpeg.org/wiki/Encode/VP9
https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu
follow this


ffmpeg -i "input.mp4" -copy_unknown -map_metadata 0 -map 0 -codec copy \
    -codec:v libx264 -pix_fmt yuv420p -crf 23 \
    -codec:a libfdk_aac -vbr 4 \
    -preset fast "output.mp4"

## clean up Ubuntu Mate Desktop environment for video review, analysis and management

Ubuntu Mate file program: Caja vs. Dolphin
media player: Celluid, mpv
terminal: Mate terminal,
it can adjust shortcut copy paste in edit->keyboard shortcuts, using super+c super+v
firefox support select and mid wheel click for copy and paste



#### use mpv for video in Ubuntu mate system
from: https://mpv.io/manual/master/
```conf
    # Location of user-defined bindings: ~/.config/mpv/input.conf
    ## wenchen
    l seek  5
    j seek -5
    k cycle pause

    9 seek 120
    7 seek -120

    o frame-step
    u frame-back-step

    UP    add volume +2
    DOWN  add volume -2
    > multiply speed 1.1
    < multiply speed 1/1.1
    . set speed 1.0
```



#### use "Eye of Mate" for pictures in Ubuntu mate system


#### use caja for file explorer
match macOS shortcut
~/.config/caja/accels
(gtk_accel_path "<Actions>/DirViewActions/Properties" "<Primary>i")   ; Ctrl+i to show metadata
(gtk_accel_path "<Actions>/DirViewActions/Rename" "Return")

from: https://askubuntu.com/questions/88010/assigning-shortcuts-accelerators-to-nautilus-3
from: https://unix.stackexchange.com/questions/443784/where-does-caja-put-its-preferences
```shell
    apt install dconf-editor -y
    ## this is not working well

    ## not helping with change shortcuts
    $ dconf dump /org/mate/caja/ > cajaprefs.txt
    $ $EDITOR cajaprefs.txt
    $ dconf load /org/mate/caja/ < cajaprefs.txt
```

#### gsetting
gsettings set org.gnome.desktop.lockdown disable-lock-screen true
TODO: look into it
https://guide.ubuntu-mate.org/#personalization-window-controls
