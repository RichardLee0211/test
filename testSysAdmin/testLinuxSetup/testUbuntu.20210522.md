log to prepare my ubuntu desktop

apt install -y vim git tmux tldr pandoc ranger

update install system using "software", then when reboot, the grub menu is missing
great, install ubuntu again

##### zsh
sudo apt-get install zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

##### use terminator
as it support "copy on select"
would be faster when with terminal and broswer work flow

##### build vim with X11 copy and paste support
from vim.git/src/INTSALL
```shell
To build Vim on Ubuntu from scratch on a clean system using git:
	Install tools required to be able to get and build Vim:
	% sudo apt install git
	% sudo apt install make
	% sudo apt install clang

	Build Vim with default features:
	% git clone https://github.com/vim/vim.git
	% cd vim/src
	% make

	Run tests to check there are no problems:
	% make test

	Install Vim in /usr/local:
	% sudo make install

	Add X windows clipboard support (also needed for GUI):
	% sudo apt install libxt-dev
	% make reconfig

	Add GUI support:
	% sudo apt install libgtk-3-dev
	% make reconfig

	Add Python 3 support:
	% sudo apt install libpython3-dev
	Uncomment this line in Makefile:
		"CONF_OPT_PYTHON3 = --enable-python3interp"
	% make reconfig
```

apt vim is in /user/bin while this build should be in /user/local/bin/vim
only ubuntu using Ctrl+Shift+c or +v to copy and paste

##### install notejs
sudo snap install node --classic
alias open=open-cli # in ~/.zshrc

sudo npm install --global open-cli
sudo npm install --global public-ip-cli    # public-ip
sudo npm install --global internal-ip-cli  # internal-ip

##### pip3
sudo apt install -y python3-pip
pip3 install speedtest-cli
export PATH="/home/wenchen/.local/bin/:$PATH" # ~/.zshrc

##### youtube-dl
sudo wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+x /usr/local/bin/youtube-dl
sudo apt install python-dev
rehash

##### how2
how2 seems to be nice, terminal app to search stack overflow
https://github.com/santinic/how2

##### dolphin
using dolphin as it provides better img preview
sudo apt install dolphin
feels like this apt build is limited

- setting default filemanager to dolphin
failed after some twinking
maybe reboot??
https://help.ubuntu.com/community/DefaultFileManager

##### nvidia driver
sudo apt install nvidia-driver-455

sudo apt-get install -y stress htop iotop lm-sensors
# Run a stress test with `nproc` CPU workers (sqrt)
#                        `nproc` Virtual Memory workers (malloc / free)
#                        `nproc` workers calling (sync)
#                        `nproc` workers writing to disk (write / unlink)
# For a total of 60 seconds.
stress --cpu `nproc` --vm `nproc` --vm-bytes 1GB --io `nproc` --hdd `nproc` --hdd-bytes 1GB --timeout 60s

git clone https://github.com/wilicc/gpu-burn
cd gpu-burn
make
./gpu_burn 60 # will run gpu_burn for 60 seconds

htop
sudo iotop
watch sudo sensors
watch nvidia-smi
