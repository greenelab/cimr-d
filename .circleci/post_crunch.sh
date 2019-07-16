#!/bin/bash
#
# This script is executed at the end of data crunching to save downloaded and
# decompressed files in a temporary location in private S3 bucket.

set -e -x

# Do nothing if "my_request.yml" doesn't exist
if [ ! -f my_request.yml ]; then
    exit 0
fi

# Do nothing if it is not in a PR
# (user request won't be handled when not in a PR)
#if [ ! -z $CIRCLE_PR_NUMBER ]; then
#    exit 0
#fi

# dhu test only
if [ -z $CIRCLE_PR_NUMBER ]; then
    CIRCLE_PR_NUMBER=9876
fi

# Save submitted data to private S3 bucket
if [ -d submitted_data ]; then
    aws s3 sync submitted_data s3://cimr-root/test-submitted/PR_${CIRCLE_PR_NUMBER}
fi

# Save processed data to private S3 bucket as well
if [ -d processed_data ]; then
    aws s3 sync processed_data s3://cimr/test-processed/PR_${CIRCLE_PR_NUMBER}
fi
