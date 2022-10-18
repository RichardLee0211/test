who thought setting up printer need a note

Dell 2155cdn Ubuntu driver install

driver from dell doesn't work with ubuntu
from: https://www.dell.com/support/home/en-us/product-support/product/dell-2155cn-cdn/drivers
from: https://www.dell.com/support/kbdoc/en-us/000129694/how-to-install-and-configure-a-dell-printer-using-the-ubuntu-operating-system
rpm2cpio your filename.rpm | cpio --extract --make-directories
sudo chown -R root:root usr
sudo cp -r usr /
sudo service cups restart
ipstat
https://ip:631/Printers



from: https://ubuntuforums.org/showthread.php?t=2053460
Openprinting recommends the Generic PCL 5c Printer - CUPS+Gutenprint v5.2.5 driver for the related 2145cn. You might have some luck there.

no, no lucky so far
