try to build a note taking system with vim,
but vim doesn't do pictures and hard drawing math equations

learn some orgmod

from: https://github.com/jceb/vim-orgmode/blob/master/doc/orgguide.txt
this project is looking for maintainers

from: http://orgmode.org/

from: https://orgmode.org/worg/org-papers.html

from: http://kieranhealy.org/files/misc/workflow-apps.pdf
title: Choosing Your Workøow Applications
author: Kieran Healy, Duke University

from: https://arxiv.org/pdf/1304.1332.pdf
title: What really happened on September 15th 2008? Getting The Most from Your
  Personal Information with Memacs

#####
emacs, evil mode

from: https://www.youtube.com/watch?v=JWD1Fpdd4Pc
title: Evil Mode: Or, How I Learned to Stop Worrying and Love Emacs

from: https://ethanaa.com/blog/switching-to-doom-emacs/#why-the-switch
from: https://github.com/doomemacs/doomemacs

from: https://orgmode.org/manual/Images.html
C-c C-x C-v (org-toggle-inline-images)

####
using emacs on remote machine

install emacs on home server

from: https://www.youtube.com/watch?v=VcgjTEa0kU4&ab_channel=SystemCrafters

####
try this out
from: https://www.vimgolf.com/challenges/4dcd7b572c8e510001000005#
title: Interweave two blocks of text

conscience
ombudsperson
detect and deter
ombud office
prudent
egregious offender
良心
监察员
检测和阻止
监察署
谨慎



a solution:
from: https://stackoverflow.com/questions/10760326/how-to-merge-two-multi-line-blocks-of-text-in-vim
:5,8del | let l=split(@") | 1,4s/$/\=remove(l,0)/
:5,8del
:let l=split(@")
:1,4s/$/\=remove(l,0)/
