#! /bin/sh

set -x


cd ~/sandbox/
git clone git@github.com:HOST-Oman/libraqm.git
cd libraqm
sudo apt-get install libfreetype6-dev libharfbuzz-dev libfribidi-dev libglib2.0-dev gtk-doc-tools -y
./autogen.sh
./configure
make
make install


cd ~/sandbox/
git clone git@github.com:python-pillow/Pillow.git
cd Pillow
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev \
    tcl8.6-dev tk8.6-dev python-tk -y
MAX_CONCURRENCY=1 python setup.py build_ext --enable-raqm --enable-freetype install
