#!/bin/bash
# GNU bash version 2.X
# the party program -- invitations to friends from the "guest" file

guestfile=~/shell/guests
if [[ ! -e "$guestfile" ]]
then
    printf "${guestfile##*/} non_existent"
    exit 1
fi

export PLACE="Sarotini's"

(( Time=$(date +%H)+1 ))
declare -a foods=(cheese crackers shrimp drinks `"hot dogs"` sandwiches)
declare -i  n=0
for person in $(cat $guestfile)
do
    if  [[ $person == root ]]
    then
        continue
    else
        # Start of here document
        mail –v –s "Party" $person <<- FINIS
      Hi $person! Please join me at $PLACE for a party!
      Meet me at $Time o'clock.
      I'll bring the ice cream. Would you please bring
      ${foods[$n] and anything else you would like to eat?
      Let me know if you can make it.
             Hope to see you soon.
                  Your pal,
                  ellie@$(hostname)
      FINIS
      n=n+1
     if (( ${#foods[*]} ==  $n ))
     then
     declare -a foods=(cheese crackers shrimp drinks `"hot dogs"` sandwiches)
     n=0
 fi
 fi
 done
 printf "Bye..."
