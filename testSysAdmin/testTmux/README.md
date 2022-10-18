install tmux plugin to save session
from: https://github.com/tmux-plugins/tpm
from: https://github.com/tmux-plugins/tmux-resurrect

####

233333, use tmux session to working on the same session
from: https://tmuxcheatsheet.com/
<C-b> + w, session and window preview

doesn't solve copy and paste convenient thing, but it's good

- copy and paste using xsel and xclip

sudo apt install xclip xsel
```~/.zshrc
  ## pbpaste
  # alias pbcopy='xclip -selection clipboard'
  # alias pbpaste='xclip -selection clipboard -o'
  alias pbcopy='xsel --clipboard --input'
  alias pbpaste='xsel --clipboard --output'
```

make sure that tmux session is lauch from host
so that vim set clipboard=unnamedplus works across tmux panel

then yy in vim, jump over to side zsh panel, echo `pbpaste` or <Ctrl+Shift+v>
it doesn't work if tmux session lauched over ssh
we can lauch session from host, and remote ssh into machine,
tmux ls
tmux attach -t <session_id>
and then use `pbpaste` to excute command from readme file

or another work around, yy and p commands into test.sh
and then bash test.sh

or use ssh -X <username>@host
yy and <CMD+v> works

from: https://unix.stackexchange.com/questions/12755/how-to-forward-x-over-ssh-to-run-graphics-applications-remotely
to make pbpaste work, echo $DISPLAY is not null
can use yy and pbpaste to copy and paste long commands
