### init

get myself a jetson nano 2GB

burn the image according to nvidia website

- don't have a case for it, it's okay for now
- install a fan on heatsink

Jetson Nano 2GB Developer Kit uses the memory-efficient
- LXDE desktop environment with
- Openbox window manager


- firefox/chromium install vimium, adblock and dark reader
    this could be a heavy program for 2GB jetson nano
- copy vimrc.basic.conf
- install tmux
- install zsh and oh-my-zsh
- wanna get a universal system search tool to lauch programs
- wanna a window manager to bind my key press

### container
from: https://developer.nvidia.com/embedded/learn/tutorials/jetson-container

sudo docker pull nvcr.io/nvidia/l4t-base:r32.4.3
sudo docker image ls
sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix nvcr.io/nvidia/l4t-base:r32.4.3

### VNC
from: https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup

1. Enable the VNC server to start each time you log in
If you have a Jetson Nano 2GB Developer Kit (running LXDE)
    mkdir -p ~/.config/autostart
    cp /usr/share/applications/vino-server.desktop ~/.config/autostart/.

For all other Jetson developer kits (running GNOME)
    cd /usr/lib/systemd/user/graphical-session.target.wants
    sudo ln -s ../vino-server.service ./.

2. config
    gsettings set org.gnome.Vino prompt-enabled false
    gsettings set org.gnome.Vino require-encryption false

3. Set a password to access the VNC server
    # Replace the password with your desired password
    gsettings set org.gnome.Vino authentication-methods "['vnc']"
    gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64)
