#!/bin/bash

if [ -z "$CRUNCH_NEEDED" ]; then
    exit
fi

# Download git-lfs tarball file in /tmp
cd /tmp && wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.2/git-lfs-linux-386-v2.7.2.tar.gz

# Unzip git-lfs tarball file in ~/git-lfs
mkdir ~/git-lfs && cd ~/git-lfs
tar xzf /tmp/git-lfs-linux-386-v2.7.2.tar.gz
sudo ./install.sh

# Install cimr
cd && git clone https://github.com/greenelab/cimr.git
cd ~/cimr
git lfs install && git lfs pull
python3 setup.py build
sudo python3 setup.py install
