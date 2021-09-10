well, Hack is another name for PenTest

nmap_network_scanning pdf from nmap.org
================================================================================

TODO: sectools.org, a collection of security tools

Chapter 01 Overview
--------------------------------------------------------------------------------

nmap -sS -p- -PS22,80,113,33334 -PAS0,113,21000 -PU19000 -PE -A -T4 -oA \
  avatartcpscan-121503 6.209.24.0/24 6.207.0.0/22

nmap phrases:
- Target enumeration
- host dicovery(ping scanning)
- Reverse-DNS resolution
		-n(no resolution ) to avoid Reverse-DNS resolution
- port scanning
		open, closed, or filtered
- version detection
		-sV
- OS detection
		-O
- traceroute
		--traceroute
- Script scanning
		--script  or -sC
- Output
		XML format or human readable format

Chapter 02 installing...
--------------------------------------------------------------------------------

Chapter 03 Host Discovery("Ping Scainning")
--------------------------------------------------------------------------------

feel the urge for IP knowledge

cool, google IP would give a IPv6

IP 67.251.74.131
scame.nmap.org 64.13.134.52

DONE: systemctl command family
DONE: class C around a IP addr

to study a IP
```shell
nmap -PN -T4 --traceroute www.target.com

whois <IP>

```

#### some re-calls about IPv4

Class A 1.0.0.1   to 126.255.255.254/7     Supports 16 million hosts on each of 127 networks.
Class B 128.1.0.1 to 191.255.255.254/16    Supports 65,000 hosts on each of 16,000 networks.
Class C 192.0.1.1 to 223.255.254.254/24    Supports 254 hosts on each of 2 million networks.
Class D 224.0.0.0 to 239.255.255.255    Reserved for multicast groups.
Class E 240.0.0.0 to 254.255.255.254    Reserved for future use, or research and development purposes.

127.0.0.1 self reflect, stuck between Class A and Class B
192.168.1.1/24 a simple class C Home network
or 192.168.0.0/24

private address in IPv4
Name            CIDR block      Address range                   Number of addresses     Classful description
24-bit block    10.0.0.0/8      10.0.0.0 – 10.255.255.255       16,777,216                Single Class A.
20-bit block    172.16.0.0/12   172.16.0.0 – 172.31.255.255     1,048,576                 Contiguous range of 16 Class B blocks.
16-bit block    192.168.0.0/16  192.168.0.0 – 192.168.255.255   65,536                   Contiguous range of 256 Class C blocks.

DHCP: Dynamic Host Configuration Protocol
to lease IP for Home router
another thing is spectrum IP assigned to client is a Class A IP. WHA

192.168.1.0         This number, called the network number, identifies the network as a whole, and is not assigned to a device.
192.168.1.1         The common default address assigned to the gateway device. In most home networks, the gateway is the router itself.
192.168.1.2         Another common gateway address. Or, it may be assigned to a device on the network.
192.168.1.3–254     Assigned to devices on the network.
192.168.1.255       The broadcast address of the network. Data sent to this address is automatically broadcast to addresses 1–254.

### 3.4 DNS Resolution
-n to disable it

### 3.5 Host Dicovery Controls
#### 3.5.1 List Scan -sL
nmap -sL www.stanford.edu/28
#### 3.5.2 Ping Scan -sP
nmap -sP -T4 www.lwn.net/24
#### 3.5.3. Disable Ping (-PN)
heavy scan at every IP and every port

### 3.6 Host Discovery Tech

standard ICMP echo request
nmap -sP -PE -R -v microsoft.com ebay.com citibank.com google.com \
                   slashdot.org yahoo.com

#### 3.6.1 TCP SYN Ping (-PS<port list>)
=> SYN
<= SYN/ACK
=> ACK

=> SYN
<= RST


#### 3.6.2 TCP ACK Ping (-PA<port list>)
=> ACK
<= RST

nmap -sP -PA www.microsoft.com
netfilter/iptables utility in Linux

