#!/bin/bash

cd ~/

git clone https://github.com/greenelab/cimr.git

cd cimr

git lfs pull

python3 setup.py build
sudo python3 setup.py install

