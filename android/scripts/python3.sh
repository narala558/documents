#! /system/bin/sh

export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
export PATH=$PATH:/data/data/com.termux/files/usr/bin
export PATH=$PATH:/data/user/0/org.qpython.qpy3/files/bin/


/data/user/0/org.qpython.qpy3/files/bin/qpython3-android5.sh "$@"
