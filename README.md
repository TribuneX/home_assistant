<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

# My Home Assistant Setup

This repository contains the configuration for my [Home Assistant](https://www.home-assistant.io) (HA) setup. More information on my HA setup is available on my [blog](https://sascha-bleidner.de). Feel free to reach out to me also via [Twitter](https://twitter.com/sbleidner) or open an issue if you have feedback.

## Host
### ASUS Tinker Board
![Tinker Board](/images/tinkerboard.png)

I moved from a Raspberry Pi3 to an [ASUS Tinker Board](https://www.asus.com/Single-Board-Computer/Tinker-Board/), which has 2GB of RAM and Gigabit Ethernet. It has the same form factor, therefore cases can be reused. 


### Docker
I am running HA as a [Docker Container](https://hub.docker.com/r/homeassistant/raspberrypi3-homeassistant/) with [DietPi](https://dietpi.com) as Host OS. Docker makes it easy to upgrade to the latest HA release, while not having to worry about dependencies and python verions.  
 
## Hardware
While HA supports over 1000 components, I am currently using a small number of hardware.
* [Ikea TRÅDFRI](https://www.ikea.com/us/en/catalog/categories/departments/lighting/36812/)
* [Xiaomi Vacuum Cleaner v1](https://www.aliexpress.com/item/2016-Original-XIAOMI-MI-Robot-Vacuum-Cleaner-Home-Automatic-Sweeping-Dust-Sterilize-Smart-Planned-Path-Mobile/32756896771.html)
* [Sonos Play1](https://www.sonos.com/en/shop/play1.html)
* [Apple TV4k](https://www.apple.com/de/shop/buy-tv/apple-tv-4k)
* [Broadlink Mini3](https://www.aliexpress.com/item/Broadlink-RM-Mini-3-Black-Bean-Smart-Home-Automation-Universal-Wifi-Switch-Remote-WiFi-IR-Controller/32828421072.html)
* [GhostyuBeacon](https://www.aliexpress.com/item/Free-shipping-1pcs-lot-GhostyuBeacon-IBeacon-Base-Station-Low-Power-Consumption-Bluetooth-4-0-Module-CC2541/32561819600.html) for presence detection
* [Sonoff S20](https://www.aliexpress.com/item/Sonoff-S20-EU-UK-US-Plug-Wifi-Power-Socket-Switch-Wireless-Remote-Control-Socket-Outlet-Timing/32823895149.html) flashed with [KamSonoff Firmware](https://github.com/KmanOz/KmanSonoff)
* [AVM Fritz!Box 7580](https://www.amazon.de/AVM-Router-Modem-MU-MIMO-DECT-Basis/dp/B01KKJFJ92/ref=sr_1_1?ie=UTF8&qid=1525735204&sr=8-1&keywords=7580)
* [COMET DECT Thermostats](https://www.eurotronic.org/en/products/comet-dect.html)

#### Xiaomi Smart Home Hardware
I can recommend the Xiaomi Smart Home hardware due to its high build quality and affordable prices. The hardware from Aqara is compatible with the Xiaomi Gateway. Compared to the Xiaomi hardware, the Aqara motion sensor has an additional light sensor and the Aqara temperature sensor has an additional pressure sensor. The Xiaomi hardware works isolated from the Xiaomi cloud. I have the internet access blocked in my router for the Xiaomi gateway.

Currently I am using the following Xiaomi Smart Home Hardware:  
* [Xiaomi Smart Home Gateway](https://www.aliexpress.com/item/Original-Xiaomi-Multifunctional-Gateway-Smart-Home-Alarm-System-Intelligent-Mini-Online-Radio-Night-Light-Bell/32741967357.html)
* [Aquara Temperatue / Humidity Sensor](https://www.aliexpress.com/item/Xiaomi-Mi-Aqara-Temperature-Humidity-Sensor-Environment-Air-Pressure-Mijia-Smart-Home-Zigbee-Wireless-Control-Mihome/32851530814.html)
* [Aqara Door Sensor](https://www.aliexpress.com/item/New-Updated-Xiaomi-Aqara-Door-Window-Sensor-Zigbee-Wireless-Connection-Smart-Mini-Door-Sensor-Work-With/32853914826.html)
* [Xiamoi Smart Switch](https://www.aliexpress.com/item/Original-Xiaomi-Smart-Wireless-Switch-for-xiaomi-Smart-Home-House-Control-Center-Intelligent-Multifunction-White-Switch/32801172560.html)
* [Aqara Motion Sensor](https://www.aliexpress.com/item/Original-Mijia-Aqara-Intelligent-human-Infrared-Motion-Sensor-Wireless-Smart-home-Automatic-for-Xiaomi-wireless-gateway/32828911875.html)
* [Xiaomi Smart Cube](https://www.aliexpress.com/item/Xiaomi-Mi-Magic-Cube-Controller-Zigbee-Version-Controlled-by-Six-Actions-For-Smart-Home-Device-work/32812410838.html) to control the TV
* [Xiaomi Plant Senor](https://www.aliexpress.com/item/International-Version-Xiaomi-Mi-Flora-Monitor-Digital-Grass-Flower-Care-Soil-Water-Light-Smart-Tester-Sensor/32856499467.html)

## Configuration Testing
Before pushing my config to this repository, I am using HA running in a [local Docker container](https://github.com/TribuneX/home_assistant/blob/master/testing/docker-compose.yml) to test the configuration files. After pushing changes, [Travis-CI] takes care of verifying the changes.

## Other Services
* [HA-Dockermon](https://hub.docker.com/r/tribunex/ha-dockermon-pi/) provides a REST-API to restart docker container
* InfluxDB stores timeseries data
* Grafana to visualize the collected data from InfluxDB
* Mosquitto as a MQTT broker for owntracks and Sonoff

## HomeKit
![HomeKit](/images/homekit.png)

Beside the HA web UI, I am using Apple's HomeKit to control my devices via Siri. Since the release 0.64 HA has a native [HomeKit component](https://www.home-assistant.io/components/homekit/). It works more reliable than [HomeBridge](https://github.com/nfarina/homebridge).

## Screenshots
![Home Tab](/images/Home_Assistant_tab_1.png)
![Tab2](/images/Home_Assistant_tab_2.png)
![Tab3](/images/Home_Assistant_tab_3.png)