#### 3.6.3 UDP Ping (-PU<port list>)
=> empty UDP package to a closed port
<= ICMP port unreachable packet

open port would ignore empty UDP packet
bypass firewall that filter all TCP packets

#### 3.6.4 ICMP Ping Types (-PE, -PP, and -PM)
-PE
=> ICMP type 8 (echo request) packet
<= ICMP type 0 (echo reply) packet

-PP and -PM timestamp and address mask query
timestamp reply (ICMP code 14) and address mask reply (code 18)

#### 3.6.5 IP Protocol Ping (-PO<protocol list>)
just send a IP package with subprotocol number, ICMP(protocol 1), IGMP(protocol 2),
and IP-in-IP(protocol 4)

#### 3.6.6 ARP Scan (-PR)
ARP request MAC that asssociate with the IP
source host machine need to how the MAC to know the endian of packet frame
```shell
	# raw IP ping scan of an offline target
	nmap -n -sP --send-ip 192.168.33.37
	# ARP ping scan of an offline target
	nmap -n -sP -PR --packet-trace --send-eth 192.168.33.37
```

#### 3.7.1 related options
--data-length32 # pretend to be a windows machine
-iL <filename>, -iR <number> # input list, and input randomly from the list
--pakcet-trace # trace every package sent and received

#### 3.7.2 Choosing Ping Options
- Most vauable TCP probe port
	80/http, 14% of open ports
	25/smtp
	22/ssh
	443/https
	21/ftp
	113/auth
	23/telnet, routers and smart switches, unencrypted
	53/domain
	554/rtsp real time stream control protocol
	3389/ms-term-server microsoft terminal services
	1723/pptp point-to-point tunnerling protocol, VPN solutions on Microsoft Windows
	389/ldap Lightweight Directory Access Protocol
	25/SMTP, the Standard Mail Transfer Protocol, unencrypted
	3306/MySQL
	5900/VNC, agraphical desktop sharing system, unencrypted
	...

- UDP
por 53 and port 37452, avoid open port
	631/IPP, internet Printing protocol
	137/NETBIOS-NS, Windows service such as file and printer sharing
	67/DHCPS, DHCP service
	68/DHCPC, DHCP client
	1900/UPNP, Microsoft Simple Service Discovery Protocolal, dicovery of Universal plug-and-play devices

- ICMP
...

default is a TCP ACK packet to port 80, and an ICMP echo request packet

```shell
	# -PE -PP -PS21,22,23,25,80,113,31339 -PA80,113,443,10042

	nmap -n -sL -iR 50000 -oN - | grep "not scanned" | awk '{print $2}' | sort -n > 50K_IPs
	head -5 50K_IPs  # a list of IPs in a file
	nmap -sP -T4 -iL 50K_IPs
	nmap -sP -T4 -iL 50K_IPs -S -oA 50KHosts_DefaultPing

	# repeating ping scan with extra probes
	nmap -sP -PE -PP -PS21,22,23,25,80,113,31339 -PA80,113,443,10042 \
	       -T4 --source-port 53 -iL 50K_IPs -oA 50KHosts_extendedPing

```

Chpter 4 Port Scanning Overview
--------------------------------------------------------------------------------

```shell
	┌──(kali㉿kali)-[~/Code]
	└─$ more /proc/sys/net/ipv4/ip_local_port_range
	32768   60999
```

