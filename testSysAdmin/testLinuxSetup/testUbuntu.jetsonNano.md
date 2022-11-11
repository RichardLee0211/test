### init
TODO: L4T-README on jetson nano
TODO: jetson nano desktop environment learning

get myself a jetson nano 2GB

burn the image according to nvidia website

- don't have a case for it, it's okay for now
- install a fan on heatsink

Jetson Nano 2GB Developer Kit uses the memory-efficient
- LXDE desktop environment with
- Openbox window manager


- firefox/chromium install vimium, adblock and dark reader
    this could be a heavy program for 2GB jetson nano
- copy vimrc.basic.conf
- install tmux
- install zsh and oh-my-zsh
- wanna get a universal system search tool to lauch programs
- wanna a window manager to bind my key press

### container
from: https://developer.nvidia.com/embedded/learn/tutorials/jetson-container

sudo docker pull nvcr.io/nvidia/l4t-base:r32.4.3
sudo docker image ls
sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix nvcr.io/nvidia/l4t-base:r32.4.3

### VNC
from: https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup

1. Enable the VNC server to start each time you log in
If you have a Jetson Nano 2GB Developer Kit (running LXDE)
    mkdir -p ~/.config/autostart
    cp /usr/share/applications/vino-server.desktop ~/.config/autostart/.

For all other Jetson developer kits (running GNOME)
    cd /usr/lib/systemd/user/graphical-session.target.wants
    sudo ln -s ../vino-server.service ./.

2. config
    gsettings set org.gnome.Vino prompt-enabled false
    gsettings set org.gnome.Vino require-encryption false

3. Set a password to access the VNC server
<<<<<<< HEAD
    # Replace the password with your desired password
    gsettings set org.gnome.Vino authentication-methods "['vnc']"
    gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64)
=======
    # Replace thepassword with your desired password
    gsettings set org.gnome.Vino authentication-methods "['vnc']"
    gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64)

Apple: the client using Apple Screen sharing app, awesome
Linux: sudo apt install gvnviewer, cool

https://en.wikipedia.org/wiki/X_Window_System
https://en.wikipedia.org/wiki/Virtual_Network_Computing

### connect using micro USB
from: https://desertbot.io/blog/jetson-nano-micro-usb-login
from: https://pbxbook.com/other/mac-tty.html
from: https://learn.sparkfun.com/tutorials/terminal-basics/all
from: https://wiki.archlinux.org/title/Working_with_the_serial_console

I like this concept, administration of a machine with no network
An Arch Linux machine can be configured for connections via the serial console port,
which enables administration of a machine even if it has no keyboard, mouse, monitor, or network attached to it.

dmesg # display system message buffer to check if usb device register a com port

screen /dev/cu.usbserial* 115200 -L      # login through usb serial console
minicom -D /dev/tty.usb*                 # prefer screen as it exits more peacefully, and it's easier
stty rows 50 cols 132      # resize the default 24x80 console size

UART: https://learn.sparkfun.com/tutorials/serial-communication/uarts

##### operative wifi config via terminal

WPA: wifi protected access
WPS: wifi protected setup
supplicant,  client station
AP, Authenticator
WPA-PSK: WPA-personal, pre-shared key
WPA-EAP: WPA-Enterprise, with RADIUS authentication server

SSID: name of network
BSSID: AP MAC Address, each access point has its own BSSID, basic service set
ESSID: extended basic service set, BSS+BSS+BSS+BSS+... = ESSID


###### wpa_supplicant_README.txt
wpa_supplicant -B -c/etc/wpa_supplicant.conf -iwlan0   # start, normal would start at boot
wpa_supplicant.example.conf

###### wpa_cli

help
interface wlan0
status
dump = dump config variables
get <name> = get information
pmksa = show PMKSA cache( pairwise master key asscociation)
identity <network id> <identity> = configure identity for an SSID
password <network id> <password> = configure password for an SSID
passphrase <network id> <passphrase> = configure private key passphrase for an SSID
save_config = save the current configuration
terminate = terminate wpa_supplicant

```shell
	> interface
	Available interfaces:
	p2p-dev-wlan0
	wlan0
	> interface wlan0
	Connected to interface 'wlan0.
	> status
	bssid=XXXXXXXXXXXXXXXXX
	freq=2447
	ssid=NETGEAR04
	id=0
	mode=station
	pairwise_cipher=CCMP
	group_cipher=CCMP
	key_mgmt=WPA2-PSK
	wpa_state=COMPLETED
	ip_address=192.168.1.30
	p2p_device_address=XXXXXXXXXXXXXXXXX
	address=XXXXXXXXXXXXXXXXX
	uuid=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	> list_networks
	network id / ssid / bssid / flags
	0       NETGEAR04       any     [CURRENT]

	> scan ## wenchen: ??
	OK
	<3>CTRL-EVENT-SCAN-STARTED
	<3>CTRL-EVENT-SCAN-RESULTS
```

