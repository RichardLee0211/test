Mac setup for working
================================================================================

in the near future, I will need a Ubuntu setup note by me

Hardware basic check
--------------------------------------------------------------------------------

- the touch pad
- the keyboard
- the screen
- the exter-material
- the hardware config, RAM, SSD, CPU, GPU, release year
- the fan sound
- a screen protector and body protector
- the power charge
- maybe a heave task test


system preferences
--------------------------------------------------------------------------------

find myself about macOS setup: note/other/newMacOS.md

need to improve it

- add chinese input method
- login the apple account to sync my buildin apps
- since this is 15 inches screen, set display to be more space
- install google chrome and log in my count
- move dock to left and choose automatically hide
- set hot corner left-bottom to be put display to sleep
- using
	First day of week: Monday
	time format: 24-hour time
	temperature: degree celsius
- set night shift from sunrise to sunset
	wait, macOS now have night shift function, do we need the app now??
- able App expose(swipe down with three fingers)
	loop up & data detector(tap with three fingers)
	tap to click
- modified caps-lock key to ctrl key
- show bluetooth in the toolbar

Xcode command line tool
--------------------------------------------------------------------------------

```shell
	xcode-select --install
```

then click and install

it refuses to install xcode-select for me. This is probably OS X command line. Need to update. GOD, reboot works.

Homebrew
--------------------------------------------------------------------------------

```shell
	# download and install brew
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	# tell shell to use brew directory
	echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
	# check the installation
	brew doctor
	# enable cask as a tap
```

iterm2
--------------------------------------------------------------------------------
```shell
	brew cask install iterm2
	# zsh
	brew install zsh
	# Oh My Zsh, this is a framework
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	# set zsh to my default shell
	chsh -s $(which zsh)
```

I would like to play with zsh configuration, [here](https://sourabhbajaj.com/mac-setup/iTerm/zsh.html)

tmux, git, vim
--------------------------------------------------------------------------------
```shell
    # wget
    brew install wget

    # git
	brew install git
    git config --global user.name "Wenchen"
    git config --global user.email "richardlee0211er@gmail.com"
    # iterm2 or zsh will remember your account and password

    # vim
	brew install vim
    wget "TODO" # the config file
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
    # in vim, :PluginInstall

    # tmux
	brew install tmux
    wget "TODO" # the config file


```
I might like to play with this vim theme, [here](https://github.com/square/maximum-awesome)

python
--------------------------------------------------------------------------------
```shell
	brew install python
	# pyenv
	brew install pyenv
	# set up pyenv
	echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
	exec $SHELL
	pyenv install --list
```
TODO: figure out python communite

```shell
	➜  ~ pyenv install 3.5.2
	python-build: use openssl from homebrew
	python-build: use readline from homebrew
	Downloading Python-3.5.2.tar.xz...
	-> https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz
	Installing Python-3.5.2...
	patching file Lib/venv/scripts/posix/activate.fish
	python-build: use readline from homebrew
	Installed Python-3.5.2 to /Users/wenchen/.pyenv/versions/3.5.2
```
[python-setup](https://sourabhbajaj.com/mac-setup/Python/)

TODO: install anaconda.

At this stage, I have too little knowledge about community

Latex
--------------------------------------------------------------------------------

search, download and install. for my lazy reason, install latex with MacTex

or
```shell
	brew install basictex
```

Google Drive
--------------------------------------------------------------------------------
search, download and install

Vmware Fusion
--------------------------------------------------------------------------------
search, download and install