netstat
```shell
	Active Internet connections (w/o servers)
	Proto Recv-Q Send-Q Local Address           Foreign Address         State
	tcp        0     52 192.168.1.35:ssh        192.168.1.28:53146      ESTABLISHED
	udp        0      0 192.168.1.35:bootpc     192.168.1.1:bootps      ESTABLISHED
	Active UNIX domain sockets (w/o servers)
	Proto RefCnt Flags       Type       State         I-Node   Path
	unix  8      [ ]         DGRAM                    10498    /run/systemd/journal/socket
	unix  2      [ ]         DGRAM                    17171    /run/wpa_supplicant/wlan0
	unix  2      [ ]         DGRAM                    17176    /run/wpa_supplicant/p2p-dev-wlan0
	unix  2      [ ]         DGRAM                    28509    /run/user/133/systemd/notify
	unix  2      [ ]         DGRAM                    19362    /run/user/1000/systemd/notify
	unix  3      [ ]         DGRAM                    10460    /run/systemd/notify
	unix  2      [ ]         DGRAM                    10482    /run/systemd/journal/syslog
	unix  19     [ ]         DGRAM                    10494    /run/systemd/journal/dev-log
	unix  3      [ ]         STREAM     CONNECTED     26970    /run/dbus/system_bus_socket
	unix  3      [ ]         STREAM     CONNECTED     29057
	unix  3      [ ]         STREAM     CONNECTED     21871    @/tmp/.ICE-unix/704
	unix  3      [ ]         STREAM     CONNECTED     20187
	unix  3      [ ]         STREAM     CONNECTED     20658    @/tmp/.X11-unix/X0
	unix  3      [ ]         STREAM     CONNECTED     26969
	unix  3      [ ]         STREAM     CONNECTED     26123    /run/user/133/bus
	unix  3      [ ]         STREAM     CONNECTED     21870
	unix  3      [ ]         STREAM     CONNECTED     21593    @/tmp/dbus-wPWNaz9lK9
	unix  3      [ ]         STREAM     CONNECTED     20396
	unix  3      [ ]         STREAM     CONNECTED     25939    @/tmp/.X11-unix/X1
	...
```
nmap <targetName>
```shell
	➜  ~ nmap 192.168.1.35
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-10 11:00 EDT
	Nmap scan report for 192.168.1.35
	Host is up (0.0044s latency).
	Not shown: 999 closed ports
	PORT   STATE SERVICE
	22/tcp open  ssh

	Nmap done: 1 IP address (1 host up) scanned in 3.92 seconds

	┌──(kali㉿kali)-[~/Code]
	└─$ nmap scanme.nmap.org
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-10 15:08 UTC
	Nmap scan report for scanme.nmap.org (45.33.32.156)
	Host is up (0.087s latency).
	Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
	Not shown: 992 closed ports
	PORT      STATE    SERVICE
	22/tcp    open     ssh
	25/tcp    filtered smtp
	80/tcp    open     http
	135/tcp   filtered msrpc
	139/tcp   filtered netbios-ssn
	445/tcp   filtered microsoft-ds
	9929/tcp  open     nping-echo
	31337/tcp open     Elite

	Nmap done: 1 IP address (1 host up) scanned in 2.65 seconds
```
1. DNS <targetName> to IP
2. Ping the target with ICMP echo and TCP ACK
3. reverse-DNS IP to DomainName, might be different from targetName, -n to skip
4. TCP port scan for popular 1000 ports in nmap-services
5. print results

