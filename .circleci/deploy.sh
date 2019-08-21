#!/bin/bash
#
# This script will be triggered when "master" branch is updated.
# It copies "submitted_data" and "processed_data" to permanent locations in S3
# buckets, cleans up everything in "submitted/" sub-directory and commits the
# changes back to remote repo.

set -e -x

function delete_requests() {
    if [ -f submitted/*.yml ] || [ -f submitted/*.yaml ]; then
	git rm --ignore-unmatch submitted/*.yml submitted/*.yaml
	git commit -m "CircleCI: Delete requests in submitted/ dir [skip ci]"
	git push --force --quiet origin master
    fi
}

# Git config
git config --global user.email "cimrroot@gmail.com"
git config --global user.name "cimrroot"
git config --global push.default simple

cd ~/cimr-d/

# Find the PR number of the latest commit
LATEST_COMMIT_HASH=$(git log -1 --pretty=format:%H)
GITHUB_SEARCH_URL="https://api.github.com/search/issues?q=sha:${LATEST_COMMIT_HASH}"
PR_NUMBER=$(curl -s $GITHUB_SEARCH_URL | jq '.items[0].number')

# If we're not merging a PR, clean up "submitted/" dir and exit.
if [ $PR_NUMBER == 'null' ]; then
    delete_requests
    exit 0
fi

# If we are merging a PR, but the indicator object is not found in S3 bucket,
# data processing must either fail or not start at all, so we exit too.
INDICATOR_FIELNAME="submitted_data/request.handled"
if [ ! -f ${INDICATOR_FIELNAME} ]; then
    delete_requests
    exit 0
fi

# Use the latest "pip"
sudo pip install --upgrade pip

# Install awscli to make "aws" command available
sudo pip install awscli

# Copy "processed_data" to "cimr-d" bucket (public).
# "PR-<n>" is inserted in the filename to avoid possible duplicate filenames.
OUTPUT_FILES=$(find processed_data -type f)
for f in ${OUTPUT_FILES}; do
    g=$(echo $f | cut -d'/' -f'2-')                # strip "processed_data/" from $f
    g_stem1="${g%.*}"                              # full path without the last extension
    g_ext1="${g##*.}"                              # last extension

    if [ "${g_ext1}" == "$g" ]; then               # "foo" will become "foo-PR-n"
	s3name=$g-PR-${PR_NUMBER}
    else
	g_stem2="${g_stem1%.*}"
	g_ext2="${g_stem1##*.}"
	if [ "${g_ext2}" == "${g_stem1}" ]; then   # "foo.ext1" will become "foo-PR-n.ext1"
	    g_stem=${g_stem1}
	    g_ext=${g_ext1}
	else                                       # "foo.ext2.ext1" will become "foo-PR-n.ext2.ext1"
	    g_stem=${g_stem2}
	    g_ext=${g_ext2}.${g_ext1}
	fi
	s3name="${g_stem}-PR-${PR_NUMBER}.${g_ext}"
    fi
    aws s3 cp $f s3://cimr-d/${s3name}
done

# Copy "submitted_data" to "cimr-root" bucket (private)
aws s3 sync submitted_data/  s3://cimr-root/PR-${PR_NUMBER}/ --exclude "request.handled"

# Move submitted YAML files to "processed/" sub-dir
mkdir -p processed/PR-${PR_NUMBER}/
git mv -k submitted/*.yml submitted/*.yaml processed/PR-${PR_NUMBER}/

# Update "processed/README.md", which lists all files in "cimr-d" S3 bucket
aws s3 ls cimr-d --recursive --human-readable > processed/s3_list.txt
python3 .circleci/txt2md.py
git add processed/README.md

# Update "cimr-d_catalog.txt"
git add cimr-d_catalog.txt

# Commit changes and push them to remote "master" branch
git commit -m "CircleCI: Save processed requests [skip ci]"
ssh-keyscan github.com >> ~/.ssh/known_hosts
git push --force --quiet origin master
