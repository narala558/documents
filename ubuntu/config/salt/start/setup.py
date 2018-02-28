import subprocess
import os


def shell_execute(command):
    """
    """
    subprocess.call(command.split())


if not os.path.exists('/usr/bin/salt-minion'):
    commands = [
        'sudo apt-get --yes -q install python-software-properties',
        'wget https://bootstrap.saltstack.com -O install_salt.sh',
        'sudo sh install_salt.sh -P',
        'sudo apt-get --yes -q install salt-master',
        'sudo apt-get --yes -q install salt-minion',
    ]
    for cmd in commands:
        shell_execute(cmd)


commands = [
    'sudo cp salt/start/minion /etc/salt/',
    'sudo cp salt/start/master /etc/salt/',
    'sudo service salt-master restart',
    'sudo service salt-minion restart',
]

for cmd in commands:
    shell_execute(cmd)

shell_execute('sudo salt-key -A')
shell_execute("sudo salt '*' state.highstate saltenv=base")
