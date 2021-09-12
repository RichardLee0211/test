#!/bin/bash

# PATH="${PATH:+"$PATH:"}$1"

# SOME=thing
# SOME=${SOME:+"$SOME:thing02"}
# echo $SOME

# testuser=rich
# if grep $testuser /etc/passwd; then
#   echo "$testuser directory:"
#   ls -l /home/$testuser/.b*
# else
#   echo "The user doesn't exist on this system"
# fi

# val1=10
# val2=11
#
# if [ $val1 -gt 5 ]; then
#   echo "1"
# fi
#
# if [ $val1 -eq $val2 ]; then
#   echo "2"
# else
#   echo "3"
# fi

# val1=10
# val2=11
# if test $val1 -eq $val2; then
#   echo 2
# else
#   echo 3
# fi

# val1=10
# if (( $val1 ** 2 > 90 )); then
#   (( val2=$val1 ** 2 ))
#   echo "$val2"
# fi

## RegExp
# if [[ $USER == w* ]]; then
#   echo "Hello, $USER"
# else
#   echo "unknown"
# fi

## case switch
# case $USER in
#   rich | barbars )
#     echo 1  ;;
#   testing )
#     echo 2
#     echo testing ;;
#   jessica | wenchen )
#     echo "Don't forget to log off when you're done " ;;
#   * )
#     echo "unkown"
# esac

## this is a quick and dirty way
# for state in Nevada "New Hampshire" "New Maxico" "New York" "North Corolina"; do
#   echo $state
# done


# list="Albama Alaska Arizona Arknasa Colorado"
# list=$list" Connecticut"
#
# for state in $list; do
#   echo "$state"
# done

# file="file.txt"
# for state in `cat $file`; do
#   echo $state
# done


# IFS_OLD=$IFS
# IFS=:
# ## use the new IFS value in code
# for path in $PATH; do
#   echo $path
# done
# IFS=$IFS_OLD
# ## add to a list, sort and print??


# for file in /home/wenchen/Code/*; do
## if [ -d $file ]; then  # ERROR if the path contains space
# for file in /Users/wenchen/Code/_MyTest/*; do
#   if [ -d "$file" ]; then
#     echo $file is a directory
#   elif [ -f "$file" ]; then
#     echo $file is a file
#   fi
# done

## C-style
# for (( i=1; i<=10; i++ )); do
#   echo $i
# done

# for (( a=1,b=10; a<10; a++, b-- )); do
#   echo $a - $b
# done

# val1=10
# while [ $val1 -gt 0 ]; do
#   echo $val1
#   val1=$[ $val1-1 ]
# done

# IFS_OLD=$IFS
# IFS=$'\n'
# for entry in `cat /etc/passwd`; do
#   if [ $entry[0]=='#' ] ; then
#     echo $entry[0]          ## how to retrive the first char??
#     continue
#   fi
#   echo "Values at $entry -"
#   IFS=:
#   for value in $entry; do
#     echo "\t$value"
#   done
#   break
#   echo "error"
# done
# IFS=$IFS_OLD


## bad practise, reture only return 0~255 status code
# function db1 {
#   read -p "Enter a value: " value
#   echo "doubleing the value"
#   return $[ $value*2 ]
# }
# db1
# echo $?

## but I cannot print debug this function anymore
# function db1 {
#   read -p "Enter a value: " value
#   echo $[ $value*2 ]
# }
#
# result=`db1`
# echo $result

## function parameters
# function addem {
#   if [ $# -eq 0 ] || [ $# -gt 2 ]; then
#     echo "error"
#   elif [ $# -eq 1 ]; then
#     echo $[ $1 + $1 ]
#   else
#     echo $[ $1 + $2 ]
#   fi
# }
# echo `addem `
# echo `addem 10 `
# echo `addem 10 20`
