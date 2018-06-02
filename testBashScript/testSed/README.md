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
TODO: come back next time, don't want to spend to much time with text process.I'm not in mood
