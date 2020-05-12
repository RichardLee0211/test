#! /bin/bash
## this is for set up a clean install kali


# install
#==================================================
# TODO
sudo apt update
# sudo apt install -y vim
# sudo apt install -y tmux
sudo apt install -y i3
# sudo apt install -y git
sudo apt install -y g++
sudo apt install -y net-tools # ifconfig
sudo apt install -y valgrind
sudo apt install -y htop
sudo apt install -y cmatrix
sudo apt install -y ctags
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
xrandr -s 2560x1600 # or resolution available

# restart i3 after this two liens
cp i3/i3.MacOSVM_Kali.config ~/.config/i3/config
cp i3/i3status.MacOSVM_Kali.config ~/.config/i3status/config

mkdir -p ~/.urxvt/ext
cp urxvt/ext/* ~/.urxvt/ext
xrdb ~/.Xresources

cp tmux.conf ~/.tmux.conf
cp vim/vimrc.basic.conf ~/.vimrc

## fonts
# or go to: https://www.nerdfonts.com/font-downloads
cd ~/Downloads/ && wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/Inconsolata.zip
mkdir Inconsolata && cd Inconsolata && unzip ../Inconsolata.zip
mkdir -p ~/.fonts/
cp Inconsolata\ Nerd\ Font\ Complete.otf ~/.fonts/
cp Inconsolata\ Nerd\ Font\ Complete\ Mono.otf  ~/.fonts/
fc-cache -vf ~/.fonts/
# fc-list -v | grep <fonts name> # confirm

## using ohmyzsh to config zsh
# sudo usermod `whoami` -s /usr/bin/zsh # need to edit passwd file
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

## wallpaper
mkdir -p ~/Pictures/WallPaper/ && cd ~/Pictures/WallPaper/
wget https://i.redd.it/cb12p2q4rocx.png
# restart i3
