TODO: transfer all mkv file to mp4

book "Linux Commnad line and shell scripting Bible" is helpful

Ch09 Using Structured Commands
--------------------------------------------------------------------------------

```bash
#!/bin/bash
testuser=rich
if grep $testuser /etc/passwd; then
  echo $testuser directory:
  ls -l /home/$testuser/.b*
else
  echo "The user doesn't exist on this system"
fi

```

if command1; then
  commandSet1
elif command2; then
  commandSet2
else
  commandSet3
fi

##### the test command
if test condition; then
  commands
fi

if [ condition ]; then
  commands
fi

!!: test command don't hadnleing floating-point values well
!!: > and < are used as redirection in shell, using \> and \<,
    feel like limited characters issue in the keyboard
```bash
  val1=baseball
  val2=hockey
  if [ $val1 \> $val2 ]; then
    echo 1
  else
    echo 2
  fi
```

##### Advanced if-then Features
- double parenthese for mathematical expressions
- double square bracket for advanced string handling functions, RegExp

```bash
  val1=10
  if (( $val1 ** 2 > 90 )); then
    (( val2=$val1 ** 2 ))
    echo "$val2"
  fi

```
double parenthese:
val++
val--
++val
--val
!     # logical negation
~     # bitwise negation
**    # exponentiation
>>    # left bitwise shift
<<    # right bitwise shift
&     # bitwise AND
|     # bitwise OR
&&    # logical AND
||    # logical OR

Ch10: More Structured Commands
--------------------------------------------------------------------------------

for item in `cat $file`; do
  commands
done

separate content in the file with $IFS
```bash
  IFS_OLD=$IFS
  IFS=$'\n'
  # IFS=$'\n':;"
  ## use the new IFS value in code
  IFS=$IFS_OLD
```

TODO: Chapter 13 Script Control

Ch14 Creating Functions
--------------------------------------------------------------------------------

bash is not very good at functions
TODO: later: array pass, local and global, etc common function problems
```bash
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
```

Ch17 Regular Expressions
--------------------------------------------------------------------------------

other
--------------------------------------------------------------------------------
conclusion is that bash script sucks, but I have to use to do some work, like
manage shell
