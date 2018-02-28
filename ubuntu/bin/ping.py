#! /usr/bin/python3


import subprocess

try:
    command = 'ping -c 1 -W 1 8.8.8.8'
    out = subprocess.check_output(command.split())
    output = out.decode('utf-8').split('\n')[1:]

    if 'time' in output[0]:
        print('UP')
except:
    print('DOWN')
