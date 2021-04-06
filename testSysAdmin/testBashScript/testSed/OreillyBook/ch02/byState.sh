#! /bin/sh
# command in the book doesn't work on my system, I use:
# sed -f nameState list | ./byState
awk -F, '{
	print $4 ", " $0
}' $* |
# I'm not sure what $* does, it works the same without it.
sort |
awk -F, '
	$1 == LastState {
        print "\t" $2
	}
	$1 != LastState {
        LastState = $1
        print $1
        print "\t" $2
	}
'
