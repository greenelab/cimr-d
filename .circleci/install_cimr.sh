#!/bin/bash
#
# Install cimr package

set -e -x

git clone https://github.com/greenelab/cimr.git /tmp/cimr
cd /tmp/cimr
# git lfs install && git lfs pull
python3 setup.py build
sudo python3 setup.py install
