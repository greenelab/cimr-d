#!/bin/bash

cd;
mkdir git-lfs
cd git-lfs
wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.2/git-lfs-linux-386-v2.7.2.tar.gz
tar xzf git-lfs-linux-386-v2.7.2.tar.gz
mv git-lfs-linux-386-v2.7.2.tar.gz /tmp/
sudo ./install.sh

cd; git clone https://github.com/greenelab/cimr.git

cd cimr

# dhu: install git lfs
# https://discuss.circleci.com/t/installing-git-lfs/867/11
#curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
#sudo apt-get update
#sudo apt-get install git-lfs --yes --quiet
#git lfs install

git lfs pull

python3 setup.py build
sudo python3 setup.py install

echo; echo "df -h"
df -h

echo; echo "free -g"
free -g

echo; echo "free -gt"
free -gt

echo; echo "vmstat -s"
vmstat -s
