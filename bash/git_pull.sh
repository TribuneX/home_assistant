#!/bin/bash

cd "/opt/home_assistant/"
git pull
sudo systemctl restart home-assistant@homeassistant
