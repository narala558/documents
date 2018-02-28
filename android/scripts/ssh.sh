#! /bin/bash

set -x


adb shell 'apt install openssh'

adb push ~/.ssh/id_rsa.pub /data/data/com.termux/files/home/.ssh/authorized_keys

chown root:root /data/data/com.termux/files/home -R
chmod 700 /data/data/com.termux/files/home
chmod 700 /data/data/com.termux/files/home/.ssh/
chmod 600 /data/data/com.termux/files/home/.ssh/*

pkill sshd
sshd -p 22
