#!/bin/bash

CONF_DIR="${TRAVIS_BUILD_DIR}/app_config.json"

if [ $TRAVIS_BRANCH == 'master' ]
then
    echo $PROD_CONFIGURATION >$CONF_DIR
else
    echo $DEV_CONFIGURATION >$CONF_DIR
fi