nmap -p0- -v -A -T4 scanme.nmap.org
-p0-, all 1024 possible port
-v, verbose
-A, aggressive test such as remote OS detection, service/version detection, and Nmap Script Engine
```shell
	┌──(kali㉿kali)-[~/Code]
	└─nmap -nmap -p0- -v -A -T4 scanme.nmap.org                                                  130 ⨯

	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-10 15:35 UTC
	NSE: Loaded 153 scripts for scanning.
	NSE: Script Pre-scanning.
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Initiating Ping Scan at 15:36
	Scanning scanme.nmap.org (45.33.32.156) [2 ports]
	Completed Ping Scan at 15:36, 0.08s elapsed (1 total hosts)
	Initiating Parallel DNS resolution of 1 host. at 15:36
	Completed Parallel DNS resolution of 1 host. at 15:36, 0.01s elapsed
	Initiating Connect Scan at 15:36
	Scanning scanme.nmap.org (45.33.32.156) [65536 ports]
	Discovered open port 22/tcp on 45.33.32.156
	Discovered open port 80/tcp on 45.33.32.156
	Discovered open port 9929/tcp on 45.33.32.156
	Discovered open port 31337/tcp on 45.33.32.156
	Completed Connect Scan at 15:36, 29.42s elapsed (65536 total ports)
	Initiating Service scan at 15:36
	Scanning 4 services on scanme.nmap.org (45.33.32.156)
	Completed Service scan at 15:36, 6.20s elapsed (4 services on 1 host)
	NSE: Script scanning 45.33.32.156.
	Initiating NSE at 15:36
	Completed NSE at 15:36, 5.20s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.34s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.01s elapsed
	Nmap scan report for scanme.nmap.org (45.33.32.156)
	Host is up (0.082s latency).
	Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
	Not shown: 65525 closed ports
	PORT      STATE    SERVICE      VERSION
	0/tcp     filtered unknown
	22/tcp    open     ssh          OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey:
	|   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
	|   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
	|   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
	|_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
	25/tcp    filtered smtp
	80/tcp    open     http         Apache httpd 2.4.7 ((Ubuntu))
	|_http-favicon: Nmap Project
	| http-methods:
	|_  Supported Methods: GET HEAD POST OPTIONS
	|_http-server-header: Apache/2.4.7 (Ubuntu)
	|_http-title: Go ahead and ScanMe!
	135/tcp   filtered msrpc
	137/tcp   filtered netbios-ns
	138/tcp   filtered netbios-dgm
	139/tcp   filtered netbios-ssn
	445/tcp   filtered microsoft-ds
	9929/tcp  open     nping-echo   Nping echo
	31337/tcp open     tcpwrapped
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

	NSE: Script Post-scanning.
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Initiating NSE at 15:36
	Completed NSE at 15:36, 0.00s elapsed
	Read data files from: /usr/bin/../share/nmap
	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 43.14 seconds

```

#### 4.3.1 Selecting Scan Techniques
TCP SYN Stealth (-sS)
TCP Connect (-sT)
UDP (-sU)
TCP FIN, Xmas, and Null (-sF, -sX, -sN)
TCP ACK (-sA)
TCP Window (-sW)
TCP Maimon (-sM)
TCP Idle (-sI <zombie host>)
IP protocol (-sO)
TCP FTP bounce (-b <FTP bounce proxy>)

-p22,25,80,0-100,600-
-pT:21,23,110,U:53,111,137,161

-T0 to -T5

-oN <fileName> # (normal)
-oG <fileName> # (grepable)
-oX <fileName> # (XML)
-oA <baseName> # (all formats)

firewall and IDS(Intrusion Detection Systems)

###### playboy example
American Tegistry Internet Number (ARIN)
```shell
	whois -h whois.arin.net -n playboy
	ping -c5 www.playboy.com
	dig @ns1-chi.playboy.com. any
	# ICMP echo ping
	ping -c4 mx.chi.playboy.com
	ping -c4 mx.chi.playboy.com
	# hping2 TCP ping against port 25
	hping2 --syn -p 25 -c 5 mx.chi.playboy.com

	# -PN skip ping stage, -n skip rNDS stage
	nmap -T4 -p80 -PN --mac-rtt-timeout 200 --initial-rtt-timeout 150 \
	--min-hostgroup 512 -n -oG pb-port80scan-%D.gnmap 216.162.128.0/20

	egrep '[^0-9]80/open' pb-port80scan-*.gnmap

```

chapter 8 Remote OS Detection
--------------------------------------------------------------------------------

