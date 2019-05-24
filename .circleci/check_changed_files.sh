#!/bin/bash

#export CRUNCH_NEEDED=false
if [ -n "$CI_PULL_REQUEST" ]; then
    API_URL="https://api.github.com/repos/dongbohu/cimr-d/pulls/10/files"
    new_submitted_data=`curl -s $API_URL | jq '.[].filename' | grep submitted_data`
    if [ -n "$new_submitted_data" ]; then
	export CRUNCH_NEEDED=true
    fi
fi
