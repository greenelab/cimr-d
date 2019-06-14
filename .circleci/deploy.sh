#!/bin/bash

set -e -x

git config --global user.email "cimrroot@gmail.com"
git config --global user.name "cimrroot"
git config --global push.default simple

# Sync files in "submitted_data" directory to private S3 bucket "cimr-root"
aws s3 sync ~/cimr-d/submitted_data s3://cimr-root

# Sync files in "processed_data" directory to public S3 bucket "cimr-d"
aws s3 sync ~/cimr-d/processed_data s3://cimr-d

# Remove submitted_data from git and commit w/o CircleCI
git rm -r submitted_data/*
git commit -m "CircleCI: clear submitted_data [skip ci]"
git push --force --quiet origin master
