#!/bin/bash

CONF_DIR="${TRAVIS_BUILD_DIR}app_config.json"
echo "Configuring build for branch ${TRAVIS_BRANCH}, configuration directory: ${CONF_DIR}"

if [ $TRAVIS_BRANCH == 'master' ]
then
    echo $PROD_CONFIGURATION >$CONF_DIR
else
    echo $DEV_CONFIGURATION >$CONF_DIR
fi
