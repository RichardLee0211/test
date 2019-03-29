log
================================================================================

network books from [here](https://stackoverflow.com/questions/8122592/which-books-to-learn-sockets-programming-and-tcp-network-communication)

though network test code and note better keep in this repository

could test with
```shell
    ./testServer 8888
    # another terminal
    ./testClient 127.0.0.1 8888 "Message to travel"
```
this is fine. But when test with
```shell
    ./testServer 80 # failed and error couldn't bind?: need sudo to open 80 port
    ./testClient 129.21.248.90 80 "Message to travel" # jammed, I don't know how VM network would deal with it
```

now I got a test code, wanna do it with multiply VM Ubuntu

the host and VM pubic ip are both: 129.21.248.90. this is probably router IP address.
Yes, it is. According to my phone response

if we are using the same public address, then package would travel to the router.
Because router don't forword the package to my computer, then it jammed.

building a new VM ubuntu
account: wenchen
password: abcd

netstat

```shell
    ipconfig getifaddr en0
```
this is like my wifi ip address, as long as clients and servers are in the same wifi network, it works
10.0.5.18
using sudo ./Server 80 may danger my computer

TODO: netstat and ifconfig

NAT is the answer for private IP for public IP translation
from: https://en.wikipedia.org/wiki/Network_address_translation

check Xiang's code
================================================================================
got segmentation fault at the first time I run it


Beej's Guide to Network Programming
================================================================================
Using Internet Sockets

from [here](http://beej.us/guide/bgnet/)
source code for building doc from [here](https://github.com/beejjorgensen/bgnet)

#### 3.2 Byte Order

```cpp
    htons() // hosttonetworkshort
    htonl() // hosttonetworklong
    ntohs() // networktohostshort
    ntohl() // networktohostlong
```

```cpp
    struct addrinfo {
        int              ai_flags;     // AI_PASSIVE, AI_CANONNAME, etc.
        int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
        int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
        int              ai_protocol;  // use 0 for "any"
        size_t           ai_addrlen;   // size of ai_addr in bytes
        struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
        char            *ai_canonname; // full canonical hostname
        struct addrinfo *ai_next;      // linked list, next node
    };

    struct sockaddr {
        unsigned short    sa_family;    // address family, AF_xxx
        char              sa_data[14];  // 14 bytes of protocol address
    };

    // (IPv4 only--see struct sockaddr_in6 for IPv6)
    struct sockaddr_in {
        short int          sin_family;  // Address family, AF_INET
        unsigned short int sin_port;    // Port number
        struct in_addr     sin_addr;    // Internet address
        unsigned char      sin_zero[8]; // Same size as struct sockaddr
    };

    // (IPv4 only--see struct in6_addr for IPv6)
    // Internet address (a structure for historical reasons)
    struct in_addr {
        uint32_t s_addr; // that's a 32-bit int (4 bytes)
    };

    struct sockaddr_storage {
        sa_family_t  ss_family;     // address family
        // all this is padding, implementation specific, ignore it:
        char      __ss_pad1[_SS_PAD1SIZE];
        int64_t   __ss_align;
        char      __ss_pad2[_SS_PAD2SIZE];
    };

    struct sockaddr_in sa; // IPv4
    struct sockaddr_in6 sa6; // IPv6
    inet_pton(AF_INET, "10.12.110.57", &(sa.sin_addr)); // IPv4
    inet_pton(AF_INET6, "2001:db8:63b3:1::3490", &(sa6.sin6_addr)); // IPv6

    // IPv4:
    char ip4[INET_ADDRSTRLEN];  // space to hold the IPv4 string
    struct sockaddr_in sa;      // pretend this is loaded with something
    inet_ntop(AF_INET, &(sa.sin_addr), ip4, INET_ADDRSTRLEN);
    printf("The IPv4 address is: %s\n", ip4);
    // IPv6:
    char ip6[INET6_ADDRSTRLEN]; // space to hold the IPv6 string
    struct sockaddr_in6 sa6;    // pretend this is loaded with something
    inet_ntop(AF_INET6, &(sa6.sin6_addr), ip6, INET6_ADDRSTRLEN);
    printf("The address is: %s\n", ip6);
```

TODO:
- addrinfo
- sockaddr
- sockaddr_in
- nread = recvfrom(sfd, buf, BUF_SIZE, 0, (struct sockaddr *) &peer_addr, &peer_addr_len);

5. System calls or Bust
--------------------------------------------------------------------------------

```cpp
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netdb.h>
    int getaddrinfo(const char *node,     // e.g. "www.example.com" or IP
                    const char *service,  // e.g. "http" or port number
                    const struct addrinfo *hints,
                    struct addrinfo **res);
```

server:
```cpp
    int status;
    struct addrinfo hints;
    struct addrinfo *servinfo;  // will point to the results
    memset(&hints, 0, sizeof hints); // make sure the struct is empty
    hints.ai_family = AF_UNSPEC;     // don't care IPv4 or IPv6
    hints.ai_socktype = SOCK_STREAM; // TCP stream sockets
    hints.ai_flags = AI_PASSIVE;     // fill in my IP for me
    if ((status = getaddrinfo(NULL, "3490", &hints, &servinfo)) != 0) {
            fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status));
            exit(1);
    }
    // servinfo now points to a linked list of 1 or more struct addrinfos
    // ... do everything until you don't need servinfo anymore ....
    freeaddrinfo(servinfo); // free the linked-list
```
