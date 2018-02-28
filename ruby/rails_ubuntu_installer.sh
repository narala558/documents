#! /bin/bash
# bash script to install Ruby on Rails on Ubuntu 12.04 LTS


# update 
sudo apt-get update


#install rvm
sudo apt-get install curl
\curl -L https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm requirements


# install ruby
rvm install ruby
rvm use ruby --default


# install ruby gems
rvm rubygems current


# install rails
gem install rails
