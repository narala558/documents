#! /bin/bash

set -x


BOARD_TAG=mega
BOARD_SUB=atmega2560

sudo pkill screen
s pkill screen; ~/projects/vendor/arduino/arduino --port /dev/ttyACM* --board arduino:avr:mega:cpu=atmega2560 --upload motor_encoder_adjust.ino

ssh $USER@$HOST 'mkdir -p /tmp/foo'
scp $FILE $USER@$HOST:/tmp/foo/foo.ino
ssh $USER@$HOST 'sudo ~/projects/vendor/arduino/arduino --port /dev/ttyACM* --board arduino:avr:mega:cpu=atmega2560 --upload /tmp/foo/foo.ino

# ssh $USER@$HOST 'sudo platformio run --target upload -d /home/pi/projects/arduino/deploy/'
# PROJECT_DIR=$HOME'/projects/arduino/deploy'
# ssh $USER@$HOST "mkdir -p /home/pi/projects/arduino/deploy"
# ssh $USER@$HOST 'platformio init --board megaatmega2560 -d /home/pi/projects/arduino/deploy'
# scp $FILE $USER@$HOST:~/projects/arduino/deploy/src/deploy.ino
# sudo platformio run --target upload -d /home/pi/projects/arduino/deploy/'
