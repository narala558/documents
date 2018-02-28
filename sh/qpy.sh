#! /bin/bash

set -eux

QPY_URL=https://github.com/qpython-android/qpython/releases/download/1.2.6/qpython-app-release-1.2.6.apk
BBOX_URL=https://busybox.net/downloads/binaries/1.21.1/busybox-armv7l


DEVICE_COUNT=$(adb devices | grep device$ | wc -l)
if [ $DEVICE_COUNT -eq 0 ]; then
    echo "No device connected."
    exit
elif [ $DEVICE_COUNT -gt 1 ]; then
    echo "Connect only one device."
    exit
fi

PD=$(pwd)
WD=$PD'/tmp'
mkdir -p "$WD"
cd "$WD"

SERIAL=$(adb devices | grep "device$" | awk '{print $1}')
SDK_VERSION=$(adb shell "getprop ro.build.version.sdk" | tr '\r' ' ' | xargs)

wget -qc "$FRIDA_URL"
unxz -fk $(basename $FRIDA_URL)

adb shell "mkdir -p /data/local/tmp/"
adb install $(basename $QPY_URL) &> /dev/null

set +x

if ! adb shell "pm list packages" | grep "org.qpython.qpy" 1> /dev/null; then
    adb shell "monkey -p org.qpython.qpy 1" &> /dev/null
    echo
    echo "In 'Qpython' app > tap Python logo > 'Run local script' > 'helloworld.py' > tap 'Okay'"
    read -n 1 -s -p "Press any key when done..."
    echo
fi

if [[ $(adb shell "getprop ro.build.host" | tr '\r' ' ' | xargs) != "cyanogenmod" ]]; then
    adb install $PD/vendor/apps/adbd-Insecure-v2.00.apk &> /dev/null
    adb shell "monkey -p eu.chainfire.adbd 1" &> /dev/null
    echo
    echo "In 'adbd Insecure' app > 'Enable Insecure adbd' > 'Enable at boot'"
    read -n 1 -s -p "Press any key when done..."
    echo
fi

adb root

set -x


if [[ $SDK_VERSION -ge 21 ]]; then
    PY_EXEC="qpython-android5.sh"
else
    PY_EXEC="qpython.sh"
fi

# Install Python and pip requirements
adb shell "
    echo '#!/system/bin/sh' > /data/data/org.qpython.qpy/files/bin/end.sh;
    export PATH=\$PATH:/data/data/org.qpython.qpy/files/bin;
    cd /data/data/org.qpython.qpy/files/bin;
    $PY_EXEC pip install Pyro4 selectors34 retrying python-logstash <<< yes;
"

adb shell "mount -o remount,rw /system"
adb shell "sync"