nmap -O -v scanme.nmap.org
```shell
	➜  testLinuxSetup git:(master) ✗ sudo nmap -O -v scanme.nmap.org
	Password:
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-10 14:07 EDT
	Initiating Ping Scan at 14:07
	Scanning scanme.nmap.org (45.33.32.156) [4 ports]
	Completed Ping Scan at 14:07, 0.07s elapsed (1 total hosts)
	Initiating Parallel DNS resolution of 1 host. at 14:07
	Completed Parallel DNS resolution of 1 host. at 14:07, 0.02s elapsed
	Initiating SYN Stealth Scan at 14:07
	Scanning scanme.nmap.org (45.33.32.156) [1000 ports]
	Discovered open port 80/tcp on 45.33.32.156
	Discovered open port 22/tcp on 45.33.32.156
	Discovered open port 31337/tcp on 45.33.32.156
	Discovered open port 9929/tcp on 45.33.32.156
	Completed SYN Stealth Scan at 14:07, 7.07s elapsed (1000 total ports)
	Initiating OS detection (try #1) against scanme.nmap.org (45.33.32.156)
	Retrying OS detection (try #2) against scanme.nmap.org (45.33.32.156)
	Nmap scan report for scanme.nmap.org (45.33.32.156)
	Host is up (0.081s latency).
	Not shown: 991 closed ports
	PORT      STATE    SERVICE
	22/tcp    open     ssh
	25/tcp    filtered smtp
	80/tcp    open     http
	111/tcp   filtered rpcbind
	161/tcp   filtered snmp
	705/tcp   filtered agentx
	2049/tcp  filtered nfs
	9929/tcp  open     nping-echo
	31337/tcp open     Elite
	Aggressive OS guesses: Linux 2.6.32 (88%), Linux 3.4 (88%), Linux 3.5 (88%), Linux 4.2 (88%), Linux 4.4 (88%), Synology DiskStation Manager 5.1 (88%), WatchGuard Fireware 11.8 (88%), Linux 2.6.35 (87%), Linux 3.10 (87%), Linux 2.6.32 or 3.10 (87%)
	No exact OS matches for host (test conditions non-ideal).
	Uptime guess: 41.913 days (since Fri Jul 30 16:13:56 2021)
	TCP Sequence Prediction: Difficulty=262 (Good luck!)
	IP ID Sequence Generation: All zeros

	Read data files from: /usr/local/bin/../share/nmap
	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 12.97 seconds
						 Raw packets sent: 1398 (65.894KB) | Rcvd: 1301 (53.582KB)

```

nmap -sV -O -v 192.168.1.XX

log 20210901
--------------------------------------------------------------------------------

find out my RPi on my network, yeah, I have my own router now.

nmap -sL 192.168.56.0/24    # scan for live hosts, no one's live, blocked
nmap -sn 192.168.56.0/24    # find and ping all live hosts
```shell
	➜  testLinuxSetup git:(master) nmap -sn 192.168.1.28/24
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 10:48 EDT
	Nmap scan report for 192.168.1.1
	Host is up (0.0028s latency).
	Nmap scan report for 192.168.1.2
	Host is up (0.0040s latency).
	Nmap scan report for 192.168.1.3
	Host is up (0.0039s latency).
	Nmap scan report for 192.168.1.4
	Host is up (0.028s latency).
	Nmap scan report for 192.168.1.5
	Host is up (0.012s latency).
	Nmap scan report for 192.168.1.7
	Host is up (0.046s latency).
	Nmap scan report for 192.168.1.12
	Host is up (0.051s latency).
	Nmap scan report for 192.168.1.14
	Host is up (0.029s latency).
	Nmap scan report for 192.168.1.28
	Host is up (0.011s latency).
	Nmap scan report for 192.168.1.37
	Host is up (0.098s latency).
	Nmap scan report for 192.168.1.38
	Host is up (0.038s latency).
	Nmap done: 256 IP addresses (11 hosts up) scanned in 29.80 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -sn 192.168.1.35
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:22 EDT
	Nmap scan report for 192.168.1.35
	Host is up (0.21s latency).
	MAC Address: XXXXXXXXXXXXXXXXX (Raspberry Pi Trading)
	Nmap done: 1 IP address (1 host up) scanned in 0.28 seconds
```

nmap 192.168.56.1,100-102   # find open ports
nmap -sV 192.168.56.102     # find services Listening


