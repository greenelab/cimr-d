#!/bin/bash
#
# This script is executed at the end of data crunching to save downloaded and
# decompressed files in a temporary location in private S3 bucket.

set -e -x

# Error if any change in "processed/" directory is detected.
git diff origin/master --name-only | grep "^processed/" || PROCESSED_UNCHANGED=true
if [ -z "$PROCESSED_UNCHANGED" ]; then
    echo "Error: Commits in 'processed' directory not allowed!"
    exit 1
fi

# Exit if no yaml files in "submitted/" directory
shopt -s nullglob dotglob

files=(submitted/*.y*ml)
if [ ${#files[@]} -eq 0 ]; then
    exit 0
fi

# Name of flag file, whose existence indicates that request has been handled correctly.
INDICATOR_FILENAME="submitted_data/request.handled"

# Remove flag file before data processing
rm -rf $INDICATOR_FILENAME

# For each yaml file, download and process data
for yaml file in submitted/*.y*ml; do
  cimr processor -process -yaml-file ${yaml_file}
done

# Create the flag file at the end
touch $INDICATOR_FILENAME
