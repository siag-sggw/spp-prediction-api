#!/bin/bash

echo "Building branch ${TRAVIS_BRANCH}"
if [ $TRAVIS_BRANCH == 'master' ]
then
    docker build --rm --no-cache -t spp_api -f Dockerfile.prod .
else
    docker build --rm --no-cache -t spp_api:dev -f Dockerfile.dev .
fi