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

preference:

need to improve it

- add chinese input method
- keyboard: map mac keyboard to more conventional layout
		modified caps-lock key to ctrl key
	    screenshot and recording options Option+p
	    select next input method using Ctrl+space
		could map move focus to next window to Opt+n,
		or Opt+Esp, but this is just for poker keyboard
- login the apple account to sync my buildin apps
- since this is 15 inches screen, set display to be more space
- install google chrome and log in my count
- share setting could enable ssh, ftp, and smb protocol, might be handy
- move dock to left and choose automatically hide
- set hot corner left-bottom to be put display to sleep
- using
	First day of week: Sunday
	time format: 24-hour time
	temperature: degree celsius
- set night shift from sunrise to sunset
	wait, macOS now have night shift function, do we need the app now??
- able App expose(swipe down with three fingers)
	loop up & data detector(tap with three fingers)
	tap to click
- show bluetooth in the toolbar

Xcode command line tool
--------------------------------------------------------------------------------

```shell
	xcode-select --install
```

then click and install

it refuses to install xcode-select for me. This is probably OS X command line.
Need to update. GOD, reboot works.

Homebrew
--------------------------------------------------------------------------------

```shell
	# download and install brew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	# tell shell to use brew directory
	echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
	# check the installation
	brew doctor
	# enable cask as a tap
```

wow, the default shell changed to zsh in macOS, cool

iterm2
--------------------------------------------------------------------------------
```shell
    brew install --cask iterm2
	# zsh
	brew install zsh
	# Oh My Zsh, this is a framework
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
	# set zsh to my default shell
	chsh -s $(which zsh)
```

warming about ncurses
```shell
    ==> ncurses
    ncurses is keg-only, which means it was not symlinked into /usr/local,
    because macOS already provides this software and installing another version in
    parallel can cause all kinds of trouble.

    If you need to have ncurses first in your PATH, run:
      echo 'export PATH="/usr/local/opt/ncurses/bin:$PATH"' >> ~/.zshrc

    For compilers to find ncurses you may need to set:
      export LDFLAGS="-L/usr/local/opt/ncurses/lib"
      export CPPFLAGS="-I/usr/local/opt/ncurses/include"
```

I would like to play with zsh configuration, [here](https://sourabhbajaj.com/mac-setup/iTerm/zsh.html)

tmux, git, vim
--------------------------------------------------------------------------------
```shell
    # wget
    brew install wget

    # cmake
    brew install cmake

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

m4 warming
```shell
    ==> m4
        m4 is keg-only, which means it was not symlinked into /usr/local,
        because macOS already provides this software and installing another version in
        parallel can cause all kinds of trouble.

        If you need to have m4 first in your PATH, run:
          echo 'export PATH="/usr/local/opt/m4/bin:$PATH"' >> ~/.zshrc
```

Latex
--------------------------------------------------------------------------------

search, download and install. for my lazy reason, install latex with MacTex

or
```shell
	brew install basictex
```

other CLIs
--------------------------------------------------------------------------------
brew install trash
brew install ranger
brew install youtube-dl
brew install tldr
brew install ffmpeg

##### git pub key
enabled github.com two factor auth, can't use account/password anymore
not very flex, don't you think, has to use public key
```shell
	ssh-keygen -t rsa -b 4096 -C your@email.com
	eval "$(ssh-agent -s)" # make sure ssh-agent is running
	ssh-add ~/.ssh/id_rsa
	cat ~/.ssh/id_rsa.pub | pbcopy  # and copy it to github website
	# change origin url
		# url = https://github.com/richardlee0211/test
		url = git@github.com:richardlee0211/test.git

	# ~/.ssh/config
	Host *
		AddKeysToAgent yes
		IdentityFile ~/.ssh/id_rsa

	# test ssh auth
	ssh -T git@github.com

```

search, download and install
--------------------------------------------------------------------------------
- Google Drive
- Vmware Fusion
- spectacle
- IINA and VLC

others
--------------------------------------------------------------------------------

TODO: maybe I need a Code download script to download my code from github in one command

build up a list of my reference repository??

using rsync --progress to copy large file in order to see the speed and progress

experience
--------------------------------------------------------------------------------

##### try to find a good way(software or script) to manage my media files
- Amarok, doesn't support Mac officially

may I could adapt this naming scheme: Suicide.Squad.2016.1080p.HDRip.KORSUB.x264.AAC2.0-STUTTERSHIT.mp4

- easy-tag
brew install easy-tag
nice tool

- exiftool

- vlc Sys+I to trigger inspect windows
