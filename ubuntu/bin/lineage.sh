#! /bin/bash

set -x


if [ ! -f ~/bin/repo ]; then
    mkdir -p ~/bin
    curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    chmod a+x ~/bin/repo
fi


mkdir -p ~/android/lineage
cd ~/android/lineage

if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

repo init -u https://github.com/LineageOS/android.git -b cm-14.1
repo sync

# include vendor, kernel, device repos and sync in roomservice.xml
# extract vendor files if not present

source build/envsetup.sh
breakfast athene


croot
brunch athene