```shell
	╭─wenchen at wenchen-nano in ~
	╰─○ sudo wpa_cli help  | less
	Selected interface 'p2p-dev-wlan0'
	commands:
		status [verbose] = get current WPA/EAPOL/EAP status
		ifname = get current interface name
		ping = pings wpa_supplicant
		relog = re-open log-file (allow rolling logs)
		note <text> = add a note to wpa_supplicant debug log
		mib = get MIB variables (dot1x, dot11)
		help [command] = show usage help
		interface [ifname] = show interfaces/select interface
		level <debug level> = change debug level
		license = show full wpa_cli license
		quit = exit wpa_cli
		set = set variables (shows list of variables when run without arguments)
		dump = dump config variables
		get <name> = get information
		driver_flags = list driver flags
		logon = IEEE 802.1X EAPOL state machine logon
		logoff = IEEE 802.1X EAPOL state machine logoff
		pmksa = show PMKSA cache
		pmksa_flush = flush PMKSA cache entries
		reassociate = force reassociation
		reattach = force reassociation back to the same BSS
		preauthenticate <BSSID> = force preauthentication
		identity <network id> <identity> = configure identity for an SSID
		password <network id> <password> = configure password for an SSID
		new_password <network id> <password> = change password for an SSID
		pin <network id> <pin> = configure pin for an SSID
		otp <network id> <password> = configure one-time-password for an SSID
		passphrase <network id> <passphrase> = configure private key passphrase
			for an SSID
		sim <network id> <pin> = report SIM operation result
		bssid <network id> <BSSID> = set preferred BSSID for an SSID
		blacklist <BSSID> = add a BSSID to the blacklist
		blacklist clear = clear the blacklist
		blacklist = display the blacklist
		log_level <level> [<timestamp>] = update the log level/timestamp
		log_level = display the current log level and log options
		list_networks = list configured networks
		select_network <network id> = select a network (disable others)
		enable_network <network id> = enable a network
		disable_network <network id> = disable a network
		add_network = add a network
		remove_network <network id> = remove a network
		remove_network <network id> = remove a network
		set_network <network id> <variable> <value> = set network variables (shows
			list of variables when run without arguments)
		get_network <network id> <variable> = get network variables
		dup_network <src network id> <dst network id> <variable> = duplicate network variables
		list_creds = list configured credentials
		add_cred = add a credential
		remove_cred <cred id> = remove a credential
		set_cred <cred id> <variable> <value> = set credential variables
		get_cred <cred id> <variable> = get credential variables
		save_config = save the current configuration
		disconnect = disconnect and wait for reassociate/reconnect command before
			connecting
		reconnect = like reassociate, but only takes effect if already disconnected
		scan = request new BSS scan
		scan_results = get latest scan results
		abort_scan = request ongoing scan to be aborted
		bss <<idx> | <bssid>> = get detailed scan result info
		get_capability <eap/pairwise/group/key_mgmt/proto/auth_alg/channels/freq/modes> = get capabilities
		reconfigure = force wpa_supplicant to re-read its configuration file
		terminate = terminate wpa_supplicant
		interface_add <ifname> <confname> <driver> <ctrl_interface> <driver_param>
			<bridge_name> <create> <type> = adds new interface, all parameters but
			<ifname> are optional. Supported types are station ('sta') and AP ('ap')
		interface_remove <ifname> = removes the interface
		interface_list = list available interfaces
		ap_scan <value> = set ap_scan parameter
		scan_interval <value> = set scan_interval parameter (in seconds)
		bss_expire_age <value> = set BSS expiration age parameter
		bss_expire_count <value> = set BSS expiration scan count parameter
		bss_flush <value> = set BSS flush age (0 by default)
		stkstart <addr> = request STK negotiation with <addr>
		ft_ds <addr> = request over-the-DS FT with <addr>
		wps_pbc [BSSID] = start Wi-Fi Protected Setup: Push Button Configuration
		wps_pin <BSSID> [PIN] = start WPS PIN method (returns PIN, if not hardcoded)
		wps_check_pin <PIN> = verify PIN checksum
		wps_cancel Cancels the pending WPS operation
		wps_nfc [BSSID] = start Wi-Fi Protected Setup: NFC
		wps_nfc_config_token <WPS|NDEF> = build configuration token
		wps_nfc_token <WPS|NDEF> = create password token
		wps_nfc_tag_read <hexdump of payload> = report read NFC tag with WPS data
		nfc_get_handover_req <NDEF> <WPS> = create NFC handover request
		nfc_get_handover_sel <NDEF> <WPS> = create NFC handover select
		nfc_report_handover <role> <type> <hexdump of req> <hexdump of sel> = report completed NFC handover
		wps_reg <BSSID> <AP PIN> = start WPS Registrar to configure an AP
		wps_ap_pin [params..] = enable/disable AP PIN
		wps_er_start [IP address] = start Wi-Fi Protected Setup External Registrar
		wps_er_stop = stop Wi-Fi Protected Setup External Registrar
		wps_er_pin <UUID> <PIN> = add an Enrollee PIN to External Registrar
		wps_er_pbc <UUID> = accept an Enrollee PBC using External Registrar
		wps_er_learn <UUID> <PIN> = learn AP configuration
		...
```

