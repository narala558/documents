#! /bin/sh

cd /home/moriarty/packages/
git clone https://github.com/libimobiledevice/libimobiledevice
git clone https://github.com/libimobiledevice/libplist
git clone https://github.com/libusb/libusb
git clone https://github.com/libimobiledevice/usbmuxd

sudo apt-get remove --purge -y libimobiledevice-dev
sudo apt-get remove --purge -y libplist-dev
sudo apt-get remove --purge -y libusb-dev



cd /tmp
cd /home/moriarty/packages/

cd libplist
./autogen.sh
make
sudo make install


cd /tmp
cd libusb
./autogen.sh
make
sudo make install


cd /tmp
cd libimobiledevice
./autogen.sh
make
sudo make install


cd /tmp
cd usbmuxd
./autogen.sh
make
sudo make install
