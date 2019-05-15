#!/bin/bash

git clone https://github.com/greenelab/cimr.git

cd cimr

# dhu: install git lfs
# https://discuss.circleci.com/t/installing-git-lfs/867/11
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get update
sudo apt-get install git-lfs
git lfs install
ssh git@github.com git-lfs-authenticate greenelab/cimr.git download



git lfs pull

python3 setup.py build
python3 setup.py install

df -h
free -g
free -gt
vmstat -s
