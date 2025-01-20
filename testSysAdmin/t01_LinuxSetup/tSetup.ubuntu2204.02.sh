#!/bin/bash

## from: https://dev.to/blueskyson/writing-a-bash-script-to-automatically-setup-ubuntu-2204-5d3e
Reset='\033[0m'
Green='\033[0;32m'
MyUser=rich

echo "${Green}Change working directory to /home/${MyUser}/Downloads.${Reset}"
cd /home/${MyUser}/Downloads

if ! [ -x "$(command -v google-chrome)" ]; then
    echo "${Green}Install Google Chrome.${Reset}"
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -i google-chrome-stable_current_amd64.deb
else
    echo "${Green}Google Chrome is already installed.${Reset}"
fi

if ! [ -x "$(command -v code)" ]; then
    echo "${Green}Install VS Code.${Reset}"
    wget "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" --output-document vscode.deb
    dpkg -i vscode.deb
else
    echo "${Green}VS Code is already installed.${Reset}"
fi

if ! [ -x "$(command -v sshd)" ]; then
    echo "${Green}Install openssh-server.${Reset}"
    apt install -y openssh-server
    systemctl enable ssh
    systemctl start ssh
    echo "${Green}Run ssh-keygen as your user after installation.${Reset}"
else
    echo "${Green}openssh-server is already installed.${Reset}"
fi

if ! [ -x "$(command -v docker)" ]; then
    echo "${Green}Install Docker.${Reset}"
    apt install -y ca-certificates curl gnupg lsb-release
    mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
    chmod a+r /etc/apt/keyrings/docker.gpg
    apt update
    apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    groupadd docker
    usermod -aG docker $MyUser
    systemctl enable docker
    systemctl start docker
    echo "${Green}You might logout or restart for docker group to take effect.${Reset}"
else
    echo "${Green}Docker is already installed.${Reset}"
fi

if ! [ -x "$(command -v autojump)" ]; then
    echo "${Green}Install autojump.${Reset}"
    apt install autojump
    echo "# Setup autojump" >> /home/$MyUser/.bashrc
    echo "[[ -s /usr/share/autojump/autojump.sh ]] && source /usr/share/autojump/autojump.sh" >> /home/$MyUser/.bashrc
else
    echo "${Green}Autojump is already installed.${Reset}"
fi
