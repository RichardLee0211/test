from the hacking book
well, I have to say this is 2000 hack book, high posibility it's out of date,
and I'm not in China network

# ch02, DNS
nslookup
dig

TODO: what's www.lycos.com search engine?? similar to google??

whois doman database
whois server

2.2.2 using command line to footprint
that's why we will need Kaili machine
1. finger
2. whois or telnet
3. Nslookup
4. dig
5. ping
6. traceroute
7. pathping

3.2.1 port scan methods
1. TCP connect scan
2. TCP SYN scan
3. TCP FIN scan
...

3.2.4 clasical multi-functional scan tool - Nmap
Nmap, network mapper
```bash
nmap -sP 192.168.0.0/27

```

Log
--------------------------------------------------------------------------------

2019/06/25
--------------------------------------------------------------------------------

Security hole at admin:admin at 192.168.1.1
WPS, wifi protected Setup, connect device without password
WPA Personal
WPA2 Personal security protocols
Deprecated WEP security, cracked easily

Wifi name: named SSID
Password: WPA-PSK key

DHCP

if need to access home’s wifi, could browser a tablet and access 192.168.1.1, the router IP, and then brute force the password, usually simple. Then we have the password of wifi. The router password would usually have something to do with address.

OMG, 3 mile wifi receive device

Through router information, we have a 192.168.1.3 to scan

Cops radio

Some wifi crack command
```
Ifconfig # or ip a
Airman-ng start wlan0
Airodump-ng wlan0mon
Aireplay-ng
Aireplay-ng —test wlan0mon
Besside-ng —help
Besside-ng wlan
```

DONE: Okay, to finish the hype, I need to finish reading these blogs.

https://null-byte.wonderhowto.com/how-to/4-ways-crack-facebook-password-protect-yourself-from-them-0139532/

A facebook security blog in 2017

TODO: learn matesploit: https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
https://www.metasploit.com/get-started