```shell
	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.38
	Password:
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 11:56 EDT
	Nmap scan report for 192.168.1.38
	Host is up (0.030s latency).
	Not shown: 999 closed ports
	PORT     STATE SERVICE
	4000/tcp open  remoteanything
	MAC Address: XXXXXXXXXXXXXXXXX (Apple)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 33.02 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.37
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 11:59 EDT
	Nmap scan report for 192.168.1.37
	Host is up (0.038s latency).
	Not shown: 999 closed ports
	PORT      STATE SERVICE
	62078/tcp open  iphone-sync
	MAC Address: XXXXXXXXXXXXXXXXX (Unknown)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 113.29 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.14
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:03 EDT
	Nmap scan report for 192.168.1.14
	Host is up (0.050s latency).
	Not shown: 999 closed ports
	PORT   STATE SERVICE
	22/tcp open  ssh
	MAC Address: XXXXXXXXXXXXXXXXX (Murata Manufacturing)
	Device type: general purpose
	Running: Linux 3.X|4.X
	OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
	OS details: Linux 3.2 - 4.9
	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 5.85 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.12
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:07 EDT
	Nmap scan report for 192.168.1.12
	Host is up (0.063s latency).
	All 1000 scanned ports on 192.168.1.12 are closed
	MAC Address: XXXXXXXXXXXXXXXXX (Xiaomi Communications)
	Too many fingerprints match this host to give specific OS details
	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 29.36 seconds


	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.7
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:08 EDT
	Nmap scan report for 192.168.1.7
	Host is up (0.011s latency).
	Not shown: 999 closed ports
	PORT     STATE SERVICE
	8000/tcp open  http-alt
	MAC Address: XXXXXXXXXXXXXXXXX (Shenzhen Rf-link Technology)
	Device type: general purpose
	Running: Linux 2.6.X|3.X
	OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
	OS details: Linux 2.6.32 - 3.10
	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 3.68 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.5
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:09 EDT
	Nmap scan report for 192.168.1.5
	Host is up (0.020s latency).
	Not shown: 999 closed ports
	PORT      STATE SERVICE
	28201/tcp open  unknown
	MAC Address: XXXXXXXXXXXXXXXXX (Unknown)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 52.17 seconds


	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.4
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:11 EDT
	Nmap scan report for 192.168.1.4
	Host is up (0.024s latency).
	All 1000 scanned ports on 192.168.1.4 are closed
	MAC Address: XXXXXXXXXXXXXXXXX (Shenzhen Bilian Electronicltd)
	Too many fingerprints match this host to give specific OS details
	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 4.49 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.3
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:12 EDT
	Nmap scan report for 192.168.1.3
	Host is up (0.016s latency).
	Not shown: 999 closed ports
	PORT     STATE SERVICE
	9999/tcp open  abyss
	MAC Address: XXXXXXXXXXXXXXXXX (Tp-link Technologies)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 15.63 seconds


	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.2
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:13 EDT
	Nmap scan report for 192.168.1.2
	Host is up (0.023s latency).
	Not shown: 999 closed ports
	PORT     STATE SERVICE
	9999/tcp open  abyss
	MAC Address: XXXXXXXXXXXXXXXXX (Tp-link Technologies)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 18.43 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.1
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:14 EDT
	Nmap scan report for 192.168.1.1
	Host is up (0.017s latency).
	Not shown: 995 closed ports
	PORT      STATE SERVICE
	53/tcp    open  domain
	80/tcp    open  http
	443/tcp   open  https
	8200/tcp  open  trivnet1
	49152/tcp open  unknown
	MAC Address: XXXXXXXXXXXXXXXXX (Netgear)
	No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
	TCP/IP fingerprint:
	OS:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 14.35 seconds

	➜  testLinuxSetup git:(master) ✗ sudo nmap -O 192.168.1.35
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-01 12:21 EDT
	Nmap scan report for 192.168.1.35
	Host is up (0.028s latency).
	Not shown: 999 closed ports
	PORT   STATE SERVICE
	22/tcp open  ssh
	MAC Address: XXXXXXXXXXXXXXXXX (Raspberry Pi Trading)
	Device type: general purpose
	Running: Linux 4.X|5.X
	OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
	OS details: Linux 4.15 - 5.6
	Network Distance: 1 hop

	OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 2.51 seconds

```
