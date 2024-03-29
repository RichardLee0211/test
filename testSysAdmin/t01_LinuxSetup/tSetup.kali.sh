#! /bin/bash
## this is for set up a clean install kali

## post installation of system
#===============================================================================
cp /etc/apt/sources.list /etc/apt/sources.list.bak
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
sudo apt update
sudo apt upgrade # it may take a while

# app and library install
#==================================================
# TODO
# sudo apt install -y vim
# sudo apt install -y tmux
# sudo apt install -y i3 # to install i3-gap refer to ./i3/README.md
# sudo apt install -y git
sudo apt install -y g++
sudo apt install -y net-tools # ifconfig
sudo apt install -y valgrind
sudo apt install -y htop
sudo apt install -y cmatrix
sudo apt install -y ctags
sudo apt install -y neofetch
# ?? sudo apt install -y python3

# git setup
git config --global user.name Wenchen
git config --global user.email richardlee0211er@gmail.com

# config
#==================================================
echo "CONFIG"
# mkdir -p ~/Code/ && cd ~/Code/
# git clone https://www.github.com/richardlee0211/test
# cd test/testLinuxSetup/
# xrandr -s 2560x1600 # or resolution available

## using ohmyzsh to config zsh
# sudo usermod `whoami` -s /usr/bin/zsh # need to edit passwd file
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

cp tmux.conf ~/.tmux.conf
cp vim/vimrc.basic.conf ~/.vimrc

## restart i3 after this two liens
# cp i3/i3.MacOSVM_Kali.config ~/.config/i3/config
# cp i3/i3status.MacOSVM_Kali.config ~/.config/i3status/config

# mkdir -p ~/.urxvt/ext
# cp urxvt/ext/* ~/.urxvt/ext
# xrdb ~/.Xresources

## fonts
# or go to: https://www.nerdfonts.com/font-downloads
# cd ~/Downloads/ && wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/Inconsolata.zip
# mkdir Inconsolata && cd Inconsolata && unzip ../Inconsolata.zip
# mkdir -p ~/.fonts/
# cp Inconsolata\ Nerd\ Font\ Complete.otf ~/.fonts/
# cp Inconsolata\ Nerd\ Font\ Complete\ Mono.otf  ~/.fonts/
# fc-cache -vf ~/.fonts/
# fc-list -v | grep <fonts name> # confirm


## wallpaper
# mkdir -p ~/Pictures/WallPaper/ && cd ~/Pictures/WallPaper/
# wget https://i.redd.it/cb12p2q4rocx.png
# restart i3
