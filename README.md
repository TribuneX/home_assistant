<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

<p align="center">
  <img src="https://travis-ci.org/TribuneX/home_assistant.svg?branch=master">
</p>

# My Home Assistant Setup

This repository contains the configuration for my [Home Assistant](https://www.home-assistant.io) (HA) setup. 

## Hardware

### Computing
### [ASUS Tinkerboard](https://www.asus.com/Single-Board-Computer/Tinker-Board/)
Previously, I was running HA on a Raspberry Pi3. The Tinker Board has the following advantages compared to the Pi3:
* Gigabit Ethernet (instead of Fast Ethernet only)
* 2GB of RAM (instead of 1GB only)
* Faster CPU  

The Tinker Board has the same form factor as the Pi3, therefore cases can be reused. 

### Docker
I am running HA as a [Docker Container](https://hub.docker.com/r/homeassistant/raspberrypi3-homeassistant/) with [DietPi](https://dietpi.com) as the Host OS. 
 
### IoT Hardware

* [Ikea TRÅDFRI](https://www.ikea.com/us/en/catalog/categories/departments/lighting/36812/)
* [Xiaomi Vacuum Cleaner v1](https://www.aliexpress.com/item/2016-Original-XIAOMI-MI-Robot-Vacuum-Cleaner-Home-Automatic-Sweeping-Dust-Sterilize-Smart-Planned-Path-Mobile/32756896771.html)
* [Broadlink Mini3](https://www.aliexpress.com/item/Broadlink-RM-Mini-3-Black-Bean-Smart-Home-Automation-Universal-Wifi-Switch-Remote-WiFi-IR-Controller/32828421072.html)
* [Sonos Play1](https://www.sonos.com/en/shop/play1.html)
* [Apple TV4k](https://www.apple.com/de/shop/buy-tv/apple-tv-4k)

#### Xiaomi Smart Home Hardware
I can recommend the Xiaomi Smart Home hardware due to its high build quality and affordable prices. The hardware from Aqara is compatible with the Xiaomi Gateway. Compared to the Xiaomi hardware, the Aqara motion sensor has an additional light sensor and the Aqara temperature sensor has an additional pressure sensor. The Xiaomi hardware works isolated from the Xiaomi cloud. I have the internet access blocked in my router for the Xiaomi gateway.

Currently I am using the follwing Xiaomi Smart Home Hardware:  
* [Xiaomi Smart Home Gateway](https://www.aliexpress.com/item/Original-Xiaomi-Multifunctional-Gateway-Smart-Home-Alarm-System-Intelligent-Mini-Online-Radio-Night-Light-Bell/32741967357.html)
* [Aquara Temperatue / Humidity Sensor](https://www.aliexpress.com/item/Xiaomi-Mi-Aqara-Temperature-Humidity-Sensor-Environment-Air-Pressure-Mijia-Smart-Home-Zigbee-Wireless-Control-Mihome/32851530814.html)
* [Aqara Door Sensor](https://www.aliexpress.com/item/New-Updated-Xiaomi-Aqara-Door-Window-Sensor-Zigbee-Wireless-Connection-Smart-Mini-Door-Sensor-Work-With/32853914826.html)
* [Xiamoi Smart Switch](https://www.aliexpress.com/item/Original-Xiaomi-Smart-Wireless-Switch-for-xiaomi-Smart-Home-House-Control-Center-Intelligent-Multifunction-White-Switch/32801172560.html)
* [Aqara Motion Sensor](https://www.aliexpress.com/item/Original-Mijia-Aqara-Intelligent-human-Infrared-Motion-Sensor-Wireless-Smart-home-Automatic-for-Xiaomi-wireless-gateway/32828911875.html)
* [Xiaomi Plant Senor](https://www.aliexpress.com/item/International-Version-Xiaomi-Mi-Flora-Monitor-Digital-Grass-Flower-Care-Soil-Water-Light-Smart-Tester-Sensor/32856499467.html)

## Configuration Testing
Before pushing my config to this repository, I am using HA running in a [local Docker container](https://github.com/TribuneX/home_assistant/blob/master/testing/docker-compose.yml) to test the configuration files. After pushing changes, [Travis-CI] takes care of verifying the changes.

## Other Services
* [HA-Dockermon](https://hub.docker.com/r/tribunex/ha-dockermon-pi/)
* InfluxDB
* Grafana
* Mosquitto

## Screenshots
![Home Tab](https://raw.githubusercontent.com/TribuneX/home_assistant/master/images/Home_Assistant_tab_1.png)
![Tab2](https://raw.githubusercontent.com/TribuneX/home_assistant/master/images/Home_Assistant_tab_2.png)
![Tab3](https://raw.githubusercontent.com/TribuneX/home_assistant/master/images/Home_Assistant_tab_3.png)