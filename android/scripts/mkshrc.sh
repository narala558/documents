# Copyright (c) 2010, 2012, 2013, 2014
#	Thorsten Glaser <tg@mirbsd.org>
# This file is provided under the same terms as mksh.
#-
# Minimal /system/etc/mkshrc for Android
#
# Support: https://launchpad.net/mksh

: ${HOSTNAME:=$(getprop ro.cm.device)}
: ${HOSTNAME:=$(getprop ro.product.device)}
: ${HOSTNAME:=android}
: ${TMPDIR:=/data/local/tmp}
export HOSTNAME TMPDIR

if (( USER_ID )); then PS1='$'; else PS1='#'; fi
PS4='[$EPOCHREALTIME] '; PS1='${|
        local e=$?

        (( e )) && REPLY+="$e|"

        return $e
}$HOSTNAME:${PWD:-?} '"$PS1 "

if [ "z$ANDROID_SOCKET_adbd" != "z" ]; then
   resize
fi



echo '@@@@@@@@@@@@@@@@@@@@@@@@@@'

if [ x"$PYTHONPATH" = x ] ; then
    export PYTHONPATH="/data/user/0/org.qpython.qpy/files/lib/python2.7/site-packages"
else
    export PYTHONPATH="/data/user/0/org.qpython.qpy/files/lib/python2.7/site-packages:$PYTHONPATH"
fi


# termux
export PATH=/data/data/com.termux/files/usr/bin:$PATH
export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
export HOME=/data/data/com.termux/files/home/

echo $PATH
echo $LD_LIBRARY_PATH
echo $PYTHONPATH


# qpython
alias python='/data/user/0/org.qpython.qpy3/files/bin/qpython-android5.sh'
# export PATH=$PATH:/data/data/org.qpython.qpy/files/bin
# alias python=qpython-android5.sh
# alias py=python


mount -o remount,rw /
mount -o remount,rw /system

mkdir -p bin
mkdir -p /usr/bin/

cp /sdcard/scripts/mkshrc.sh /system/etc/mkshrc
cp /sdcard/scripts/bash.sh /bin/bash
cp /sdcard/scripts/bash.sh /bin/sh
cp /sdcard/scripts/python.sh /usr/bin/python
cp /sdcard/scripts/python3.sh /usr/bin/python3


alias sl='ssh -v localhost'
alias c=cat
alias rs='pkill sshd && sshd -p 22'



echo 'Supercharged shell started'
echo '@@@@@@@@@@@@@@@@@@@@@@@@@@'

cd /sdcard/

/bin/sh
