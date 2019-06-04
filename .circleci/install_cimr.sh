#!/bin/bash

set -e -x

# Install git-lfs
cd /tmp
wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.2/git-lfs-linux-386-v2.7.2.tar.gz
mkdir -p git-lfs
cd git-lfs
tar xzf ../git-lfs-linux-386-v2.7.2.tar.gz
sudo ./install.sh

# Install cimr package
cd ~/
git clone https://github.com/greenelab/cimr.git
cd cimr
git lfs install
git lfs pull
python3 setup.py build
sudo python3 setup.py install
