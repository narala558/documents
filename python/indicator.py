#! /usr/bin/python

import shlex
import subprocess


def run_shell_command(cmd):
    out = subprocess.check_output(shlex.split(cmd))
    return out.decode('utf-8')


cmd = 'nmcli dev wifi'
out = run_shell_command(cmd)
out = out.split('\n')[1:]
network = next((i for i in out if '*' in i))
network = network.split()[1]

cmd = 'ping 8.8.8.8 -c 1'
out = run_shell_command(cmd)
if 'Unreachable' not in out:
    status = 'Online'
else:
    status = 'Offline'

text = '{} - {}'.format(network, status)
print(text)
