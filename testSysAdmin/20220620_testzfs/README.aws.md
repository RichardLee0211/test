####
going AWS or Google Cloud

####
https://console.cloud.google.com/
Google is like 170 dollars per year

####
from: https://aws.amazon.com/ec2/instance-types/t2/
one year for around 70 dollars

name       cpu   mem   cpu redit/hour hourly    1yr        3yr
t2.micro    1    1.0    6             $0.0116    $0.007    $0.005
t2.small    1    2.0    12             $0.023    $0.014    $0.009
t2.medium    2    4.0    24             $0.0464    $0.031    $0.021
t2.large    2    8.0    36             $0.0928    $0.055    $0.037
t2.xlarge    4    16.0    54             $0.1856    $0.110    $0.074
t2.2xlarge    8    32.0    81             $0.3712    $0.219    $0.148

https://lightsail.aws.amazon.com/ls/webapp/home/instances

####
some network CLIs

```shell
  ssh -i "keytest001.pem" <username>@xxxxxxxxxxxxxxx.compute-1.amazonaws.com

  ## iptables
  ## ufw
  ## ping

  ssh -T ubuntu@xxxxxxxxxxx

  (base) ➜  20220127test git:(main) ✗ nmap <ip> -Pn -p ssh
    Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-25 17:12 EDT
    Nmap scan report for XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    Host is up (0.012s latency).

    PORT   STATE SERVICE
    22/tcp open  ssh

    Nmap done: 1 IP address (1 host up) scanned in 0.17 seconds

  ubuntu@ip-xxxxxxxxxxxxx:~$ sudo lsof -i
    COMMAND    PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    systemd-n  396 systemd-network   15u  IPv4  33033      0t0  UDP xxxxxxxxxxxxxxxx.ec2.internal:bootpc
    systemd-r  398 systemd-resolve   13u  IPv4  16607      0t0  UDP localhost:domain
    systemd-r  398 systemd-resolve   14u  IPv4  16608      0t0  TCP localhost:domain (LISTEN)
    chronyd    511         _chrony    5u  IPv4  17284      0t0  UDP localhost:323
    chronyd    511         _chrony    6u  IPv6  17285      0t0  UDP ip6-localhost:323
    sshd       725            root    3u  IPv4  18338      0t0  TCP *:ssh (LISTEN)
    sshd       725            root    4u  IPv6  18349      0t0  TCP *:ssh (LISTEN)
    sshd      2905            root    4u  IPv4  23246      0t0  TCP xxxxxxxxxxxxxxxxxxxx.internal:ssh->xxxxxxxxxxxxxx:50587 (ESTABLISHED)
    sshd      2955          ubuntu    4u  IPv4  23246      0t0  TCP xxxxxxxxxxxxxxxxxxxx.internal:ssh->xxxxxxxxxxxxxx:50587 (ESTABLISHED)

  vislab $ telnet xxxxxxxxxxx 22
    Trying xxxxxxxxxxx...
    Connected to xxxxxxxxxxx.
    Escape character is '^]'.
    SSH-2.0-OpenSSH_8.9p1 Ubuntu-3

  ubuntu@ip-xxxxxxxxxxxxx:~$ netstat -nr
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
    0.0.0.0         xxxxxxxxxxx     0.0.0.0         UG        0 0          0 eth0
    xxxxxxxxxxx     xxxxxxxxxxx     255.255.255.255 UGH       0 0          0 eth0
    xxxxxxxxxxx     0.0.0.0         255.255.240.0   U         0 0          0 eth0
    xxxxxxxxxxx     0.0.0.0         255.255.255.255 UH        0 0          0 eth0

  ubuntu@ip-xxxxxxxxxxxxx:~$ sudo netstat -plantu
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      725/sshd: /usr/sbin
    tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      398/systemd-resolve
    tcp        0   4024 xxxxxxxxxxx24:22        xxxxxxxxxxx242:50587    ESTABLISHED 2905/sshd: ubuntu [
    tcp6       0      0 :::22                   :::*                    LISTEN      725/sshd: /usr/sbin
    udp        0      0 xxxxxxxxxxx23           0.0.0.0:*                           511/chronyd
    udp        0      0 xxxxxxxxxxx53           0.0.0.0:*                           398/systemd-resolve
    udp        0      0 xxxxxxxxxxx24:68        0.0.0.0:*                           396/systemd-network
    udp6       0      0 ::1:323                 :::*                                511/chronyd

  ubuntu@ip-xxxxxxxxxxxxx:~$ sudo iptables -L
    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination

    Chain FORWARD (policy ACCEPT)
    target     prot opt source               destination

    Chain OUTPUT (policy ACCEPT)
    target     prot opt source               destination

  ubuntu@ip-xxxxxxxxxxxxx:~$ netstat -ta
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State
    tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
    tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN
    tcp        0    340 xxxxxxxxxxxxxxxx.ec:ssh xxxxxxxxxxxxxx:50587    ESTABLISHED
    tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
```

####
aws cli

from: https://docs.aws.amazon.com/cli/latest/reference/
from: https://github.com/aws/aws-cli

from: https://www.youtube.com/watch?v=U5y7JI_mHk8&ab_channel=AWSEvents
title: AWS re:Invent 2019: [REPEAT] Introduction to the AWS CLI v2 (DOP343-R)

aws2 configure wizard
aws ec2 describe-instances --instance-ids <id>

[cloudshell-user@ip-xxxxxxxxxxxx]~% aws configure  list
      Name                    Value             Type    Location
      ----                    -----             ----    --------
   profile                <not set>             None    None
access_key     ****************OV74   container-role
secret_key     ****************Vebf   container-role
    region                us-east-1              env    ['AWS_REGION', 'AWS_DEFAULT_REGION']

cat ~/.aws/config

complete -C aws2_completer aws2
aws dynamodb list-tables --output yaml
