#!/bin/bash

DOCKER_REPOSITORY='kowalikjakub/spp_api:dev'
docker tag spp_api:dev $DOCKER_REPOSITORY

echo "Deploying branch ${TRAVIS_BRANCH}"
docker login -p $DOCKER_PASSWORD -u $DOCKER_USERNAME
if [ $TRAVIS_BRANCH == 'master' ]
then
    docker push $DOCKER_REPOSITORY
elif [ $TRAVIS_BRANCH == 'develop' ]
then
    docker push $DOCKER_REPOSITORY
else
    echo "No matching configuration for ${TRAVIS_BRANCH}, skipping deploy stage"
fi