###### /etc/wpa_supplicant.conf
some examples at line# 700 of wpa_supplicant.doc.conf file


```wpa_supplicant_README.txt
	# pairwise: list of accepted pairwise (unicast) ciphers for WPA
	# CCMP = AES in Counter mode with CBC-MAC [RFC 3610, IEEE 802.11i/D7.0]
	# TKIP = Temporal Key Integrity Protocol [IEEE 802.11i/D7.0]
	# NONE = Use only Group Keys (deprecated, should not be included if APs support
	# pairwise keys)
	# If not set, this defaults to: CCMP TKIP
```


ifconfig wlan0
```shell
	usb0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
					inet6 fe80::fc8e:47ff:fe70:57e7  prefixlen 64  scopeid 0x20<link>
					ether fe:8e:47:70:57:e7  txqueuelen 1000  (Ethernet)
					RX packets 3344  bytes 752383 (752.3 KB)
					RX errors 0  dropped 0  overruns 0  frame 0
					TX packets 1061  bytes 297472 (297.4 KB)
					TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
					inet 192.168.1.30  netmask 255.255.255.0  broadcast 192.168.1.255
					inet6 fe80::670f:e044:35be:8ed6  prefixlen 64  scopeid 0x20<link>
					ether 00:e0:4c:4b:b7:97  txqueuelen 1000  (Ethernet)
					RX packets 9729  bytes 8684168 (8.6 MB)
					RX errors 0  dropped 0  overruns 0  frame 0
					TX packets 1811  bytes 181115 (181.1 KB)
					TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
iwconfig
```shell
	╭─wenchen at wenchen-nano in ~
	╰─○ iwconfig
	dummy0    no wireless extensions.

	l4tbr0    no wireless extensions.

	eth0      no wireless extensions.

	wlan0     IEEE 802.11bgn  ESSID:"NETGEAR04"  Nickname:"<WIFI@REALTEK>"
						Mode:Managed  Frequency:2.447 GHz  Access Point: 10:0C:6B:12:E7:08
						Bit Rate:72.2 Mb/s   Sensitivity:0/0
						Retry:off   RTS thr:off   Fragment thr:off
						Power Management:off
						Link Quality=100/100  Signal level=64/100  Noise level=0/100
						Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
						Tx excessive retries:0  Invalid misc:0   Missed beacon:0

	usb0      no wireless extensions.

	lo        no wireless extensions.

	docker0   no wireless extensions.

	rndis0    no wireless extensions.

```

NetworkManager
```shell
	╭─wenchen at wenchen-nano in ~
	╰─○ sudo systemctl status NetworkManager.service
	[sudo] password for wenchen:
	● NetworkManager.service - Network Manager
		 Loaded: loaded (/lib/systemd/system/NetworkManager.service; enabled; vendor preset: enabled)
		 Active: active (running) since Tue 2021-08-31 12:49:55 EDT; 21h ago
			 Docs: man:NetworkManager(8)
	 Main PID: 3949 (NetworkManager)
			Tasks: 4 (limit: 2280)
		 CGroup: /system.slice/NetworkManager.service
						 ├─ 3949 /usr/sbin/NetworkManager --no-daemon
						 └─13832 /sbin/dhclient -d -q -sf /usr/lib/NetworkManager/nm-dhcp-helper -pf /run/dhclient

	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1509] device (wlan0): state c
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1530] device (wlan0): state c
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1536] device (wlan0): state c
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1540] manager: NetworkManager
	Sep 01 10:15:16 wenchen-nano dhclient[13832]: bound to 192.168.1.30 -- renewal in 37503 seconds.
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1659] manager: NetworkManager
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1661] policy: set 'NETGEAR04'
	Sep 01 10:15:16 wenchen-nano NetworkManager[3949]: <info>  [1630505716.1678] device (wlan0): Activat
	Sep 01 10:15:28 wenchen-nano NetworkManager[3949]: <info>  [1630505728.2763] manager: NetworkManager
	Sep 01 10:20:24 wenchen-nano NetworkManager[3949]: <info>  [1630506024.7433] connectivity: (l4tbr0)
```

dhclient, dynamic host to get a private IP
```shell
	╭─wenchen at wenchen-nano in ~
	╰─○ sudo dhclient wlan0
	RTNETLINK answers: File exists
```
