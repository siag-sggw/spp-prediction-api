#!/bin/bash

DOCKER_REPOSITORY='kowalikjakub/spp_api'


echo "Deploying branch ${TRAVIS_BRANCH}"
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
if [ $TRAVIS_BRANCH == 'master' ]
then
    docker tag spp_api $DOCKER_REPOSITORY
    docker push $DOCKER_REPOSITORY
elif [ $TRAVIS_BRANCH == 'develop' ]
then
    docker tag spp_api:dev "$DOCKER_REPOSITORY:dev"
    docker push "$DOCKER_REPOSITORY:dev"
else
    echo "No matching configuration for ${TRAVIS_BRANCH}, skipping deploy stage"
fi
