#! /bin/bash

## goal: put together script for my usage
## - video code
## - python3,
## - security tools
## is there a different with root/normal user on live boot linux system ??


## config
output_file="output.log"
username="rich"
# username="wenchen"
timezone=""

# Set the machine's timezone
# Arguments:
#   tz data timezone
function setTimezone() {
    local timezone=${1}
    echo "${1}" | sudo tee /etc/timezone
    sudo ln -fs "/usr/share/zoneinfo/${timezone}" /etc/localtime # https://bugs.launchpad.net/ubuntu/+source/tzdata/+bug/1554806
    sudo dpkg-reconfigure -f noninteractive tzdata
}
## wrapper
function setupTimezone() {
    # echo -ne "Enter the timezone for the server (Default is 'Asia/Singapore'):\n" >&3
    # read -r timezone
    if [ -z "${timezone}" ]; then
        # timezone="Asia/Singapore"
        timezone="America/New_York"
    fi
    setTimezone "${timezone}"
    echo "Timezone is set to $(cat /etc/timezone)" >&3
}

# Configure Network Time Protocol
function configureNTP() {
    ubuntu_version="$(lsb_release -sr)"

    # if [[ $(bc -l <<< "${ubuntu_version} >= 20.04" ) -eq 1 ]]; then
    if [[ `bc -l <<< "${ubuntu_version} >= 20.04"` -eq 1 ]]; then
        sudo systemctl restart systemd-timesyncd
    else
        sudo apt-get update
        sudo apt-get --assume-yes install ntp
        # force NTP to sync
        sudo service ntp stop
        sudo ntpd -gq
        sudo service ntp start
    fi
}

function revertSudoers() {
    sudo cp /etc/sudoers.bak /etc/sudoers
    sudo rm -rf /etc/sudoers.bak
}

function cleanup() {
    if [[ -f "/etc/sudoers.bak" ]]; then
        revertSudoers
    fi
}

function getCurrentDir() {
    local current_dir="${BASH_SOURCE%/*}"
    if [[ ! -d "${current_dir}" ]]; then current_dir="$PWD"; fi
    echo "${current_dir}"
}

## wen: this one is nice
function includeDependencies() {
    # shellcheck source=./setupLibrary.sh
    # source "${current_dir}/setupLibrary.sh"
    source "${current_dir}/tSetup.ubuntu2204.0402.sh"
}


## Add/Update/Delete user account
# Arguments:
#   Account Username
#   Flag to determine if user account is added silently. (With / Without GECOS prompt)
function addUserAccount() {
    local username=${1}
    local silent_mode=${2}

    if [[ ${silent_mode} == "true" ]]; then
        sudo adduser --disabled-password --gecos '' "${username}"
    else
        sudo adduser --disabled-password "${username}"
    fi

    sudo usermod -aG sudo "${username}"
    sudo passwd -d "${username}"
}
# Arguments:
#   Account Username
function updateUserAccount() {
    local username=${1}
    sudo passwd -d "${username}"
    sudo usermod -aG sudo "${username}"
}
## wen: maybe need to confirm operation
function delUserAccount() {
    local username=${1}
    sudo deluser --remove-home "${username}"
}

# Update the user account
# Arguments:
#   Account Username
function updateUserAccount() {
    local username=${1}
    sudo passwd -d "${username}"
    sudo usermod -aG sudo "${username}"
}

function logTimestamp() {
    local filename=${1}
    {
        echo "==================="
        echo "Log generated on $(date)"
        echo "==================="
    } >>"${filename}" 2>&1
}

## wen: interesting
# Disables the sudo password prompt for a user account by editing /etc/sudoers
# Arguments:
#   Account username
function disableSudoPassword() {
    local username="${1}"
    sudo cp /etc/sudoers /etc/sudoers.bak
    sudo bash -c "echo '${1} ALL=(ALL) NOPASSWD: ALL' | (EDITOR='tee -a' visudo)"
}

# Add the local machine public SSH Key for the new user account
# Arguments:
#   Account Username
#   Public SSH Key
function addSSHKey() {
    local username=${1}
    local sshKey=${2}

    execAsUser "${username}" "mkdir -p ~/.ssh; chmod 700 ~/.ssh; touch ~/.ssh/authorized_keys"
    execAsUser "${username}" "echo \"${sshKey}\" | sudo tee -a ~/.ssh/authorized_keys"
    execAsUser "${username}" "chmod 600 ~/.ssh/authorized_keys"
}

## wen: need to double check it
# Modify the sshd_config file
# shellcheck disable=2116
function changeSSHConfig() {
    sudo sed -re 's/^(\#?)(PasswordAuthentication)([[:space:]]+)yes/\2\3no/' -i."$(echo 'old')" /etc/ssh/sshd_config
    sudo sed -re 's/^(\#?)(PermitRootLogin)([[:space:]]+)(.*)/PermitRootLogin no/' -i /etc/ssh/sshd_config
}

## wen: cool
# Setup the Uncomplicated Firewall
function setupUfw() {
    sudo apt-get install ufw
    sudo ufw allow OpenSSH
    yes y | sudo ufw enable
}

## from: https://linuxiac.com/how-to-install-docker-on-linux-mint-21/
function installDocker02() {
  sudo apt update
  sudo apt install -y apt-transport-https ca-certificates curl gnupg
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt update
  sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  # sudo systemctl is-active docker
}

## from: https://docs.docker.com/engine/install/ubuntu/
function installDocker() {
  for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
    sudo apt-get remove $pkg;
  done

  # Add Docker's official GPG key:
  sudo apt-get update
  sudo apt-get install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc

  # Add the repository to Apt sources:
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update

  sudo apt install -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin

}

