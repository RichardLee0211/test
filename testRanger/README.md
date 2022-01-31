time to start learning more
from: https://ranger.github.io/index.html

## remap ALT+NUM for tab access for it conflicts with i3 config
for now, use TAB to navigate tabs

get img preview, from: https://github.com/ranger/ranger/wiki/Image-Previews
in Debian: sudo apt install w3m-img
``` ~/.config/ranger/rc.config
    set preview_images true
    set preview_images_method urxvt
```

the plain screen lock program slock and i3lock

maybe vimiv is a good replacement for img viewer

ranger --copy-config=all
creating: /home/vislab/.config/ranger/rifle.conf
creating: /home/vislab/.config/ranger/commands.py
creating: /home/vislab/.config/ranger/commands_full.py
creating: /home/vislab/.config/ranger/rc.conf
creating: /home/vislab/.config/ranger/scope.sh

#### colorscheme
feel like ranger give up on colorschemes, need to program to give it new color
from: http://dotshare.it/dots/1465/
from: https://github.com/ranger/ranger/issues/1194
from: https://github.com/ranger/ranger/blob/master/doc/colorschemes.md

a hack:
```shell
dpkg -L ranger
sudo vim /usr/lib/python3/dist-packages/ranger/colorschemes/default.py
## add blue = 220
```

# wenchen: need to change default folder color, too dark
# Which colorscheme to use?  These colorschemes are available by default:
# default, jungle, snow, solarized
set colorscheme default

## .metadata.json, !!
# When the metadata manager module looks for metadata, should it only look for
# a ".metadata.json" file in the current directory, or do a deep search and
# check all directories above the current one as well?
set metadata_deep_search false


# Disable displaying line numbers in main column.
# Possible values: false, absolute, relative.
set line_numbers false

### change python preview color scheme, can not tell in black background
~/.config/ranger/scope.sh  ## this file introduced a lot handy tool
tool used: from: https://pygments.org/styles/
GNU bash manual, from: https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
from: https://www.gnu.org/software/bash/manual/bash.html
```bash
    ## PYGMENTIZE_STYLE=${PYGMENTIZE_STYLE:-autumn}
    PYGMENTIZE_STYLE=${PYGMENTIZE_STYLE:-rrt}
```


### rename
could use I and A to rename, 23333333


### delete, trash
wanna to use Backspace to trash

- add: :touch something.md or <INS>
- minus:
- edit: use E
- delete(trash): dT<return> not work for me, dD<return> works
- operation history(reverse changes on file system)

map s  console shell%space    # exec shell command
map S shell $SHELL            # open shell in this PWD
map <backspace> console delete

zh toggle hidden files

### some improvement:
the command line mod could auto-complete
say I have a file need to move to a directory with a long file name, I couldn't
    say :move this_file_name[tab] Directory_name[tab]

### need to check delete and trash function in ranger
TODO
