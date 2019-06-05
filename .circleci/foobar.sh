#!/bin/bash

set -e -x

git config --global user.email "cimrroot@gmail.com"
git config --global user.name "cimrroot"
git config --global push.default simple

(date; echo "hello from cimrroot") >> foobar.txt
git add foobar.txt
git commit -m "Committed by CircleCI [skip ci]"
git push --set-upstream origin dhu/git-lfs

#git add processed_data/*
#git commit -m "Committed by CircleCI [skip ci]"
#git push --force --quiet origin master
