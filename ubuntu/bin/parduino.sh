#! /bin/bash

set -x


BOARD_TAG=mega
BOARD_SUB=atmega2560

USER='pi'
HOST='192.168.1.102'
FILE=$1

PROJECT_DIR=$HOME'/projects/arduino/deploy'

ssh $USER@$HOST "mkdir -p /home/pi/projects/arduino/deploy"
ssh $USER@$HOST 'platformio init --board megaatmega2560 -d /home/pi/projects/arduino/deploy'
scp $FILE $USER@$HOST:~/projects/arduino/deploy/src/deploy.ino
ssh $USER@$HOST 'sudo platformio run --target upload -d /home/pi/projects/arduino/deploy/'
