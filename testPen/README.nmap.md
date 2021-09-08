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
