#! /system/bin/sh

export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
export PATH=$PATH:/data/data/com.termux/files/usr/bin
export PATH=$PATH:/data/user/0/org.qpython.qpy/files/bin/

source /data/user/0/org.qpython.qpy/files/bin/init.sh

/data/user/0/org.qpython.qpy/files/bin/qpython-android5.sh "$@"