## wen: some of my stuff
function installPackages() {
  sudo apt install -y terminator
  sudo apt install -y vim-gtk3     # for +clipboard and +python3
  sudo apt install -y tmux
  sudo apt install -y git
  sudo apt install -y cmatrix
  sudo apt install -y tldr
  sudo apt install -y pandoc
  sudo apt install -y net-tools # ifconfig
  sudo apt install -y htop, btop
  sudo apt install -y dolphin
  sudo apt install -y jq
  sudo apt install -y scrot # and bind it to PrtSc
  sudo apt install -y gnome-screenshot
  sudo apt install -y openssh-server
  sudo apt install -y multitail
  sudo systemctl enable ssh
  sudo systemctl status ssh

  ## ranger is not showing text file preview ??
  # set preview_script $HOME/.config/ranger/scope.sh
  # set ranger_load_default_rc false
  ## from: https://github.com/HrushikeshK/dotfiles/blob/master/.config/ranger/rc.conf
  ## from: https://github.com/ranger/ranger/issues/1072
  sudo apt install -y ranger
  cat > $HOME/.config/ranger/rc.config <<EOL
set use_preview_script false
set draw_borders true
set preview_images true
set preview_images_method urxvt
set draw_borders true
EOL


  ## change caplock to ctrl on keyboard
  cat > $HOME/.Xmodmap <<EOL
! Simplest example of changeing CapsLock into Control
! from: https://wiki.archlinux.org/title/xmodmap
! need to clear modifier key involved
clear lock
clear control
! assign new keysym to keycode
keycode 66 = Control_L
! add back the modifier key
add control = Control_L Control_R
EOL

  sudo apt install -y zsh
  sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
  cat >> $HOME/.zshrc <<EOL
## wenchen
## inside ~/.bash_profile
xmodmap ~/.Xmodmap
## ~/.bash_profile is for login shells(GUI login or ssh)
## while ~/.bashrc is for interactive non-login shells
bindkey -v
bindkey "^A" vi-beginning-of-line
bindkey "^E" vi-end-of-line

## from: https://unix.stackexchange.com/questions/97843/how-can-i-search-history-with-text-already-entered-at-the-prompt-in-zsh/280845
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey "^[[A" up-line-or-beginning-search # Up
bindkey "^[[B" down-line-or-beginning-search # Down

## take one directory path to add to $PATH
pathadd() {
    if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
        PATH="${PATH:+"$PATH:"}$1"
    fi
}
EOL
  source ~/.zshrc; rehash;

  git config --global user.name rich
  git config --global user.email richardlee0211er@gmail.com

  mkdir -p $HOME/Code
  git clone https://github.com/richardlee0211/test $HOME/Code/_Mytest

  ## pulling from github might be better
  cp $HOME/Code/_Mytest/testSysAdmin/t01_LinuxSetup/vim/vimrc.basic.conf $HOME/.vimrc
  cp $HOME/Code/_Mytest/testSysAdmin/t01_LinuxSetup/c01_tmux.conf  $HOME/.tmux.conf

  ## TODO: doom emacs for notes
  ## from: https://github.com/satyg-66/ubuntu-doom-emacs

  ## snap doesn't work with live boot VM
  # sudo snap install vlc
  sudo apt install vlc

  ## install npm and node
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
  source ~/.zshrc; rehash;
  nvm install v16.14.0
  npm install -g tldr
  npm install -g open-cli
  npm install -g public-ip-cli    # public-ip
  npm install -g internal-ip-cli  # internal-ip
  npm install -g get-port-cli     # get-port, get a random available port

  ## pipx
  # pipx ensurepath
  sudo apt install pipx
  sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
  pipx install speedtest-cli

  ## install wireshark
  echo "wireshark-common wireshark-common/install-setuid boolean true" | sudo debconf-set-selections
  sudo DEBIAN_FRONTEND=noninteractive apt -y install wireshark

  sudo systemctl is-active docker

  ## next:
  ## install awesome fonts ??
  ## install chrome, and brave broswer, and Tor, and Plugins?? Possible ??
  ## install notion ?? or just broswer is good enough
  ## install window management shortcuts
  ## get ventoy for multi-boot with USB driver
}

## pre-main config
current_dir=$(getCurrentDir)
includeDependencies

function main() {
    # Run setup functions when these signals are received
    trap cleanup EXIT SIGHUP SIGINT SIGTERM
    # Exit immediately if a command exits with a non-zero status.
    set -e

    ## wen: more like create user "rich" if doesn't exist
    # if id $username >/dev/null 2>&1; then
    #     echo "user $username found"
    #     ## wen: single quote in bash is raw string, $username format doesn't work
    #     # delUserAccount $username
    # else
    #     echo "user $username not found, creating"
    #     addUserAccount "${username}"
    #     echo "$username created"
    # fi

    echo 'Running setup script...'
    logTimestamp "${output_file}"

    # read -rp "Paste in the public SSH key for the new user:\n" sshKey
    ## redict output of bash process
    exec 3>&1 >>"${output_file}" 2>&1

    ## wen: don't need them for now
    # disableSudoPassword "${username}"
    # addSSHKey "${username}" "${sshKey}"
    # changeSSHConfig
    # setupUfw

    installPackages

    echo "Configuring System Time... " >&3
    setupTimezone
    configureNTP

    sudo service ssh restart
    cleanup

    echo "Setup Done! Log file is located at ${output_file}" >&3
}


main
