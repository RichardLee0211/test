well, Hack is another name for PenTest

nmap_network_scanning pdf from nmap.org
================================================================================

TODO: sectools.org, a collection of security tools

Chapter 3 Host Discovery("Ping Scainning")
--------------------------------------------------------------------------------

feel the urge for IP knowledge

cool, google IP would give a IPv6

IP 67.251.74.131
scame.nmap.org 64.13.134.52

TODO: systemctl command family
TODO: class C around a IP addr

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
