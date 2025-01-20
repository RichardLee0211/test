#! /bin/bash

## Setup script for clean installed kali


## install
#===============================================================================
# TODO
# sudo apt install -y i3
sudo apt update
sudo apt install -y zsh
sudo apt install -y vim-gtk3
sudo apt install -y tmux
sudo apt install -y git
sudo apt install -y g++
sudo apt install -y net-tools # ifconfig
sudo apt install -y valgrind
sudo apt install -y htop
sudo apt install -y cmatrix
sudo apt install -y ctags
sudo apt install -y python3
sudo apt install -y ranger
sudo apt install -y tldr
sudo apt install -y pandoc
sudo apt install -y dolphin
sudo snap install node

# config
#===============================================================================
echo "CONFIG"

## git setup
git config --global user.name Wenchen
git config --global user.email richardlee0211er@gmail.com


## ohmyzsh
# sudo usermod `whoami` -s /usr/bin/zsh # need to edit passwd file
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

wget https://raw.githubusercontent.com/RichardLee0211/test/master/testSysAdmin/testLinuxSetup/vim/vimrc.basic.conf -O ~/.vimrc
wget https://raw.githubusercontent.com/RichardLee0211/test/master/testSysAdmin/testLinuxSetup/tmux.conf -O ~/.tmux.conf

## before you pull the test repository
# mkdir -p ~/Code/ && cd ~/Code/
# git clone https://www.github.com/richardlee0211/test
# cd test/testLinuxSetup/

## resolution
# xrandr -s 2560x1600 # or resolution available

## fonts
## or go to: https://www.nerdfonts.com/font-downloads
# cd ~/Downloads/ &&
# wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/Inconsolata.zip
# wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/Terminus.zip
# mkdir -p Inconsolata && cd Inconsolata && unzip ../Inconsolata.zip && cd ../
# mkdir -p Terminus && cd Terminus && unzip ../Terminus.zip && cd ../
# mkdir -p ~/.fonts/
# cp ~/Downloads/Inconsolata/Inconsolata\ Nerd\ Font\ Complete.otf ~/.fonts/
# cp ~/Downloads/Inconsolata/Inconsolata\ Nerd\ Font\ Complete\ Mono.otf  ~/.fonts/
# cp ~/Downloads/Terminus/'Terminess (TTF) Bold Italic Nerd Font Complete Mono.ttf' ~/.fonts/
# fc-cache -vf ~/.fonts/
# fc-list -v | grep <fonts name> # confirm


## restart i3 after these two liens
# cp i3/i3.MacOSVM_Kali.config ~/.config/i3/config
# cp i3/i3status.MacOSVM_Kali.config ~/.config/i3status/config

# mkdir -p ~/.urxvt/ext
# cp urxvt/ext/* ~/.urxvt/ext
# xrdb ~/.Xresources

# cp tmux.conf ~/.tmux.conf
# cp vim/vimrc.basic.conf ~/.vimrc

## wallpaper
# mkdir -p ~/Pictures/WallPaper/ && cd ~/Pictures/WallPaper/
# wget https://i.redd.it/cb12p2q4rocx.png


# restart i3
# logout and login for loginShell take effect


## GUI config
#===============================================================================

# install vimium, and adblock in chromium or firefox
