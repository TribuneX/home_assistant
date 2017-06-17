#!/bin/bash

/usr/bin/curl -X GET https://api.travis-ci.org/repos/TribuneX/home_assistant/cc.xml\?branch\=master | grep lastBuildStatus | cut -d'\"' -f2