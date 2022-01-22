well, I don't really need it. But have met it so many times, I got to learn it.
have some command like this:
```bash
    grep -E 'archive.ubuntu.com|security.ubuntu.com' /etc/apt/sources.list.d/*
    sed -i -e \
        's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' \
        /etc/apt/sources.list.d/official-package-repositories.list
```

get a tutorial here: http://www.grymoire.com/Unix/Sed.html
Sed is the ultimate stream editor.
sed s/day/night/ < old > new
Another important concept is that sed is line oriented.
meaning by default only change the first instance per line
GNU to use -r to enable regular expression

book "Sed & Awk"
================================================================================

the satisfaction of solving a problem is the difference between work and drudgery.

sed 's/MA/Massachusetts/' mailList
awk -F, '{ print $1; print $2; print $3; }' mailList

code from: https://github.com/nmcglincy/oreilly-sed-and-awk

TO BE CONTINUE


20220102 extract file extension from tree.md
================================================================================

from: https://developer.ibm.com/tutorials/l-lpic1-103-2/

#### manage PATH strings
```shell
  ## my PATH variable is messed up
  oldPATH=$PATH
  newPATH=`echo $PATH | sed 's/:/\n/g' | sort | uniq | sed 'H;1h;$!d;x;y/\n/:/'`
  export PATH=$newPATH

```

## use tree -N > tree.txt for non-printable characters
## find out what extensions are in my files
## cut is no good for this one
## need to learn sed
cat tree.txt | grep "\." | cut -d . -f -1

## a working one
cat tree.txt  | sed -r 's/.*(\.[a-zA-Z0-9]+)$/\1/' | grep '^\.' | sort | uniq
cat tree.txt  | LC_ALL=C sed -r 's/.*(\.[a-zA-Z0-9]+)$/\1/' | grep '^\.' | sort | uniq   # avoid illegal byte sequence on macOS sed
cat tree.whole.txt  | LC_ALL=C sed -r 's/.*(\.[a-zA-Z0-9]+)$/\1/' | grep '^\.' | sort | uniq

```extension.txt
	.MP4
	.RMVB
	.avi
	.flac
	.flv
	.htm
	.jpeg
	.jpg
	.log
	.m3u
	.m3u8
	.m4v
	.mkv
	.mov
	.mp3
	.mp4
	.nfo
	.nrg
	.opus
	.pdf
	.png
	.rar
	.rm
	.rmvb
	.sfv
	.sh
	.shell
	.srt
	.sub
	.torrent
	.txt
	.url
	.vtt
	.wav
	.webm
```

from: https://www.grymoire.com/Unix/Sed.html
!! this is good !!

## extended regular expression
## \1 and & for matched string

## change order of first three characters
echo abcdef | sed -r 's/^(.)(.)(.)/\3\2\1/'

## remove words other than the first one
echo "word1 word2" | sed -r 's/^([a-zA-Z0-9]+) .*/\1/'
echo "word1 word2 word3" | sed -r 's/[a-zA-Z0-9]+ /DELETED /2'          # only apply to the second match

## add colon at 80th char
sed -r 's/./&:/80'  # or harder way
sed -r 's/................................................................................/&:/'

## replace grep ?: no, I need colored highlight
grep -rn MIME whole/fileMeta.whole.json
sed -n 's/MIME/&/ p' < whole/fileMeta.whole.json    # p for print, only print modified line
## put a space between flags and command

## even numbers and write to file
sed -n 's/^[0-9]*[02468] /&/w even.txt' < file

## /* Ignore Case
sed -n '/mp4/I p' < file

## -e --expression for multiple commands

## count lines not start with #
sed -e 's/^#.*//' f1 f2 f3 | grep -v '^$' | wc -l

sed -e 's/a/A/g' \
       's/e/E/g' \
       's/i/I/g' \
       's/o/O/g' \
       's/u/U/g' < oldfile > newfile

## range
sed '3 s/[0-9]+//'     # remove first number at third line
sed '/^#/ s/[0-9]+//'  # remove first number at lines where first char is #

sed '/\/usr\/local\/bin/ s/\/usr\/local\/bin/\/common\/all\/bin/g'
sed '\_/usr/local/bin_ s_/usr/local/bin_/common/all/bin_g'

sed '200,$ s/A/a/'    # line 200 to the last line
sed '/start/,/stop/ s/#.*//'    # remove comments line from start to stop marks
sed -e '1,/start/ s/#.*//' -e '/end/,$ s/#.*//'     # otherwise

## this can get isolated section out
(base) ➜  testSed git:(master) ✗ sed -n -r '/^>+$/,/^<+$/ p' testfile.txt
>>>>>>>
something
# something else
<<<<<<<


## chop off the head of a mail message
## everything up to the first blank line
sed '1,/^$/ d' <file

sed_head:
sed -n '1,10 p' <file>
```sed_tail.sh
  #!/bin/sh
  #print last 10 lines of file
  # First argument is the filename
  lines=$(wc -l "$1" | awk '{print $1}' )
  start=$(( lines - 10))
  sed "1,$start d" "$1"
```

## remove comments, trailing blanks, and blank lines, !!
sed -e 's/#.//' -e 's/[ ^I]*$//' -e '/^$/ d'


## duplicate blank lines
sed '/^$/ p'

## not !
sed -n '/match/ p'
sed -n '/match/ !p'     # print every line not match, ! apply to the range
sed '/match/ d'         # better

## get youtube ID
(base) ➜  20220103_process git:(master) echo "asd fasdfasdfasdfa sdf-907p_2UhZCU" | sed -r "s/-([_0-9a-zA-Z]){11}/-ID/"
asd fasdfasdfasdfa sdf-ID

```bash
	#!/bin/sh
	# This is a Bourne shell script that removes #-type comments
	# 1~100 line and then between 'begin' and 'end' words.
	sed -n '
	    1,100 {
	        /begin/,/end/ {
	             s/#.*//
	             s/[ ^I]*$//
	             /^$/ d
	             p
	        }
	    }
	'
```

! apple to the range
```bash
	#!/bin/sh
	sed '
	    /begin/,/end/ !{
	         s/#.*//
	         s/[ ^I]*$//
	         /^$/ d
	         p
	    }
	'
```

```bash
#!/bin/sh
sed '
    /begin/,/end/ {
      /begin/n # skip over the line that has "begin" on it
      /end/ !{
        s/old/new/
      }
    }
'
```

```bash
#!/bin/sh
sed '
/WORD/ {
i\
Add this line before
a\
Add this line after
c\
Change the line to this one
}'

#!/bin/sh
sed '
/WORD/ a\
Add this line\
This line\
And this line
'
```

## multi-line pattern
```bash
#!/bin/sh
sed -n '
/ONE/ {
# found "ONE" - read in next line
    N
# look for "TWO" on the second line
# and print if there.
    /\n.*TWO/ p
}' file
```

skip3
```bash
#!/bin/sh
sed '/skip3/ {
           N
           N
           s/skip3\n.*\n.*/# 3 lines deleted/
}'
```

search for two words that might cross line boarder
```bash
#!/bin/sh
sed '
/ONE/ {
# append a line
    N
# "ONE TWO" on same line
    s/ONE TWO/TWO/
# "ONE
# TWO" on two consecutive lines
    s/ONE\nTWO/TWO/
}' file
```

Dig deeper into multiline pattern next time
