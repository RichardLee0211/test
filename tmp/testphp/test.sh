#!/bin/sh

for ((i=0; i<10; i++)) ; do
    wget -q -O unsplash_wallpaper_$i.jpg https://unsplash.it/1920/1080/?random
done
