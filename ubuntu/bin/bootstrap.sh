#! /bin/sh

set -x

sudo apt-get install --yes -qq git

cd
mkdir -p projects
git clone https://github.com/chillaranand/eddie projects/eddie || true

sudo apt-get install --yes -qq zsh
if [ ! -f ~/.oh-my-zsh/README.md ]; then
    sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
fi

BASE_DIR=$HOME'/projects/01'
CONFIG_DIR=$BASE_DIR'/ubuntu/config'

rm ~/.zshrc
ln -s $CONFIG_DIR'/zsh/zshrc.sh' ~/.zshrc


if [ ! -f /usr/bin/google-chrome ]; then
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list'
    sudo apt-get install --yes -qq google-chrome-stable
    echo "chrome is installed"
fi


sudo apt-get install --yes -qq software-properties-common python python-pip

sudo -H pip install ansible -q

sudo ansible-playbook $CONFIG_DIR'/playbooks/ubuntu.yml' -i localhost, --connection local
