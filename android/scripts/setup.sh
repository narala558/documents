#! /bin/bash

set -eux


adb devices

adb shell su "mount -o remount,rw /"
adb shell "mount -o remount,rw /system"

declare -a directories=(
    "/data/local/scripts" "/data/local/apps" "/data/local/tmp"
    "/bin"  "/usr/bin"
)
for directory in "${directories[@]}"; do
    adb shell mkdir -p "$directory"
done

adb shell "chmod -R 777 /data/local/scripts"
adb shell "chmod -R 777 /data/local/tmp"

adb shell "apt install zsh wget curl util-linux git"


APK_FOLDER=${HOME}'/Dropbox/android'
declare -a apps=(
    'termux.apk'
    # 'qr.apk' 'tea.apk'
    # 'sshdu.apk' 'sshd.apk'
)
# for app in "${apps[@]}"; do
#     adb install "$APK_FOLDER/$app"
# done


CONFIG_FOLDER=${HOME}'/projects/eddie/ubuntu/bin'
adb push -p "$CONFIG_FOLDER/android_sh.sh" /bin/sh
adb shell "chmod +x /bin/sh"
adb push -p "$CONFIG_FOLDER/python.sh" /usr/bin/python
adb shell "chmod +x /usr/bin/python"

adb push -p "$CONFIG_FOLDER/mkshrc.sh" /system/etc/mkshrc


adb shell 'apt install openssh'

adb push ~/.ssh/id_rsa.pub /data/data/com.termux/files/home/.ssh/authorized_keys

mkdir -p /data/data/com.termux/files/home/
chown root:root /data/data/com.termux/files/home/ -R
chmod 700 /data/data/com.termux/files/home
chmod 700 /data/data/com.termux/files/home/.ssh/
chmod 600 /data/data/com.termux/files/home/.ssh/*

pkill sshd
sshd -p 22


adb shell "mount -o remount,ro /"
adb shell "mount -o remount,ro /system"
