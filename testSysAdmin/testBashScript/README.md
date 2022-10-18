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

some cheat sheet
--------------------------------------------------------------------------------
from: red hat developers
```shell
  env   # display all ENV variables
  grep -i stuff `find . -name \*.txt -print`  # cool
  grep -i ffmpeg `find . -name \*.md -print`

  ## grep through a large and complexed research folder
  ## with --include and --exclude-dir
  (base) ➜  20220127test git:(main) ✗
  grep -rn  --include=\*.md --exclude-dir=node_modules "dl.acm.org" ./
  .//RPE_research/README.md:8:from: https://dl.acm.org/doi/abs/10.1145/1101908.1101941?casa_token=LOWHLGyBbv8AAAAA:GY5l6WGcZNpC8Acf3ujo5J86wdsUp28vt10PmaJl8kl0VQ_rwuoVcyxuXvvmYf641S8JT789XMAIzA
  .//test_frontend/test009/my-app/data01/clusterdata-master/README.md:44:  * [Who Limits the Resource Efficiency of My Datacenter: An Analysis of Alibaba Datacenter Traces](https://dl.acm.org/citation.cfm?doid=3326285.3329074), Jing Guo, Zihao Chang, Sa Wang, Haiyang Ding, Yihui Feng, Liang Mao, Yungang Bao, IEEE/ACM International Symposium on Quality of Service, IWQoS 2019
  .//test_frontend/test009/my-app/data01/clusterdata-master/README.md:51:  * [The Elasticity and Plasticity in Semi-Containerized Co-locating Cloud Workload: a View from Alibaba Trace](https://dl.acm.org/citation.cfm?id=3267830), Qixiao Liu and Zhibin Yu. SoCC2018
  .//test_frontend/test009/my-app/data01/clusterdata-master/cluster-trace-microservices-v2021/README.md:2:The released traces contain the detailed runtime metrics of nearly twenty thousand microservices. They are collected from Alibaba production clusters of over ten thousand [bare-metal nodes](https://dl.acm.org/doi/10.1145/3373376.3378507) during twelve hours in 2021.


  sudo netstat -anp | grep tcp | grep LISTEN   # Lists the various in-use ports and the process using it

  find ./ -mtime 10 # finds all files modified in the last 10 days

  # could have a better way to do this
  history | grep -Ev "(clear|vim|cd|ls|fg|git|jobs|exit).*" |  tail -n 150 | less
  !<num> # to excute a old command

  sestatus

  finger  # shows user information of all the users logged in.
  groups
  useradd
  groupadd
  userdel

  systemctl # ...
  journalctl -f -l -u httpd -u mariadb --since -300 ## system log

  ## netManager cli
  nmcli d
    DEVICE     TYPE      STATE        CONNECTION
    enp0s31f6  ethernet  connected    Wired connection 1
    docker0    bridge    connected    docker0
  nmcli d show enp0s31f6

  ## heredoc
  cat << EOF > /var/www/html/test.php

  iotop



```
