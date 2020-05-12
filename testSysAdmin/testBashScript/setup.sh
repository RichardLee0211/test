#!/bin/sh

sudo apt-get update
sudo apt-get install -y xubuntu-desktop 

#set up for automatic unattended upgrades; important for security
sudo apt-get install -y unattended-upgrades

#popular revision control system
sudo apt-get install -y git 

#install packages which may be necessary in building native js modules
sudo apt-get install -y software-properties-common build-essential libssl-dev

#install nodejs
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

#install npm
sudo apt-get install -y npm
sudo npm install -g npm

#install nodejs testing package
sudo apt-get install -y mocha

#json query / pretty-printer
sudo apt-get install -y jq

#editors
sudo apt-get install -y xauth emacs vim

#remote desktop vnc
sudo apt-get install -y tightvncserver xtightvncviewer

#
sudo apt-get install -y xfce4 gnome-system-tools


#install autocutsel for VNC copy text between client and server
sudo apt-get install -y autocutsel

#google-chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub \
  | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' \
  | sudo tee /etc/apt/sources.list.d/google-chrome.list 
sudo apt-get install -y google-chrome-stable

#x2go remote desktop
sudo apt-add-repository ppa:x2go/stable
sudo apt-get update
sudo apt-get install -y x2goserver x2goclient x2goserver-xsession

#ruby
sudo apt-get install -y ruby

#python
sudo apt-get install -y python3
sudo apt-get install -y python3-pip

#compilers specific stuff
#java
sudo apt-get install -y default-jdk

#install antlr jar
sudo mkdir /usr/local/share/java
( cd /usr/local/share/java; \
  sudo wget -q https://www.antlr.org/download/antlr-4.7.2-complete.jar )

#antlr python target
sudo -H pip3 install antlr4-python3-runtime
