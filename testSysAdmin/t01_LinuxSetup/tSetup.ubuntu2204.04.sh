#!/bin/bash

## from: https://github.com/jasonheecs/ubuntu-server-setup/blob/master/setup.sh

set -e

function getCurrentDir() {
    local current_dir="${BASH_SOURCE%/*}"
    if [[ ! -d "${current_dir}" ]]; then current_dir="$PWD"; fi
    echo "${current_dir}"
}

## wen: this one is nice
function includeDependencies() {
    # shellcheck source=./setupLibrary.sh
    source "${current_dir}/setupLibrary.sh"
}

function logTimestamp() {
    local filename=${1}
    {
        echo "==================="
        echo "Log generated on $(date)"
        echo "==================="
    } >>"${filename}" 2>&1
}

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
        timezone="Asia/Singapore"
    fi
    setTimezone "${timezone}"
    echo "Timezone is set to $(cat /etc/timezone)" >&3
}

## wen: what this for ?
function setupSwap() {
    createSwap
    mountSwap
    tweakSwapSettings "10" "50"
    saveSwapSettings "10" "50"
}

function hasSwap() {
    [[ "$(sudo swapon -s)" == *"/swapfile"* ]]
}

function cleanup() {
    if [[ -f "/etc/sudoers.bak" ]]; then
        revertSudoers
    fi
}

## config
current_dir=$(getCurrentDir)
includeDependencies
output_file="output.log"

function main() {
    read -rp "Do you want to create a new non-root user? (Recommended) [Y/N] " createUser

    # Run setup functions
    trap cleanup EXIT SIGHUP SIGINT SIGTERM

    if [[ $createUser == [nN] ]]; then
        username=$(whoami)
        updateUserAccount "${username}"
    elif [[ $createUser == [yY] ]]; then
        read -rp "Enter the username of the new user account: " username
        addUserAccount "${username}"
    else
        echo 'This is not a valid choice!'
        exit 1
    fi

    read -rp $'Paste in the public SSH key for the new user:\n' sshKey
    echo 'Running setup script...'
    logTimestamp "${output_file}"

    exec 3>&1 >>"${output_file}" 2>&1


    disableSudoPassword "${username}"
    addSSHKey "${username}" "${sshKey}"
    changeSSHConfig
    setupUfw

    # if ! hasSwap; then
    #     setupSwap
    # fi

    setupTimezone
    echo "Configuring System Time... " >&3
    configureNTP

    sudo service ssh restart
    cleanup

    echo "Setup Done! Log file is located at ${output_file}" >&3
}


main
